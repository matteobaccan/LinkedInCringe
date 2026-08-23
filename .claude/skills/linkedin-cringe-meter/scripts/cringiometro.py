#!/usr/bin/env python3
"""Cringiometro: genera l'immagine di risposta (PNG 1080x1080 + SVG) da un JSON.

Uso:
    python cringiometro.py dati.json cartella_output/

dati.json:
    {
      "score": 7,                      # 1-10, interi o mezzi (7.5)
      "register": "credibile",         # credibile | parodico | dichiarato
      "modules": [                     # max 8, in ordine di importanza
        {"code": "C01", "name": "Parabola forzata"},
        {"code": "C13", "name": "Numeri finti-precisi"}
      ],
      "verdict": "Un 7 solido. Mancano i numeri finti per il podio.",
      "quote": "Le persone non lasciano le aziende. Lasciano le macchinette.",
      "footer": "github.com/matteobaccan/LinkedInCringe",  # opzionale
      "lang": "en",                    # lingua dei testi fissi: it (default), en, de, fr, es
      "labels": {"title": "..."}       # opzionale: override dei testi fissi
    }

I nomi dei moduli, il verdetto e la citazione vanno scritti già nella lingua del post.

Niente nomi, foto o headline dell'autore: l'immagine giudica il post, non la persona.
Il PNG richiede Pillow; se manca, viene scritto solo l'SVG.
"""
import json
import math
import os
import sys

W = H = 1080
BG = (247, 243, 234)
INK = (28, 28, 32)
MUTED = (110, 108, 100)
CARD = (255, 255, 255)
STOPS = [(0.0, (52, 168, 83)), (0.5, (244, 180, 0)), (1.0, (217, 48, 37))]

# Testi fissi dell'immagine, per lingua. "lang" nel JSON sceglie la lingua; una
# lingua non presente ricade sull'inglese; "labels" nel JSON sovrascrive i singoli
# campi (utile per una terza lingua senza toccare lo script).
LANGS = {
    "it": {
        "title": "CRINGIOMETRO",
        "register": {"credibile": "registro credibile", "parodico": "registro parodico",
                     "dichiarato": "cringe dichiarato"},
        "words": ["innocuo", "lieve", "fastidioso", "imbarazzante", "insostenibile", "leggendario"],
    },
    "en": {
        "title": "CRINGE METER",
        "register": {"credibile": "believable register", "parodico": "parody register",
                     "dichiarato": "declared cringe"},
        "words": ["harmless", "mild", "annoying", "embarrassing", "unbearable", "legendary"],
    },
    "de": {
        "title": "CRINGEOMETER",
        "register": {"credibile": "glaubwürdig", "parodico": "Parodie",
                     "dichiarato": "erklärter Cringe"},
        "words": ["harmlos", "leicht", "nervig", "peinlich", "unerträglich", "legendär"],
    },
    "fr": {
        "title": "CRINGEOMÈTRE",
        "register": {"credibile": "registre crédible", "parodico": "registre parodique",
                     "dichiarato": "cringe assumé"},
        "words": ["anodin", "léger", "agaçant", "gênant", "insoutenable", "légendaire"],
    },
    "es": {
        "title": "CRINGÓMETRO",
        "register": {"credibile": "registro creíble", "parodico": "registro paródico",
                     "dichiarato": "cringe declarado"},
        "words": ["inocuo", "leve", "molesto", "vergonzoso", "insoportable", "legendario"],
    },
}


def lerp_color(t):
    t = max(0.0, min(1.0, t))
    for (t0, c0), (t1, c1) in zip(STOPS, STOPS[1:]):
        if t <= t1:
            k = 0 if t1 == t0 else (t - t0) / (t1 - t0)
            return tuple(int(a + (b - a) * k) for a, b in zip(c0, c1))
    return STOPS[-1][1]


def verdict_word(score, L):
    """Parola della scala di tassonomia.md: 1-2 innocuo, 3-4 lieve, 5-6 fastidioso,
    7-8 imbarazzante, 9 insostenibile, 10 leggendario."""
    words = L["words"]
    if score <= 2:
        return words[0]
    if score <= 4:
        return words[1]
    if score <= 6:
        return words[2]
    if score <= 8:
        return words[3]
    if score < 10:
        return words[4]
    return words[5]


