<img src="assets/banner.svg" width="560" alt="LINKEDIN CRINGE — Un post. Una morale. Nessun rapporto tra le due. Sei d'accordo? 👇 #mindset #leadership #grateful #hustle">

🇬🇧 [English version](README.en.md)

# LinkedIn Cringe

Tre skill per Claude Code, che si chiudono a cerchio:

- **`linkedin-cringe`** genera post LinkedIn cringe in italiano, quelli veri,
  quelli che vengono screenshottati e girati nelle chat;
- **`linkedin-cringe-analytics`** scarica i commenti del post una volta
  pubblicato e misura cosa è successo: quanti ci hanno creduto, quanti hanno
  colto lo scherzo, la top ten per gradimento, i toni, il cringe involontario
  dei commenti stessi;
- **`linkedin-cringe-meter`**, il *Cringiometro*, misura il post di qualcun
  altro con lo stesso metro: voto da 1 a 10, ganci presi, verdetto, e
  un'immagine anonima pronta da lasciare nei commenti.

Quello che le altre due scoprono finisce nei moduli della prima: il catalogo
si migliora coi dati veri, non con le opinioni.

La skill di generazione non produce "post brutti". Produce **imbarazzo
vicario**: post in cui chi scrive ci crede davvero, rivendica una profondità
che il testo non ha, e sta vendendo qualcosa fingendo di non vendere nulla.

## La skill di generazione

### Cosa chiede

Quando la invochi senza parametri, la skill ti fa quattro domande:

| Domanda | Opzioni |
|---|---|
| **Livello di cringe** | 4 lieve · 7 imbarazzante · 9 insostenibile · 10 leggendario |
| **Registro** | credibile (deve passare per vero) · parodico (satira dichiarata) · surreale deadpan (il mondo è impossibile, la voce non se ne accorge) |
| **Voce** | fuffaguru · founder/CEO · HR/recruiter · boomer con consiglio |
| **Moduli cringe** | scelta multipla da un catalogo di 37 moduli (`C01`…`C37`) |

Se invece scrivi già tutto nella richiesta (`post livello 9, credibile, tema
smart working, moduli C19 e C02`), salta le domande e genera direttamente.

### Ispirato a fatti reali

Una buona fetta del cringe vero non parte da un aneddoto inventato ma da una
notizia: il rendering che fa il giro del mondo, il dato Inps, le accise, la
finale persa. Il fatto è vero; cringe è l'uso che se ne fa. La skill lo
riproduce in due modi:

- **dai tu il fatto** (`ispirati alla notizia X`, un dato, un link) e la skill
  lo usa con cifre e date esatte;
- **dici solo "ispirati all'attualità"** e la skill cerca le notizie degli
  ultimi giorni, te ne propone 3-4 come ganci e scrive sul prescelto.

Le regole stanno in
[`references/attualita.md`](.claude/skills/linkedin-cringe/references/attualita.md):
il fatto resta vero, esatto e mai linkato nel corpo, la morale resta sganciata,
e la riga finale separa il vero dal finto ("La notizia è vera. La lezione no.").
**Le notizie tragiche si usano solo in registro parodico**: in credibile
vengono scartate o attenuate al dato aggregato, e il registro surreale non fa
eccezione (lì la voce è sincera, quindi è peggio, non meglio).

### Il registro surreale

