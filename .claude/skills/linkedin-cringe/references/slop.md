# Il registro AI-SLOP

Il quarto valore dell'asse credibilità, accanto a *credibile*, *parodico* e *surreale
deadpan*. È il registro in cui il post non ha un autore: è stato generato, incollato e
pubblicato, e nessuno lo ha riletto.

Non si attiva mai da solo. Vedi *Attivazione* qui sotto, che viene prima di tutto il resto.

---

## Attivazione

**Il generatore non sceglie mai AI-SLOP di sua iniziativa.** Non lo deduce, non lo
propone come ripiego, non lo usa per riempire un parametro mancante.

Si attiva **solo** se l'utente lo nomina, in una di queste forme:

- "AI-SLOP", "modalità slop", "slop", "aislop";
- "fallo sembrare scritto dall'AI", "che trasudi AI", "tutto AI dall'inizio alla fine";
- "sembra contenuto IA scadente" (il nome del tasto di segnalazione di LinkedIn);
- la scelta esplicita della quarta voce nella domanda D2 del menu registri.

**Non sono attivazioni**, e vanno trattate come richieste normali in registro credibile:

- "scrivilo con l'AI", "usa l'AI", "fallo scrivere a Claude": descrivono lo strumento,
  non il registro. Ogni post di questa skill è scritto con l'AI, e il default resta
  suonare umani.
- "fallo più levigato", "scrivilo meglio", "rendilo più professionale".
- la combo D4 "Pacchetto completo", che non seleziona mai questo registro.

Se mancano i parametri, il registro resta **credibile**. Se l'utente chiede un post
generico e la skill sospetta che voglia lo slop, **chiede**, non lo assume.

In consegna, dopo il post, la skill dichiara in una riga che il registro è AI-SLOP e
che è stato richiesto esplicitamente. Serve a rendere la scelta tracciabile quando
l'utente rilegge la conversazione tre giorni dopo.

---

## Che cos'è

| Registro | Il mondo | La voce | Il lettore |
|---|---|---|---|
| Credibile | vero | sincera | ci crede |
| Parodico | vero | complice | ride |
| Surreale deadpan | impossibile | sincera | non sa dove mettersi |
| AI-SLOP | generico | assente | scorre, e poi segnala |

**La definizione in una riga: il post rivendica un'esperienza personale che nessuno ha
avuto.**

Il resto della skill lavora per non sembrare scritta da un modello. Qui si fa l'opposto,
e la sezione *Non deve sembrare scritto da un'AI* di SKILL.md va letta al contrario riga
per riga: quella lista di divieti diventa la lista della spesa.

**Perché è cringe.** Le tre condizioni della tassonomia reggono, spostate:

- *sincerità*: chi pubblica ci crede davvero, perché crede che quel testo sia suo;
- *scarto*: massimo, fra l'intimità rivendicata ("una cosa che ho imparato sulla mia
  pelle") e il fatto che il testo non contiene una sola cosa successa a qualcuno;
- *intenzione nascosta*: non è più vendere fingendo di non vendere, è **firmare fingendo
  di aver scritto**. È l'unico registro in cui l'asimmetria di consapevolezza non riguarda
  il carattere di chi scrive ma la paternità del testo.

**Dato di contesto (agosto 2026).** Rilevazioni indipendenti di giugno 2026 stimano il
41% dei post lunghi su LinkedIn e il 30% dei commenti come scritti da un modello, contro
il 29% su X e il 13% su Reddit. Dall'estate 2026 la piattaforma ha un tasto per segnalarli
("sembra contenuto IA scadente"). Questo registro non inventa un genere: ne riproduce
il più diffuso.

---

## Le otto regole

**1. Il trattino lungo torna, ed è obbligatorio.** È l'unico punto di tutto il repo in
cui si scrive. Almeno due per post, in posizione di incidentale.

**2. Zero dettagli concreti.** Nessun orario, nessun oggetto, nessun nome, nessuna cifra
verificabile, nessun luogo. Dove il registro credibile chiede "le 5:41" e "la sedia di
plastica bianca", qui si scrive "qualche tempo fa" e "un cliente".

**3. Tutti i paragrafi della stessa misura.** Due righe l'uno, riga vuota, avanti. La
broetry di C21 resta, ma perde l'irregolarità: nel post umano i blocchi sono lunghi 1,
poi 4, poi 1. Qui sono sempre 2.

