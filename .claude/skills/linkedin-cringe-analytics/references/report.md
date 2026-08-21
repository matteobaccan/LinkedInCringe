# Struttura del report

File: `analisi/YYYY-MM-DD-<slug>/report.md` nella cartella del progetto.
Lo slug viene dal tema del post ("sedia", "pasticceria"), non dall'URL.

## Regole di scrittura

- **Anonimizzazione totale.** Mai nomi, cognomi o aziende dei commentatori.
  Al loro posto la categoria di profilo: "un recruiter", "un dev", "una
  pagina satirica", "un guru del marketing". L'autore del post è l'unico
  nominabile (è l'utente).
- **Estratti brevi.** Le citazioni dai commenti restano sotto le 15-20 parole,
  tra virgolette, senza attribuzione. Se un commento è riconoscibilissimo
  anche senza nome (pagine famose, testi molto caratteristici), parafrasa
  invece di citare.
- **Copertura dichiarata** in testa: commenti letti vs contatore LinkedIn,
  con la spiegazione della differenza (cancellati/filtrati).
- **Percentuali sui classificabili**, con i non classificabili mostrati a
  parte. Niente percentuali con denominatore nascosto.
- Numeri assoluti accanto a ogni percentuale: "45 su 125 (36%)".
- Il tono del report può essere divertito (il materiale lo è) ma i dati
  devono essere rigorosi: chi legge deve poter rifare i conti.

## Sezioni, nell'ordine

1. **Testata**: URL post, data analisi, impressioni (se visibili), contatore
   commenti vs letti, quante risposte dell'autore escluse, totale analizzato.
2. **Ci hanno creduto?** Tabella dei 4 esiti con conteggi e percentuali, due
   righe di lettura del dato. Includi l'avvertenza sul bias di
   auto-selezione: commenta chi ha voglia di commentare, i creduloni silenti
   non si vedono, quindi la percentuale di creduti è una stima per difetto.
3. **Top 10 per gradimento**: tabella con reazioni, categoria anonima
   dell'autore, esito, estratto. Pari merito dichiarati, tie-break sul numero
   di risposte generate. Due righe su cosa premia il pubblico.
4. **Fenomeni ricorrenti**: citazioni e tormentoni (con conteggio), refusi o
   trappole del post notati dai lettori, thread degni di nota.
5. **Toni**: tabella tono -> quota con un esempio-tipo ciascuno.
6. **Categoria x esito**: chi ci casca e chi no, per tipo di profilo.
7. **Cringe-metro**: podio dei 2-3 commenti in buona fede più cringe con
   livello e moduli riconosciuti; menzione d'onore alle parodie consapevoli.
8. **Note di copertura**: quando è stata fatta la raccolta, post ancora
   attivo o no, limiti noti.
9. Riga finale: generato dalla skill, commentatori anonimizzati per policy.

## Consegna in chat

Apri con i 3-4 numeri che l'utente vuole sapere subito (percentuale creduti
in testa, primo posto della top ten, il fenomeno ricorrente più curioso),
poi invia il file con SendUserFile. Non incollare tutto il report in chat.

## Dashboard HTML (opzionale, solo su richiesta)

`dashboard.html` nella stessa cartella: autocontenuta (CSS/JS inline, niente
CDN, niente richieste esterne), tema chiaro/scuro, grafici semplici (barre
CSS bastano). Stessi dati e stessa anonimizzazione del markdown: la dashboard
è una vista, non una fonte.
