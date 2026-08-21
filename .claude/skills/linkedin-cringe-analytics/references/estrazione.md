# Estrazione dei commenti da LinkedIn

Playbook collaudato (agosto 2026) sulla nuova UI di LinkedIn: classi CSS
offuscate (`dcc5d0b1 _2aa7769b ...`), lista commenti **virtualizzata** (i
commenti fuori schermo vengono rimossi dal DOM) e lazy-load che si innesca
solo con eventi rotella. Non fidarti dei selettori per classe: usa gli
attributi `componentkey`, che sono stabili e parlanti.

## A. Browser automation

### Setup

1. Carica i tool in un solo `ToolSearch`: `tabs_context_mcp`, `navigate`,
   `computer`, `read_page`, `find`, `tabs_create_mcp`, `tabs_close_mcp`,
   `javascript_tool`, `browser_batch`, `list_connected_browsers`,
   `select_browser`.
2. `list_connected_browsers`: se vuoto, il browser non è collegato; guida
   l'utente (estensione installata, login su claude.ai con lo stesso account,
   riavvio completo di Chrome) e nel frattempo offri il fallback manuale.
   Se ci sono browser, chiedi con AskUserQuestion quale usare (elenca tutti
   + l'opzione di conferma broadcast), poi `select_browser`.
3. `tabs_context_mcp {createIfEmpty: true}` e naviga all'URL del post.

### Preparazione pagina

- Chiudi il pannello Messaggistica se aperto (icona freccia in alto a destra
  del pannello): copre la colonna e disturba gli screenshot.
- **Ordinamento**: `find` "selettore ordinamento commenti", clicca il dropdown
  ("Più pertinenti") e scegli **"Più recenti"**: è l'unico ordinamento che
  mostra tutti i commenti ("Più pertinenti" ne nasconde).
- Annota il contatore ufficiale ("N commenti"): serve per dichiarare la
  copertura nel report.

### Raccolta (il cuore del problema)

Concetti chiave, tutti verificati:

- Ogni commento (anche le risposte) vive in un elemento
  `[componentkey^="replaceableComment_urn:li:comment:"]`. L'URN nel
  componentkey è l'**identificatore univoco**: è la chiave di deduplica.
- La lista è virtualizzata: bisogna **raccogliere durante lo scroll** in un
  accumulatore sulla window, non alla fine.
- **Solo la rotella vera innesca il lazy-load**: né `scrollTop` via JS né i
  PageDown/End (il focus non è sullo scroller) caricano i batch successivi,
  e il WheelEvent sintetico funziona solo a tratti (probabilmente finché
  dura la user activation di un input reale recente): non farci affidamento.
  Il ciclo affidabile è: **scroll reale col tool `computer`** (azione
  scroll, `scroll_amount: 10`, coordinate sulla colonna dei commenti) +
  harvest via JS dopo ogni giro.
- **Dopo il cambio di ordinamento la lista si ricarica vuota**: prima di
  iniziare il ciclo aspetta che i primi commenti compaiano nel DOM
  (polla `querySelectorAll(...).length > 0`), altrimenti il ciclo "finisce"
  su una lista vuota.
- I bottoni "… altro" (testo troncato) e "Vedi risposte precedenti" /
  "Mostra altre risposte" vanno cliccati man mano che compaiono: `click()`
  via JS su di loro funziona normalmente. **Attenzione: non sono sempre
  `<button>`**: in alcune varianti della pagina "Vedi risposte precedenti"
  è un `div[role="button"]`. Seleziona sempre `button, [role="button"]`,
  altrimenti le risposte annidate restano chiuse e ne perdi decine.
  A fine raccolta fai una risalita di verifica su tutta la lista: se il
  conteggio letto è sotto il contatore, quasi sempre mancano risposte
  dietro espansori non cliccati.
- `javascript_tool` tronca l'output a ~2.500 caratteri e ha un timeout di
  45 secondi: restituisci **solo contatori**, mai il malloppo. Se un batch
  del browser va in timeout ("did not respond in time"), lo stato sulla
  window sopravvive: riprendi da dove eri con lotti più piccoli.
- Se compare il popup delle reazioni (hover su un pulsante like), cattura la
  rotella: sposta le coordinate di scroll o clicca un punto neutro.

Setup una tantum via `javascript_tool`:

```js
window.__scroller = [...document.querySelectorAll('div, main, section')]
  .filter(el => { const s = getComputedStyle(el);
    return (s.overflowY === 'auto' || s.overflowY === 'scroll')
      && el.scrollHeight > el.clientHeight + 200; })
  .sort((a, b) => b.scrollHeight - a.scrollHeight)[0];
window.__got = window.__got || {};
```

Poi il ciclo, in `browser_batch` da 2-3 giri per chiamata (giri più lunghi
rischiano il timeout): ogni giro è `computer.scroll` (down, 10 tick, sulla
colonna commenti) + `wait` 2-3s + questo harvest via JS:

```js
const got = window.__got;
const expand = () => [...document.querySelectorAll('button, [role="button"]')].forEach(b => {
  const t = (b.innerText || '').trim();
  if ((/^…\s*altro$/i.test(t) ||
       /vedi risposte precedenti|vedi altre risposte|mostra altre risposte/i.test(t))
      && b.offsetParent !== null) b.click(); });
expand();
document.querySelectorAll('[componentkey^="replaceableComment_urn:li:comment:"]')
  .forEach(el => {
    const u = el.getAttribute('componentkey').replace('replaceableComment_','');
    const t = el.innerText;
    if (!got[u] || t.length > got[u].length) got[u] = t; });
({c: Object.keys(got).length,
  atBottom: window.__scroller.scrollTop + window.__scroller.clientHeight
            >= window.__scroller.scrollHeight - 100});
```

Ripeti finché il conteggio resta fermo per 2-3 chiamate consecutive con
`atBottom` vero, poi fai la **verifica finale**: nessun bottone di
espansione residuo (`expand` non trova nulla) e conteggio stabile.
Ogni scroll reale restituisce uno screenshot: è il costo del trigger
affidabile, non aggiungere screenshot espliciti.

Se la raccolta si ferma molto sotto il contatore ufficiale, non insistere
all'infinito: 10-25% di scarto è normale (commenti cancellati o filtrati);
dichiara la copertura nel report.

### Export dei dati

L'output del tool JS è troncato, quindi il malloppo passa dagli appunti:

1. Clicca un punto neutro della pagina (serve il focus del documento, senza
   focus `clipboard.writeText` fallisce con NotAllowedError).
2. `await navigator.clipboard.writeText(JSON.stringify(window.__got))`
3. Leggi gli appunti dal sistema e salva **in scratchpad**:
   - Windows: `Get-Clipboard -Raw | Set-Content -Encoding UTF8 <scratchpad>\commenti-raw.json`
   - macOS: `pbpaste > commenti-raw.json` · Linux: `xclip -o -selection clipboard`
4. Chiudi il tab che hai aperto (`tabs_close_mcp`).

Converti poi il JSON in un file di testo leggibile (un blocco per commento,
separatore con progressivo e URN) e leggilo con Read: 150 commenti sono
~60KB, gestibili in una-due letture.

## B. Fallback manuale

Chiedi all'utente di:

1. aprire il post e mettere i commenti su "Più recenti";
2. cliccare tutti i "Carica altri commenti" / "Vedi risposte precedenti" /
   "…altro" finché non ne restano;
3. selezionare tutto (Ctrl+A), copiare e incollare in chat, **oppure**
   salvare la pagina (Ctrl+S, "solo HTML") e passare il percorso.

Dal testo incollato i blocchi si riconoscono con le stesse regole di parsing
qui sotto; manca solo l'URN, quindi dedup su (autore, tempo, inizio testo).

## Parsing dei blocchi

Ogni blocco raccolto ha questa forma (righe vuote variabili):

```
Nome Cognome [, Disponibile a lavorare] [Profilo Verificato|Profilo Premium] 2°
Nome Cognome • 2°            <- riga doppia: il nome compare due volte
Headline del profilo         <- fonte della categoria
3h | 1 giorno | (modificato) 1g
[Segui]
TESTO DEL COMMENTO           <- può contenere "… altro" residuo a fine riga
N reazioni | N reazione | 0
N                            <- eco del numero
[M                           <- numero risposte, se presenti]
```

Attenzioni:

- **Risposte dell'autore del post**: il blocco ha la riga "Autore" al posto
  della headline con pallino, e in coda "N impressioni". Vanno tenute fuori
  dalla classificazione.
- Le **pagine** (non persone) hanno "N follower" al posto di headline e grado.
- Un blocco di primo livello può contenere in coda il numero di risposte;
  le risposte sono blocchi a sé con il proprio URN, quindi non sommare due
  volte.
- Il grado ("1°", "2°", "3°+", "Già segui") e i badge non servono all'analisi
  ma aiutano a distinguere le righe di intestazione dal testo.
- Reazioni: prendi il numero dalla riga "N reazioni"; se c'è solo "0 " il
  commento non ha reazioni.
