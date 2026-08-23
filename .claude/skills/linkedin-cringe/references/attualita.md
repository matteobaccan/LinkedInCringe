# Il gancio reale: cringe ispirato ai fatti

Una quota consistente del cringe che LinkedIn produce ogni giorno non parte da un
aneddoto inventato ma da una notizia vera: un rendering urbanistico che fa il giro del
mondo, un dato sui morti per il caldo, l'aumento delle accise, il lancio di un modello
di AI, una finale persa. Il fatto è vero. Quello che lo rende cringe è l'uso: la morale
che ci viene incollata sopra, l'autore che si mette al centro, la cifra sbagliata di
scala.

Questo file spiega come pescare il fatto e come usarlo senza rompere la credibilità.

---

## Da dove arriva il fatto

**Lo dà l'utente.** Una notizia descritta, un dato, un link. Se è un link, leggi la
pagina con `WebFetch` e tira fuori i dettagli esatti: data, cifre, luoghi, nomi di enti.
Il post li userà così come sono.

**L'utente dice solo "ispirati all'attualità".** Allora cerchi tu:

1. `WebSearch` sulle notizie degli **ultimi 7-10 giorni** nel paese della lingua
   target (Italia di default). Cerca per genere, non con una query generica: "accise
   carburanti", "Inps giovani", "caldo record", "rientro a scuola", "Serie A".
2. Se i risultati sono vaghi (succede spesso con le notizie italiane recenti), leggi
   direttamente i feed RSS delle agenzie, che rispondono sempre e sono datati:
   - `https://www.ansa.it/sito/notizie/economia/economia_rss.xml`
   - `https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml`
   - `https://www.ansa.it/sito/notizie/cronaca/cronaca_rss.xml`
   - `https://www.ansa.it/sito/notizie/sport/sport_rss.xml`
   Per altre lingue, l'agenzia nazionale equivalente (Reuters, AFP, dpa, EFE).
3. Scegli **3-4 ganci** e proponili con `AskUserQuestion` (`header: "Gancio"`), uno
   per riga: il fatto in dieci parole, la data, e in mezza riga *perché* è cringe-abile
   (quale dei cinque usi qui sotto attiva). L'utente sceglie o scrive il suo con
   "Other". Questa domanda sostituisce la richiesta del tema: non è una quinta domanda
   in più.

In registro credibile scarta già in fase di proposta i ganci con vittime o lutti
(vedi *Paletti*). Se l'utente ne ha dato uno lui, diglielo in una riga e proponi
l'attenuazione.

---

## I cinque usi del fatto reale

Tutti si combinano con i moduli del catalogo: il gancio è il tema, i moduli
restano la struttura.

### 1. La notizia come parabola
C01 su scala pubblica. Il fatto viene raccontato con precisione giornalistica per
tre righe, poi: "e ho pensato che è esattamente quello che succede nelle aziende".
**Attacco tipo:** "In questi giorni gira un dato che mi ha colpito."
**Marcatore:** il passaggio dal pubblico al privato avviene in una riga sola, senza
transizione. La notizia parlava di accise, la morale parla di leadership.

### 2. Il dato a sproposito (C35)
Una statistica macroscopica, spesso drammatica, usata per giustificare un problema
domestico o aziendale minuscolo, o il contrario: il proprio micro-caso elevato a
prova di un fenomeno nazionale. Dettagli nel catalogo, modulo C35.

### 3. L'hot take sulla notizia
C07 applicato al fatto del giorno: "Unpopular opinion sulla vicenda X" seguito da
quello che pensano tutti. Variante: "Tutti parlano di X. Nessuno dice la cosa più
importante", e la cosa più importante è un'ovvietà.
**Marcatore:** la presa di posizione coraggiosa coincide col senso comune.

### 4. L'io c'ero / l'avevo detto
C25 e C28 applicati alla cronaca: l'autore si mette dentro la notizia. "Mentre
tutti parlavano di X, io alle 6 ero già…", "Lo scrivevo tre anni fa, nessuno mi
ascoltava", "Ne ho parlato proprio ieri con un cliente". Il fatto pubblico diventa
conferma di una propria qualità.
**Marcatore:** la notizia sparisce dopo l'attacco; il resto del post è su di lui.

### 5. La notizia come sfondo
C09 con la cronaca al posto della vacanza: il fatto non è il tema ma l'ambiente
dell'aneddoto privato. "Stamattina, con le accise a quel prezzo, ho deciso di
andare in ufficio in bici. E lungo la strada…" La notizia dà il sapore di attualità,
il resto è il solito post.

---