**4. La triade ovunque.** Tre esempi, tre lezioni, tre aggettivi, tre verbi all'infinito
in fila come chiusa di paragrafo. Ascoltare. Adattarsi. Crescere.

**5. "Non è X. È Y." in serie.** Nel registro credibile se ne concede una. Qui almeno tre,
e almeno una in cui X e Y sono la stessa cosa.

**6. Nessuna sbavatura.** Grammatica perfetta, punteggiatura perfetta, nessuna ripetizione,
lessico uniformemente medio-alto. Se viene voglia di ripetere una parola, si cerca il
sinonimo. È l'inverso della regola umana, e va applicato senza pietà.

**7. Il paragrafo finale riassume il post.** Introdotto da "In conclusione", "In definitiva"
o "La verità è che". Non aggiunge niente, e non deve.

**8. Il markdown resta nel testo.** Il modello scrive gli asterischi del grassetto,
LinkedIn non li interpreta, e restano lì. Almeno un `**Titolo:**` o un `**Punto 1:**`
visibile nel post. È il tell più riconoscibile in assoluto e il più rapido a farsi
segnalare.

---

## Il repertorio

Da usare a piene mani, non con parsimonia.

- **Gli attacchi:** "In un mondo sempre più veloce e interconnesso,", "Recentemente mi
  sono trovato a riflettere su", "Riflessione del lunedì:", "Spoiler: non è quello che
  pensi."
- **Le cerniere:** "Ed è proprio qui che entra in gioco", "Ma andiamo con ordine.",
  "Facciamo un passo indietro.", "Inoltre", "Tuttavia", "Pertanto".
- **Le formule da assistente:** "È importante notare che", "Vale la pena sottolineare",
  "Che si tratti di un team di due persone o di una multinazionale, il principio resta
  lo stesso."
- **Gli elenchi:** emoji numerate o spunte verdi in colonna, ogni voce con la stessa
  identica sintassi, ogni voce che comincia con un sostantivo astratto.
- **Le chiuse:** "In conclusione,", "E voi, cosa ne pensate? Fatemelo sapere nei commenti!",
  "Se questo post ti è stato utile, condividilo con la tua rete".
- **Gli hashtag:** sempre gli stessi quattro, sempre capitalizzati in CamelCase.
  #Leadership #Innovazione #Crescita #Mindset
- **L'esperienza senza esperienza:** "un cliente mi ha detto una frase che non
  dimenticherò", senza chi, senza quando, senza dove, e la frase è un proverbio.

---

## Livelli

Il registro vive **da 5 in su**. Sotto il 5 lo slop è soltanto noioso, e la tassonomia
è esplicita: un post noioso non è cringe, scivola via.

| Livello | Come si comporta lo slop |
|---|---|
| 5-6 | levigato e generico, ma ancora plausibile come post scritto male da una persona |
| 7-8 | tutti i tic insieme, il markdown nel testo, la triade a ogni paragrafo. È il punto dolce |
| 9 | si aggiunge la cicatrice del copia-incolla (vedi sotto) |
| 10 | la cicatrice più il segnaposto mai compilato: `[inserisci qui il tuo aneddoto personale]` |

Default consigliato: **8**.

---

## La cicatrice del copia-incolla

La riga che il modello ha scritto per chi lo ha interrogato, e che è finita nel post.
È l'elemento più riconoscibile del registro e il più divertente, ma è anche quello che
rompe l'illusione: da 9 in su è accesa, sotto il 9 è spenta.

- in cima: "Certo! Ecco un post per LinkedIn dal tono professionale e coinvolgente:"
- in mezzo: `[Inserisci qui un aneddoto personale]`, `**Opzione 2:**`
- in fondo: "Fammi sapere se vuoi che lo adatti a un tono più informale!"

Una sola per post. Non viene mai commentata dalla voce, esattamente come l'impossibile
nel registro surreale.

---

## Cosa cambia nei moduli

- **`C12` sapore-AI** è sempre incluso e non conta nel totale: è il registro fatto modulo,
  come `C37` per il surreale.