Il terzo valore sull'asse della credibilità, e il più difficile da tenere in
piedi: **il mondo raccontato è impossibile e la voce non se ne accorge.** Non è
credibile (nessuno crede a un cervo che esce dal ronzio dei lampioni) e non è
parodia (non c'è nessuna battuta, la quarta parete resta chiusa). Il tono resta
quello del post motivazionale del lunedì mattina mentre i fatti smettono di
funzionare.

Funziona perché le tre condizioni del cringe restano tutte: la sincerità è
massima, lo scarto è enorme (la morale aziendale incollata su un evento che non
può essere successo) e il P.S. che vende il percorso arriva puntuale anche
dentro il sogno.

Si attiva chiedendolo ("alla David Lynch", "surreale", "onirico", "tipo
sogno"), vive dal livello 7 in su e ha il punto dolce al 9. Le regole stanno in
[`references/surreale.md`](.claude/skills/linkedin-cringe/references/surreale.md):
una sola fisica del sogno per post, niente spiegazioni, il concreto che regge
l'impossibile, il fatto di cronaca come unico punto fermo, e la regola
controintuitiva sull'immagine, **l'impossibile sta nel soggetto, lo stile resta
noioso** (mai chiedere al generatore "dreamlike" o "cinematic": la foto che
sembra arte tradisce quanto la foto patinata). Il file contiene anche le frasi
che uccidono il registro e una tabella di diagnosi per quando viene male.

### Il catalogo dei moduli

37 moduli codificati in
[`references/moduli.md`](.claude/skills/linkedin-cringe/references/moduli.md),
divisi in narrativi, retorici e formali. Alcuni esempi:

- `C01` parabola forzata, il caffè che diventa una lezione sul senso del lavoro
- `C02` colpo di scena moralista, "l'ho scartato perché non ha salutato la receptionist"
- `C03` vulnerabilità strumentale, il fallimento come antefatto della vanteria
- `C06` hustle tossico, sveglia alle 5:17, ferie come debolezza
- `C13` numeri finti-precisi, "il 78% dei manager che incontro"
- `C15` sfruttamento venduto come opportunità, "ti pago in esperienza"
- `C19` l'artigiano-parabola, il panettiere che dice una frase millenaria
- `C21` broetry, una frase per riga, il white space che simula gravitas
- `C30` lead-gen mascherata, il P.S. che smentisce tutto il post
- `C32` l'errore piantato, l'impossibilità logica lasciata lì come esca
- `C33` il nervo scoperto, l'errore di prassi che i professionisti correggeranno
- `C34` il diario orario, "Ore 8:23, solo una controllatina alle email"
- `C35` statistica a sproposito, i morti per il caldo per convincere i genitori
  a mettere il condizionatore in soggiorno
- `C36` il rifiuto come flex, "sono io che scelgo i clienti"
- `C37` onirico deadpan, il cervo che invece di caricarti ti dà un feedback

`C32` e `C33` sono nati dall'analisi sul campo: il primo dall'osservazione che
la sedia rimessa a posto *prima di alzarsi* ha generato thread interi, il
secondo dal fatto che il 13% dei commenti a un post virale erano correzioni
serissime sulla RAL. Chi ti corregge ti ha creduto. `C34`-`C36` vengono
dall'osservazione del cringe che LinkedIn produce ogni giorno, e che qualcuno
ha la pazienza di raccogliere (vedi i ringraziamenti in fondo). `C37` è nato
invece usando la skill: da un post surreale su un fatto di cronaca è stato
ricavato il registro descritto in `surreale.md`.

### Lingue

Il default è l'italiano, ma il cringe non è un fenomeno italiano: cambia il
rivestimento, non il meccanismo. Chiedendo un post in un'altra lingua, la skill
**rigenera dai moduli** invece di tradurre (un post tradotto suona tradotto, e
smette di essere credibile).

Restano invariati la definizione, la scala e la struttura; vengono sostituiti
lo strato di gergo contaminato (in italiano l'itanglese, in inglese il buzzword
corporate, in tedesco il Denglisch…), gli hashtag, e i quattro moduli a radice
culturale (`C14` `C15` `C19` `C26`), che vanno riscritti sul mercato del lavoro
locale. Dettagli in
[`references/lessico.md`](.claude/skills/linkedin-cringe/references/lessico.md).

### Riga finale

Ogni post generato finisce, dopo gli hashtag, con una riga che rivela lo
scherzo. La formulazione cambia ogni volta e, quando possibile, riprende un
dettaglio del post. È l'unico punto in cui la voce ammicca: il corpo sopra
resta serio, altrimenti il cringe si spegne.

Dato di collaudo: il muro di hashtag seppellisce il disclaimer davvero. Su un
post virale, un commentatore su tre ci ha creduto nonostante la riga finale.
Con un gancio reale la riga separa il vero dal finto ("La notizia è vera. La
lezione no."), così chi scopre lo scherzo non butta via anche il dato.

### Niente sapore-AI

Un post che profuma di modello linguistico non è credibile come cringe umano.
La skill vieta in output il trattino lungo, i connettivi levigati, le triadi
perfette, i paragrafi tutti della stessa misura e il finale riassuntivo; e
impone almeno un dettaglio concreto inutile, un ritmo irregolare e una piccola
sbavatura.

### Come si tara il livello

La leva non sono le emoji. È la **distanza fra l'evento raccontato e la morale
che ci si costruisce sopra**: più l'evento è minuscolo e la morale è cosmica,
più alto il cringe.

### Esempi

Un livello 4 credibile, quello che passa inosservato nel feed:

```
Tre anni fa non sapevo nemmeno cosa fosse un CRM.

Ricordo la prima call con un cliente importante: mani sudate, slide sbagliate,
e una domanda a cui non ho saputo rispondere.

Sono uscito da quella riunione convinto di aver chiuso la mia carriera prima
ancora di iniziarla.

Oggi coordino un team di 6 persone.

Non è cambiato il talento. È cambiata la costanza.

Grazie al mio responsabile di allora, che quel giorno non mi ha detto niente.
Mi ha solo rimesso in agenda la stessa call, la settimana dopo.

#crescitapersonale #leadership #grateful

Sei arrivato in fondo e hai alzato gli occhi al cielo? È una parodia.
```

Fastidioso ma sobrio: humblebrag, gratitudine ostentata, morale proporzionata.
Gli altri livelli (7, 9, 10, una versione parodica, una con gancio reale e una
surreale) sono in
[`references/esempi.md`](.claude/skills/linkedin-cringe/references/esempi.md).

> **Nota.** Nessun esempio in questo repository è la trascrizione o il
> rimaneggiamento di un post reale. Sono tutti scritti da zero applicando la
> tassonomia e i moduli. Nomi, aziende, numeri e aneddoti sono inventati.

### Occhio alle immagini

Collaudato sul campo: il testo regge, **la foto generata con l'AI tradisce**.
Cartelli con scritte storpiate, cappellino ad agosto, luce da giugno alle 5:41
del mattino: i commentatori fanno zoom e smontano tutto in poche ore. La skill
ora contiene le regole per non farsi sgamare dalla foto (o per farsi sgamare
apposta, ai livelli alti), e a ogni consegna **propone anche il prompt pronto
per generare l'immagine del post**: estetica da foto di smartphone, niente testo
in scena, luce e stagione coerenti con quello che il post racconta.

## La skill di analisi

Dai a `linkedin-cringe-analytics` l'URL di un post LinkedIn e ottieni un report
markdown in `analisi/YYYY-MM-DD-<tema>/report.md` con:

- **la classifica creduloni/svegli**: quanti ci hanno creduto (😇), quanti
  hanno colto lo scherzo (🎭), i dubbiosi (🤨) e i non classificabili (⬜),
  con le percentuali calcolate sui soli commenti decidibili;
- **la top ten dei commenti per gradimento** (reazioni, con tie-break sulle
  risposte generate);
- **i fenomeni ricorrenti**: citazioni, tormentoni, le trappole del post
  notate dai lettori;
- **la distribuzione dei toni** (ironico, motivazionale, correttivo,
  logico-forense, indignato, aneddotico);
- **l'incrocio categoria × esito**: chi ci casca, per tipo di profilo;
- **il cringe-metro dei commenti**: i commenti in buona fede più cringe,
  valutati con la scala 1-10 della skill gemella.

Come si procura i commenti: con l'estensione **Claude in Chrome** fa tutto da
sola nel tuo browser loggato (ordina per "più recenti", scrolla, espande le
risposte, deduplica); senza estensione basta incollare il testo della pagina.
Il playbook tecnico (DOM offuscato, liste virtualizzate, lazy-load) è in
[`references/estrazione.md`](.claude/skills/linkedin-cringe-analytics/references/estrazione.md).

Due regole fisse: i **commentatori sono sempre anonimizzati** nel report
(niente nomi, solo categorie: "un recruiter", "una pagina satirica"), e la
**copertura è sempre dichiarata** ("letti X commenti su un contatore di Y": il
contatore di LinkedIn include i commenti cancellati e filtrati).

### Risultati sul campo

I report vengono scritti in `analisi/` (che resta fuori dal repository: sono
dati sui post di chi usa la skill). I primi due, generati su post pubblicati
per davvero, hanno dato questi numeri:

| Post | Età | Impressioni | Creduloni | Svegli |
|---|---|---|---|---|
| A (livello 7, virale) | 1 giorno | sei cifre | **~36%** | ~57% |
| B (livello 9, recente) | 8 ore | cinque cifre | ~8% | **~86%** |

La differenza non è nel testo: è nel pubblico. Nelle prime ore commenta la
cerchia che conosce il gioco; i creduloni arrivano con la viralità. Bonus
statistico: quando nel post compare un oggetto con un'àncora comica nazionale,
più di un commento su dieci cita la scenetta di riferimento.

## Il Cringiometro

Dai a `linkedin-cringe-meter` l'URL di un post LinkedIn (anche uno short link
`lnkd.in`), oppure il testo incollato o uno screenshot, e ottieni:

- **il livello 1-10** sulla stessa scala del generatore (1-2 innocuo, 3-4
  lieve, 5-6 fastidioso, 7-8 imbarazzante, 9 insostenibile, 10 leggendario),
  con lo scarto evento → morale in una riga;
- **i ganci presi**: i moduli del catalogo rilevati, ciascuno con la citazione
  del post che lo prova;
- il **registro** (credibile, parodico, surreale deadpan, o *cringe dichiarato*
  se c'è la riga di disclaimer), il **sapore-AI** (bassa/media/alta), la
  **lead-gen** e dove si nasconde;
- **il verdetto**: una frase secca, stile blastometro ma in tema cringe;
- **cosa manca per salire** di un livello, che è il ponte col generatore;
- un report markdown in `analisi/YYYY-MM-DD-<tema>/cringiometro.md` e
  **un'immagine 1080×1080** pronta da lasciare come risposta sotto al post.

Con l'estensione **Claude in Chrome** legge il post da sola nel tuo browser
loggato (solo il testo del post, non i commenti); senza, incolli il testo.
L'immagine **parla la lingua del post**: titolo, registro e parola della scala
sono localizzati (italiano, inglese, tedesco, francese, spagnolo, altre via
override), e i nomi dei moduli, il verdetto e la citazione vengono scritti in
quella lingua. Il report resta nella tua.

### Galleria

I primi quattro sono post inventati, presi da
[`references/esempi.md`](.claude/skills/linkedin-cringe/references/esempi.md)
del generatore (per questo il registro è "cringe dichiarato"); gli ultimi due
sono post reali in inglese, anonimizzati.

| | | |
|---|---|---|
| <img src="assets/cringiometro-4.png" width="300" alt="Cringiometro 4/10, lieve: C03 C11 C21"> | <img src="assets/cringiometro.png" width="300" alt="Cringiometro 7/10, imbarazzante: C01 C13 C08 C21 C10 C23"> | <img src="assets/cringiometro-9.png" width="300" alt="Cringiometro 9/10, insostenibile: C19 C02 C04 C13 C30 C31 C23"> |
| 4/10, l'humblebrag sobrio | 7/10, la macchinetta del caffè | 9/10, la pasticceria e il P.P.S. |
| <img src="assets/cringiometro-10.png" width="300" alt="Cringiometro 10/10, leggendario: C06 C09 C13 C22 C29 C24 C23"> | <img src="assets/cringiometro-en-7.png" width="300" alt="Cringe Meter 7/10, embarrassing: C30 C10 C33 C14 C08"> | <img src="assets/cringiometro-en-2.png" width="300" alt="Cringe Meter 2/10, harmless: C23"> |
| 10/10, le 5:17 e la neonata | 7/10 in inglese, post reale: il collasso della società e poi "hire me" | 2/10 in inglese, post reale: una demo di prodotto che ammette di esserlo |

L'ultimo è il campione di controllo: un post tecnico onesto deve uscire basso.
Il Cringiometro distingue il cringe dal marketing dichiarato, dall'opinione
che non condividi e dal post semplicemente brutto (che è un 2, non un 7).

### Come è fatto

Il voto lo dà il modello leggendo `tassonomia.md` e `moduli.md` del generatore
attraverso la rubrica in
[`references/valutazione.md`](.claude/skills/linkedin-cringe-meter/references/valutazione.md):
prima lo scarto, poi i moduli con prova, poi ±1 per il registro. Ogni modulo
senza citazione non conta. L'immagine la disegna
[`scripts/cringiometro.py`](.claude/skills/linkedin-cringe-meter/scripts/cringiometro.py)
(Python + Pillow, nessun browser) a partire da un JSON con punteggio, registro,
moduli, verdetto, citazione e lingua: si può ritoccare il JSON e rigenerare a
mano. Senza Pillow esce l'SVG.

L'immagine **non porta mai nome, foto o headline dell'autore**: si giudica il
post, non la persona, e il soggetto delle frasi è sempre il post. Lutti,
malattie e licenziamenti veri non si valutano. Lasciare l'immagine come
risposta sotto al post di un estraneo è una scelta tua: la skill consegna il
file e si ferma lì.

## Struttura

```
.claude/skills/
├── linkedin-cringe/                generazione
│   ├── SKILL.md                    flusso, domande, regole, paletti
│   └── references/
│       ├── tassonomia.md           definizione del cringe, scala 1-10
│       ├── moduli.md               catalogo dei 37 moduli C01-C37
│       ├── attualita.md            il gancio reale: cringe ispirato ai fatti
│       ├── surreale.md             il registro deadpan: regole, repertorio, diagnosi
│       ├── lessico.md              itanglese, formule, hashtag, altre lingue
│       └── esempi.md               post calibrati sui livelli 4, 7, 9, 10
├── linkedin-cringe-analytics/      analisi
│   ├── SKILL.md                    flusso: acquisizione, analisi, report
│   └── references/
│       ├── estrazione.md           playbook browser + fallback manuale + parsing
│       ├── classificazione.md      criteri creduto/colto, toni, categorie
│       └── report.md               struttura del report e regole di consegna
└── linkedin-cringe-meter/          cringiometro
    ├── SKILL.md                    flusso: acquisizione, valutazione, immagine
    ├── references/
    │   ├── valutazione.md          la rubrica: livello, moduli, verdetto
    │   └── report.md               struttura del report e regole di anonimato
    └── scripts/
        └── cringiometro.py         genera PNG + SVG dell'immagine di risposta
analisi/                            i report prodotti (anonimizzati)
assets/                             banner del README, galleria del cringiometro
community/                          i post cringe accettati dalla community
```

## Installazione

Le skill vivono in `.claude/skills/` dentro questo repository, quindi
**clonando il repo sono già installate**: apri Claude Code nella cartella e le
trovi disponibili senza fare altro.

```bash
git clone https://github.com/matteobaccan/LinkedInCringe.git
cd LinkedInCringe
```

### Per usarle in tutti i tuoi progetti

Copiale fra le skill personali. Da quel momento sono disponibili ovunque.

**PowerShell (Windows):**

```powershell
Copy-Item -Recurse .claude\skills\linkedin-cringe "$env:USERPROFILE\.claude\skills\linkedin-cringe"
Copy-Item -Recurse .claude\skills\linkedin-cringe-analytics "$env:USERPROFILE\.claude\skills\linkedin-cringe-analytics"
Copy-Item -Recurse .claude\skills\linkedin-cringe-meter "$env:USERPROFILE\.claude\skills\linkedin-cringe-meter"
```

**Bash (macOS / Linux / Git Bash):**

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/linkedin-cringe ~/.claude/skills/linkedin-cringe
cp -r .claude/skills/linkedin-cringe-analytics ~/.claude/skills/linkedin-cringe-analytics
cp -r .claude/skills/linkedin-cringe-meter ~/.claude/skills/linkedin-cringe-meter
```

Se le installi in entrambi i posti tieni presente che diventano copie
indipendenti: modificandone una, l'altra resta indietro.

### Verifica

Digita `/linkedin-cringe`, `/linkedin-cringe-analytics` o
`/linkedin-cringe-meter`. Se compaiono nell'elenco delle skill, sono installate.
Il Cringiometro usa Pillow per l'immagine: `pip install pillow` se manca
(senza, consegna l'SVG).

## Uso

Generazione:

```
/linkedin-cringe
```

```
fammi un post cringe livello 8, credibile, voce da recruiter, tema colloqui
```

```
rifallo con i moduli C15 e C32
```

```
scrivimi un post livello 7, voce founder, ispirato all'attualità
```

Analisi:

```
/linkedin-cringe-analytics https://www.linkedin.com/posts/...
```

```
analizza i commenti di questo post: <URL>
```

Cringiometro:

```
/linkedin-cringe-meter https://lnkd.in/p/...
```

```
quanto è cringe questo post? <testo incollato>
```

```
cringiometro su questi tre: <URL> <URL> <URL>
```

L'immagine esce nella lingua del post; se vuoi forzarla ("immagine in
inglese"), basta dirlo.

## Paletti

Anche in modalità "credibile" la skill di generazione non produce:

- post attribuiti a **persone reali** o firmati da **aziende esistenti**
- lutti, malattie o licenziamenti **reali** usati come materiale narrativo
- contenuti che imitino un profilo specifico per farlo passare per autentico

I nomi sono sempre di fantasia. È satira, non impersonificazione.

La skill di analisi, dal canto suo: **anonimizza sempre i commentatori** nei
report, giudica i commenti e mai le persone, tiene i dati grezzi fuori dal
repository e si limita a leggere un thread pubblico.

Il Cringiometro **non nomina mai l'autore** del post valutato (né nel report,
né nell'immagine, né in chat), giudica il post e non la persona, e si rifiuta
di dare un voto a lutti, malattie e licenziamenti veri. Lasciare l'immagine
come risposta sotto al post di un estraneo è una scelta di chi la usa: la skill
consegna il file e si ferma lì.

## Manda il tuo cringe

Il catalogo migliora coi dati veri, e i dati veri li avete voi: il post del
fuffaguru che vi ha fatto chiudere l'app, il recruiter-filosofo, quello che
avete scritto voi nel 2019 e che ancora vi sveglia di notte.

**Mandatecelo.** Aprite una
[issue](https://github.com/matteobaccan/LinkedInCringe/issues) con il testo
del post, o direttamente una PR su `esempi.md`. Regole di ingaggio:

- **anonimizzato**: niente nomi reali, niente aziende riconoscibili, niente
  screenshot con foto profilo — il paletto qui sopra vale anche all'incontrario;
- diteci se è **trovato in natura o scritto da voi** (non giudichiamo, anzi:
  il cringe autoprodotto consapevole è ricerca);
- se vi va, azzardate **livello 1-10 e moduli** che ci vedete, o passatelo
  prima al Cringiometro e allegate l'immagine: se il post non rientra in
  nessuno dei 37, potreste aver appena scoperto il C38.

I post accettati finiscono in [`community/`](community/), i migliori negli
esempi della skill, e i pattern nuovi diventano moduli del catalogo. Il
vostro imbarazzo non andrà sprecato.

## Ringraziamenti

A [**Maicol Pirozzi**](https://youtube.com/playlist?list=PLCj24iwop8vijRvocuUO85rEqRU4-o2Mv) e alla community di
[r/LinkedInCringeIT](https://www.reddit.com/r/LinkedInCringeIT/), per le
infinite ispirazioni: il catalogo dei moduli deve molto al materiale che
LinkedIn produce ogni giorno e che loro, instancabili, raccolgono.

## Licenza

MIT.