def layout_rows(pills, measure, maxw, gap):
    """Spezza le pillole in righe (max 3) dato un misuratore di larghezza."""
    rows, row, used = [], [], 0
    for p in pills:
        wpx = measure(p)
        if used + wpx > maxw and row:
            rows.append(row)
            row, used = [], 0
        row.append((p, wpx))
        used += wpx + gap
    if row:
        rows.append(row)
    return rows[:3]


def fit_lines(lines, n):
    """Tiene al massimo n righe, con puntini sull'ultima se si taglia."""
    if len(lines) <= n:
        return lines
    kept = lines[:n]
    kept[-1] = kept[-1].rstrip(".,;: ") + "…"
    return kept


CY, R = 470, 270          # centro e raggio del quadrante
FOOTER_Y = H - 34


def load(path):
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    d["score"] = float(d.get("score", 5))
    d["score"] = max(1.0, min(10.0, d["score"]))
    d.setdefault("register", "credibile")
    d.setdefault("modules", [])
    d["modules"] = d["modules"][:8]
    d.setdefault("verdict", "")
    d.setdefault("quote", "")
    d.setdefault("footer", "github.com/matteobaccan/LinkedInCringe")
    lang = str(d.get("lang", "it")).lower()[:2]
    base = LANGS.get(lang, LANGS["en"])
    L = {"title": base["title"], "register": dict(base["register"]), "words": list(base["words"])}
    for k, v in (d.get("labels") or {}).items():
        if k in L and isinstance(v, type(L[k])):
            if isinstance(v, dict):
                L[k].update(v)
            else:
                L[k] = v
    d["_L"] = L
    return d


# ----------------------------------------------------------------------------
# SVG
# ----------------------------------------------------------------------------

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def polar(cx, cy, r, deg):
    rad = math.radians(deg)
    return cx + r * math.cos(rad), cy + r * math.sin(rad)