- **`C13` numeri finti-precisi si capovolge.** Niente 1.247 profili e +37%: lo slop
  arrotonda. "Il 90% dei leader", "tre volte su quattro", "la maggior parte delle persone".
  La precisione sospetta è un'impronta umana, e qui non ce ne sono.
- **`C32` errore piantato: non si pianta.** In questo registro l'errore arriva da solo,
  ed è sempre lo stesso: l'appiattimento del dato reale. Vedi *Il gancio reale* qui sotto.
- **`C19`, `C20`, `C04`** perdono il corpo. L'artigiano non ha bottega, il mentore non ha
  una prima volta, il dialogo non ha una stanza. Restano le battute, che diventano proverbi.
- **`C33` nervo scoperto è sconsigliato.** Ha bisogno di una voce che si esponga e non
  risponda alle correzioni; lo slop smussa tutto e non si espone mai. Se serve un post
  che faccia arrabbiare i professionisti del settore, il registro giusto è credibile.
- **`C37` onirico deadpan è incompatibile.** Il deadpan è tutto nella voce sincera che
  non si accorge di niente; qui la voce non c'è. Se l'utente chiede tutti e due, va
  detto e va scelto.
- **`C30` lead-gen** sopravvive benissimo e si standardizza: "P.S. Se vuoi approfondire,
  ti lascio il link nel primo commento."

---

## Il gancio reale in AI-SLOP

Il fatto resta vero: la regola di `attualita.md` non si tocca, cifre e date restano
quelle della fonte. Ma **lo slop le arrotonda**, ed è lì che il registro si vede.

Dove il registro credibile scrive "850mila", AI-SLOP scrive "quasi un milione". Dove
credibile scrive "dal 7 aprile", slop scrive "di recente". Nessuna falsità pubblicabile,
nessun numero inventato: solo la perdita di precisione, che è la firma del genere.

Il fatto viene inoltre nominato una volta sola in apertura e poi abbandonato, perché
il testo non ne ha bisogno: avrebbe funzionato uguale con qualunque altra notizia.

---

## L'immagine

Qui la regola generale si ribalta, e va dichiarato all'utente.

Il post in AI-SLOP arriva con la sua immagine generata, e l'immagine **deve** avere i
difetti che negli altri registri sono vietati: testo impresso, insegne storpiate, mani
sbagliate, luce da render, sorrisi da stock. Il divieto di testo leggibile in scena non
si applica: qui il cartello mezzo sbagliato è il punto.

Nel prompt si chiede l'opposto del solito: "professional stock photography, clean
corporate lighting, smiling business people, 8k, highly detailed". La foto patinata,
che altrove tradisce, qui è il costume di scena.

---

## Il disclaimer

Vale la regola generale, con un'inclinazione sua: la riga finale è l'unica del post che
una persona ha scritto, e può dirlo senza spiegare niente.

- "Questo post è finto, ed è stato scritto apposta perché sembri scritto da una macchina.
  Questa riga no."
- "Se stavi cercando il tasto «sembra contenuto IA scadente», hai ragione tu."

Con un gancio reale resta l'obbligo di separare il vero dal finto, e va aggiunto che il
dato è stato arrotondato apposta.

---

## Diagnosi: quando è venuto male

| Sintomo | Cosa è successo | Rimedio |
|---|---|---|
| Si legge volentieri | è rimasto un post umano | togli i dettagli concreti, pareggia i paragrafi |
| Fa ridere | è scivolato in parodico | lo slop non fa battute, toglile |
| Sembra solo scritto male | manca la levigatezza | correggi ogni sbavatura, alza il lessico |
| Ha una voce riconoscibile | non è slop | togli le opinioni, lascia le constatazioni |
| Il lettore ricorda un dettaglio | ce n'era uno | non deve restare niente |

---

## Paletti

Restano tutti quelli di SKILL.md. Due valgono in più:

- **Il registro non abbassa la soglia dei contenuti.** Nessuna persona reale, nessuna
  azienda reale, nessun lutto: che il testo sembri generato non lo rende meno pubblicabile
  né meno dannoso.
- **Il disclaimer non si toglie.** Negli altri registri l'utente decide; qui la riga
  finale è l'unica cosa che distingue un esercizio da un contributo al 41%. Se l'utente
  la vuole togliere, si dice una volta e poi si fa, come sempre.
