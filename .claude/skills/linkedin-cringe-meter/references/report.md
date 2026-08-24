# Struttura del report

File: `analisi/YYYY-MM-DD-<slug>/cringiometro.md`. Lo slug viene dal tema del post
(es. `asparagi`, `macchinetta`), mai dal nome dell'autore. Nella stessa cartella
vanno `cringiometro.png`, `cringiometro.svg` e `cringiometro.json` (i dati passati
allo script, utili per rigenerare l'immagine a mano).

Se nella cartella c'è già un `report.md` della skill analytics (stesso post,
analizzato dopo la pubblicazione), i due file convivono: il Cringiometro misura il
post, analytics misura i commenti.

---

## Regole

- **Anonimato totale dell'autore.** Mai nome, cognome, azienda, headline, ruolo,
  foto, link al profilo. L'URL del post non va nel report (basta nel JSON di
  scratchpad, che non si committa): chi legge il report legge una valutazione di un
  testo, non di una persona. Si può dire "un post del 23 agosto 2026".
- **Citazioni brevi.** Massimo due righe per citazione, solo quanto serve a provare
  il modulo. Il post non si riporta mai per intero.
- **Il soggetto è il post.** "Il post usa", "la morale arriva", "il P.S. vende".
  Mai "l'autore è".
- **Lingua.** Il report è nella lingua dell'utente; l'immagine nella lingua del
  post (campo `lang` del JSON, nomi dei moduli e verdetto tradotti). Se il post è
  in inglese, il verdetto nel report compare in entrambe le lingue: quello italiano
  nel testo, quello inglese citato sotto, perché è quello che finisce nell'immagine.
- **Markdown piatto**, niente HTML. Emoji solo nelle intestazioni di sezione, come
  sotto. Niente trattini lunghi, come in tutto il repo.

---

## Template

```markdown
# Cringiometro: <slug>

Post valutato il YYYY-MM-DD · testo di N parole · immagine allegata: sì/no

## 🎯 Livello: X/10 (parola)

Due righe di motivazione: lo scarto e il peso dei moduli.

**Registro:** credibile / parodico / surreale deadpan / cringe dichiarato (una riga sul perché)
**Lo scarto:** [evento] → [morale]

## 🧩 Moduli rilevati

| # | Modulo | Prova |
|---|---|---|
| 1 | C01 Parabola forzata | "…citazione breve…" |
| 2 | C13 Numeri finti-precisi | "…" |
| … | | |

Altri tic minori: C31, C23 (una riga).

**Gancio reale:** no / sì, [uso] su [fatto], citato giusto / sbagliato (solo se c'è).

## 🤖 Sapore-AI: bassa / media / alta

Gli indizi, in una riga o due. Osservazione sul testo, non accusa.

## 💰 Lead-gen: no / sì

Dove si nasconde, in una riga.

## 🗣️ Verdetto

> La frase secca (quella dell'immagine).

## 📈 Per salire a X+1

- C.. nome: dove andrebbe, in una riga
- C.. nome: idem

## 🖼️ Immagine

`cringiometro.png` (1080×1080). Nessun dato dell'autore. Pronta come risposta.
```

---

## Consegna in chat

Nell'ordine: livello e parola, i moduli in una riga (solo i codici con il nome
corto), il verdetto, poi il file PNG via `SendUserFile` e il percorso del report.
Una riga, la prima volta, per ricordare che rispondere con l'immagine sotto al
post di un estraneo è una scelta sua e che l'immagine non porta nomi.
