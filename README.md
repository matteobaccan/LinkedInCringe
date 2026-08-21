```
              L I N K E D I N
 ██████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗
██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝
██║     ██████╔╝██║██╔██╗ ██║██║  ███╗█████╗
██║     ██╔══██╗██║██║╚██╗██║██║   ██║██╔══╝
╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
──────────────────────────────────────────────
 Un post.

 Una morale.

 Nessun rapporto tra le due.

                             Sei d'accordo? 👇
 #mindset #leadership #grateful #hustle
──────────────────────────────────────────────
```

# LinkedIn Cringe

Due skill per Claude Code, una coppia che si chiude a cerchio:

- **`linkedin-cringe`** genera post LinkedIn cringe in italiano, quelli veri,
  quelli che vengono screenshottati e girati nelle chat;
- **`linkedin-cringe-analytics`** scarica i commenti del post una volta
  pubblicato e misura cosa è successo: quanti ci hanno creduto, quanti hanno
  colto lo scherzo, la top ten per gradimento, i toni, il cringe involontario
  dei commenti stessi.

Quello che la seconda skill scopre finisce nei moduli della prima: il catalogo
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
| **Credibilità** | credibile (deve passare per vero) · parodico (satira dichiarata) |
| **Voce** | fuffaguru · founder/CEO · HR/recruiter · boomer con consiglio |
| **Moduli cringe** | scelta multipla da un catalogo di 33 moduli (`C01`…`C33`) |

Se invece scrivi già tutto nella richiesta (`post livello 9, credibile, tema
smart working, moduli C19 e C02`), salta le domande e genera direttamente.

### Il catalogo dei moduli

33 moduli codificati in
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

Gli ultimi due sono nati dall'analisi sul campo: `C32` dall'osservazione che la
sedia rimessa a posto *prima di alzarsi* ha generato thread interi, `C33` dal
fatto che il 13% dei commenti a un post virale erano correzioni serissime sulla
RAL. Chi ti corregge ti ha creduto.

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
Gli altri livelli (7, 9, 10 e una versione parodica) sono in
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
| la sedia | 1 giorno | ~122.000 | **36,0%** | 56,8% |
| Athos, le 5:41 | 8 ore | ~24.600 | 8,3% | **86,1%** |

La differenza non è nel testo: è nel pubblico. Nelle prime ore commenta la
cerchia che conosce il gioco; i creduloni arrivano con la viralità. Bonus
statistico: sul post della sedia, il 13,4% dei commenti citava la "cadrega" di
Aldo, Giovanni e Giacomo.

## Struttura

```
.claude/skills/
├── linkedin-cringe/                generazione
│   ├── SKILL.md                    flusso, domande, regole, paletti
│   └── references/
│       ├── tassonomia.md           definizione del cringe, scala 1-10
│       ├── moduli.md               catalogo dei 33 moduli C01-C33
│       ├── lessico.md              itanglese, formule, hashtag, altre lingue
│       └── esempi.md               post calibrati sui livelli 4, 7, 9, 10
└── linkedin-cringe-analytics/      analisi
    ├── SKILL.md                    flusso: acquisizione, analisi, report
    └── references/
        ├── estrazione.md           playbook browser + fallback manuale + parsing
        ├── classificazione.md      criteri creduto/colto, toni, categorie
        └── report.md               struttura del report e regole di consegna
analisi/                            i report prodotti (anonimizzati)
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
```

**Bash (macOS / Linux / Git Bash):**

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/linkedin-cringe ~/.claude/skills/linkedin-cringe
cp -r .claude/skills/linkedin-cringe-analytics ~/.claude/skills/linkedin-cringe-analytics
```

Se le installi in entrambi i posti tieni presente che diventano copie
indipendenti: modificandone una, l'altra resta indietro.

### Verifica

Digita `/linkedin-cringe` o `/linkedin-cringe-analytics`. Se compaiono
nell'elenco delle skill, sono installate.

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

Analisi:

```
/linkedin-cringe-analytics https://www.linkedin.com/posts/...
```

```
analizza i commenti di questo post: <URL>
```

## Paletti

Anche in modalità "credibile" la skill di generazione non produce:

- post attribuiti a **persone reali** o firmati da **aziende esistenti**
- lutti, malattie o licenziamenti **reali** usati come materiale narrativo
- contenuti che imitino un profilo specifico per farlo passare per autentico

I nomi sono sempre di fantasia. È satira, non impersonificazione.

La skill di analisi, dal canto suo: **anonimizza sempre i commentatori** nei
report, giudica i commenti e mai le persone, tiene i dati grezzi fuori dal
repository e si limita a leggere un thread pubblico.

## Licenza

MIT.