## Regole di credibilità

Nel cringe da fatto reale, **il fatto è la parte che regge tutto**. I commentatori
verificano davvero: una cifra sbagliata o una data fuori posto viene smontata in
poche ore, e invece di "che cringe" si legge "è falso", che è peggio.

- **Fatto recente.** Entro 7-10 giorni. Una notizia di un mese fa suona riscaldata,
  e il post vero non la riscalderebbe.
- **Cifre e date esatte**, prese dalla fonte. Il post le cita con la disinvoltura di
  chi le ha lette sul telefono: "19mila", "più 12 per cento", "tre milioni". Niente
  decimali da rapporto, quelli sono C13 e vanno sui numeri inventati dell'autore, non
  sul fatto.
- **Mai il link alla fonte.** Il cringe reale non cita: "ho letto che", "gira un dato",
  "in questi giorni si parla di". Se l'utente vuole il link, va nel disclaimer.
- **Il fatto resta vero, la morale resta sganciata.** La leva del cringe è sempre lo
  scarto (tassonomia): qui lo scarto è fra la precisione del dato e l'arbitrarietà
  della lezione. Non correggere la notizia per farla tornare con la morale.
- **Il fatto si racconta in poche righe.** Chi legge lo conosce già: tre righe al
  massimo, poi il post diventa quello che sarebbe stato comunque.
- **Dettaglio d'epoca.** Il fatto reale dà gratis il "dettaglio concreto e inutile" che
  serve a suonare umani: il giorno della settimana, il luogo della conferenza, il
  nome dell'ente. Usane uno, non tutti.

---

## Generi di fatti e attacchi tipo

| Genere | Esempi di gancio | Attacco tipo |
|---|---|---|
| Economia | accise, tassi, inflazione, bonus, una fusione bancaria | "Mentre i giornali parlano di X, nelle PMI che seguo succede un'altra cosa." |
| Lavoro e welfare | dati Inps, Istat, rapporti su occupazione e giovani | "Un dato uscito ieri mi ha fatto riflettere." |
| Tech e AI | lancio di un modello, un'app che chiude, un blackout | "Ieri X ha annunciato Y. Io ho fatto una cosa semplice: ho chiuso il portatile." |
| Sport | finale, esonero, record | "Non seguo il calcio. Ma quello che è successo ieri sera ha molto da insegnare a chi fa impresa." |
| Meteo e stagioni | caldo record, nubifragio, rientro, Ferragosto | "Sono le 6:10 e ci sono già 29 gradi." |
| Urbanistica e grandi opere | un rendering, un cantiere, un'inaugurazione | "Loro in un pomeriggio disegnano un'isola. Noi…" (C26) |
| Scuola e ricorrenze | primo giorno di scuola, maturità, Giornata mondiale di qualcosa | "Oggi è la Giornata mondiale della X. E io voglio parlare di Y." |
| Costume | un festival, un film, un personaggio televisivo | "Ho visto anch'io X. E non ho potuto fare a meno di pensare al mio team." |

---

## Paletti specifici del gancio reale

Si sommano ai paletti di SKILL.md.

- **Tragedie solo in registro parodico.** Disastri, vittime, crisi umanitarie, guerre,
  incidenti con morti: in registro credibile non si usano, perché un post credibile
  su una tragedia reale è indistinguibile da un post reale su una tragedia reale, e
  se viene pubblicato fa male davvero. In parodico sono leciti: la presa in giro è
  dichiarata e il bersaglio è chi lo fa sul serio. Quando scarti un gancio tragico in
  credibile, dillo in una riga e proponi l'**attenuazione**: il dato aggregato al posto
  dell'evento nominato (il rapporto annuale sul caldo, non l'ondata con le vittime di
  ieri; la statistica sugli infortuni, non l'incidente di stamattina).
- **Persone pubbliche.** Si possono citare per il fatto pubblico che le riguarda
  (ha detto, ha vinto, ha annunciato), con le parole che hanno detto davvero. Mai
  attribuire frasi inventate, mai un C04 con una persona reale, mai un incontro
  privato inventato ("l'ho incrociato in aeroporto e mi ha detto").
- **Aziende ed enti reali.** Solo come soggetto della notizia, mai come autore del
  post o come bersaglio di un giudizio inventato.
- **Il disclaimer distingue vero e finto.** Con gancio reale, la riga finale deve dire
  che il fatto è vero e il resto no, altrimenti la smentita travolge anche il dato:
  "La notizia è vera. La lezione no, e nemmeno il cliente di cui parlo." Se l'utente
  vuole, lì si può mettere il link alla fonte.