def svg(d):
    cx, cy = W / 2, CY
    L = d["_L"]
    score = d["score"]
    frac = (score - 1) / 9.0
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" font-family="Segoe UI, Helvetica, Arial, sans-serif">',
             f'<rect width="{W}" height="{H}" fill="rgb{BG}"/>',
             f'<text x="{W/2}" y="118" text-anchor="middle" font-size="64" font-weight="800" '
             f'letter-spacing="6" fill="rgb{INK}">{esc(L["title"])}</text>',
             f'<text x="{W/2}" y="162" text-anchor="middle" font-size="26" fill="rgb{MUTED}">'
             f'{esc(L["register"].get(d["register"], d["register"]))}</text>']
    # gauge: 60 segments from 180deg to 360deg
    n = 60
    for i in range(n):
        a0 = 180 + 180 * i / n
        a1 = 180 + 180 * (i + 1) / n + 0.6
        col = lerp_color(i / (n - 1))
        x0, y0 = polar(cx, cy, R, a0)
        x1, y1 = polar(cx, cy, R, a1)
        parts.append(f'<path d="M{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f}" '
                     f'stroke="rgb{col}" stroke-width="58" fill="none"/>')
    for k in range(1, 11):
        a = 180 + 180 * (k - 1) / 9
        x, y = polar(cx, cy, R - 62, a)
        parts.append(f'<text x="{x:.1f}" y="{y+10:.1f}" text-anchor="middle" font-size="28" '
                     f'font-weight="700" fill="rgb{MUTED}">{k}</text>')
    # needle
    a = 180 + 180 * frac
    nx, ny = polar(cx, cy, R - 20, a)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="rgb{INK}" '
                 f'stroke-width="10" stroke-linecap="round"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="rgb{INK}"/>')
    # score
    col = lerp_color(frac)
    s = f"{score:g}"
    parts.append(f'<text x="{W/2}" y="{cy+120}" text-anchor="middle" font-size="150" '
                 f'font-weight="900" fill="rgb{col}">{s}<tspan font-size="56" '
                 f'fill="rgb{MUTED}">/10</tspan></text>')
    parts.append(f'<text x="{W/2}" y="{cy+170}" text-anchor="middle" font-size="34" '
                 f'font-weight="700" letter-spacing="3" fill="rgb{col}">'
                 f'{verdict_word(score, L).upper()}</text>')
    # pillole, verdetto e citazione: layout dal basso
    pills = [f'{m["code"]} {m["name"]}' for m in d["modules"]]
    rows = layout_rows(pills, lambda p: 22 * len(p) * 0.62 + 40, W - 120, 14)
    nq_max = 1 if len(rows) >= 3 else 2
    qlines = fit_lines(wrap("“" + d["quote"] + "”", 64), nq_max) if d["quote"] else []
    vlines = fit_lines(wrap(d["verdict"], 46), 2)
    block_h = len(vlines) * 42 + (16 + len(qlines) * 30 if qlines else 0)
    pills_end = cy + 240 + len(rows) * 58
    space = (FOOTER_Y - 12) - pills_end
    verdict_top = pills_end + max(0, (space - block_h) / 2)
    quote_top = verdict_top + len(vlines) * 42 + 16
    y = cy + 240
    for row in rows:
        total = sum(w for _, w in row) + 14 * (len(row) - 1)
        x = (W - total) / 2
        for p, wpx in row:
            parts.append(f'<rect x="{x:.1f}" y="{y}" rx="24" ry="24" width="{wpx:.1f}" '
                         f'height="48" fill="rgb{CARD}" stroke="rgb{MUTED}" stroke-width="2"/>')
            parts.append(f'<text x="{x+wpx/2:.1f}" y="{y+32}" text-anchor="middle" '
                         f'font-size="22" font-weight="600" fill="rgb{INK}">{esc(p)}</text>')
            x += wpx + 14
        y += 58
    y = verdict_top + 34
    for line in vlines:
        parts.append(f'<text x="{W/2}" y="{y}" text-anchor="middle" font-size="34" '
                     f'font-weight="700" fill="rgb{INK}">{esc(line)}</text>')
        y += 42
    y = quote_top + 24
    for line in qlines:
        parts.append(f'<text x="{W/2}" y="{y}" text-anchor="middle" font-size="24" '
                     f'font-style="italic" fill="rgb{MUTED}">{esc(line)}</text>')
        y += 30
    parts.append(f'<text x="{W/2}" y="{FOOTER_Y+8}" text-anchor="middle" font-size="20" '
                 f'fill="rgb{MUTED}">{esc(d["footer"])}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


# ----------------------------------------------------------------------------
# PNG (Pillow)
# ----------------------------------------------------------------------------

FONT_CANDIDATES = {
    "bold": ["segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
             "/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
    "regular": ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "/System/Library/Fonts/Supplemental/Arial.ttf"],
    "italic": ["segoeuii.ttf", "ariali.ttf", "DejaVuSans-Oblique.ttf",
               "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
               "/System/Library/Fonts/Supplemental/Arial Italic.ttf"],
}


def font(kind, size):
    from PIL import ImageFont
    for name in FONT_CANDIDATES[kind]:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def wrap_px(draw, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if text_w(draw, cand, f) > maxw and cur:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines


def png(d, out_path):
    from PIL import Image, ImageDraw
    S = 2  # supersampling per bordi lisci
    img = Image.new("RGB", (W * S, H * S), BG)
    dr = ImageDraw.Draw(img)
    cx, cy, RR = W * S / 2, CY * S, R * S
    L = d["_L"]
    score = d["score"]
    frac = (score - 1) / 9.0

    f_title = font("bold", 64 * S)
    f_sub = font("regular", 26 * S)
    f_tick = font("bold", 28 * S)
    f_score = font("bold", 150 * S)
    f_den = font("bold", 56 * S)
    f_word = font("bold", 34 * S)
    f_pill = font("bold", 22 * S)
    f_verd = font("bold", 34 * S)
    f_quote = font("italic", 24 * S)
    f_foot = font("regular", 20 * S)

    def ctext(y, s, f, fill):
        w = text_w(dr, s, f)
        dr.text(((W * S - w) / 2, y), s, font=f, fill=fill)

    ctext(70 * S, " ".join(L["title"]), f_title, INK)
    ctext(140 * S, L["register"].get(d["register"], d["register"]), f_sub, MUTED)

    # gauge
    n = 90
    box = [cx - RR, cy - RR, cx + RR, cy + RR]
    for i in range(n):
        a0 = 180 + 180 * i / n
        a1 = 180 + 180 * (i + 1) / n + 0.8
        dr.arc(box, a0, a1, fill=lerp_color(i / (n - 1)), width=58 * S)
    for k in range(1, 11):
        a = 180 + 180 * (k - 1) / 9
        x, y = polar(cx, cy, RR - 62 * S, a)
        s = str(k)
        w = text_w(dr, s, f_tick)
        dr.text((x - w / 2, y - 16 * S), s, font=f_tick, fill=MUTED)
    a = 180 + 180 * frac
    nx, ny = polar(cx, cy, RR - 20 * S, a)
    dr.line([(cx, cy), (nx, ny)], fill=INK, width=10 * S)
    dr.ellipse([cx - 22 * S, cy - 22 * S, cx + 22 * S, cy + 22 * S], fill=INK)

    col = lerp_color(frac)
    s = f"{score:g}"
    den = "/10"
    w1, w2 = text_w(dr, s, f_score), text_w(dr, den, f_den)
    x0 = (W * S - w1 - w2) / 2
    dr.text((x0, cy + 10 * S), s, font=f_score, fill=col)
    dr.text((x0 + w1, cy + 88 * S), den, font=f_den, fill=MUTED)
    ctext(cy + 185 * S, "  ".join(verdict_word(score, L).upper()), f_word, col)

    # pillole, verdetto e citazione: layout dal basso
    pills = [f'{m["code"]}  {m["name"]}' for m in d["modules"]]
    rows = layout_rows(pills, lambda p: text_w(dr, p, f_pill) + 40 * S, (W - 120) * S, 14 * S)
    nq_max = 1 if len(rows) >= 3 else 2
    qlines = (fit_lines(wrap_px(dr, "“" + d["quote"] + "”", f_quote, (W - 160) * S), nq_max)
              if d["quote"] else [])
    vlines = fit_lines(wrap_px(dr, d["verdict"], f_verd, (W - 140) * S), 2)
    block_h = (len(vlines) * 42 + (16 + len(qlines) * 30 if qlines else 0)) * S
    pills_end = cy + 240 * S + len(rows) * 58 * S
    space = (FOOTER_Y - 12) * S - pills_end
    verdict_top = pills_end + max(0, (space - block_h) / 2)
    quote_top = verdict_top + (len(vlines) * 42 + 16) * S
    y = cy + 240 * S
    for row in rows:
        total = sum(w for _, w in row) + 14 * S * (len(row) - 1)
        x = (W * S - total) / 2
        for p, wpx in row:
            dr.rounded_rectangle([x, y, x + wpx, y + 48 * S], radius=24 * S,
                                 fill=CARD, outline=MUTED, width=2 * S)
            tw = text_w(dr, p, f_pill)
            dr.text((x + (wpx - tw) / 2, y + 10 * S), p, font=f_pill, fill=INK)
            x += wpx + 14 * S
        y += 58 * S
    y = verdict_top
    for line in vlines:
        ctext(y, line, f_verd, INK)
        y += 42 * S
    y = quote_top
    for line in qlines:
        ctext(y, line, f_quote, MUTED)
        y += 30 * S
    ctext((FOOTER_Y - 8) * S, d["footer"], f_foot, MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    img.save(out_path, "PNG", optimize=True)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    d = load(sys.argv[1])
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    svg_path = os.path.join(out, "cringiometro.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg(d))
    print("svg:", svg_path)
    try:
        import PIL  # noqa: F401
    except ImportError:
        print("png: Pillow non installato (pip install pillow); consegnato solo l'SVG")
        return
    png_path = os.path.join(out, "cringiometro.png")
    png(d, png_path)
    print("png:", png_path)


if __name__ == "__main__":
    main()
