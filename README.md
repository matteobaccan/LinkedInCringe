```
      ██╗     ██╗███╗   ██╗██╗  ██╗███████╗██████╗ ██╗███╗   ██╗
      ██║     ██║████╗  ██║██║ ██╔╝██╔════╝██╔══██╗██║████╗  ██║
      ██║     ██║██╔██╗ ██║█████╔╝ █████╗  ██║  ██║██║██╔██╗ ██║
      ██║     ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║  ██║██║██║╚██╗██║
      ███████╗██║██║ ╚████║██║  ██╗███████╗██████╔╝██║██║ ╚████║
      ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═══╝

             ██████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗
            ██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝
            ██║     ██████╔╝██║██╔██╗ ██║██║  ███╗█████╗
            ██║     ██╔══██╗██║██║╚██╗██║██║   ██║██╔══╝
            ╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝███████╗
             ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

      ──────────────────────────────────────────────────────────
       Un post.

       Una morale.

       Nessun rapporto tra le due.

                                          Sei d'accordo? 👇
       #mindset #leadership #crescitapersonale #grateful #hustle
      ──────────────────────────────────────────────────────────
```

# LinkedIn Cringe

Una skill per Claude Code che genera post LinkedIn cringe in italiano, quelli veri,
quelli che vengono screenshottati e girati nelle chat.

Non genera "post brutti". Genera **imbarazzo vicario**: post in cui chi scrive ci crede
davvero, rivendica una profondità che il testo non ha, e sta vendendo qualcosa fingendo
di non vendere nulla.

## Cosa chiede

Quando la invochi senza parametri, la skill ti fa quattro domande:

| Domanda | Opzioni |
|---|---|
| **Livello di cringe** | 4 lieve · 7 imbarazzante · 9 insostenibile · 10 leggendario |
| **Credibilità** | credibile (deve passare per vero) · parodico (satira dichiarata) |
| **Voce** | fuffaguru · founder/CEO · HR/recruiter · boomer con consiglio |
| **Moduli cringe** | scelta multipla da un catalogo di 31 moduli (`C01`…`C31`) |

Se invece scrivi già tutto nella richiesta (`post livello 9, credibile, tema smart working,
moduli C19 e C02`), salta le domande e genera direttamente.

## Il catalogo dei moduli

31 moduli codificati in [`references/moduli.md`](.claude/skills/linkedin-cringe/references/moduli.md),
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

## Lingue

Il default è l'italiano, ma il cringe non è un fenomeno italiano: cambia il rivestimento,
non il meccanismo. Chiedendo un post in un'altra lingua, la skill **rigenera dai moduli**
invece di tradurre (un post tradotto suona tradotto, e smette di essere credibile).

Restano invariati la definizione, la scala e la struttura; vengono sostituiti lo strato di
gergo contaminato (in italiano l'itanglese, in inglese il buzzword corporate, in tedesco il
Denglisch…), gli hashtag, e i quattro moduli a radice culturale (`C14` `C15` `C19` `C26`),
che vanno riscritti sul mercato del lavoro locale. Dettagli in
[`references/lessico.md`](.claude/skills/linkedin-cringe/references/lessico.md).

## Riga finale

Ogni post generato finisce, dopo gli hashtag, con una riga che rivela lo scherzo
("Hai letto fino a qui e volevi uccidermi? Non farlo, è semplicemente ironia."). La
formulazione cambia ogni volta e, quando possibile, riprende un dettaglio del post.
È l'unico punto in cui la voce ammicca: il corpo sopra resta serio, altrimenti il cringe
si spegne. Sta all'utente decidere se tenerla o cancellarla prima di pubblicare.

## Niente sapore-AI

Un post che profuma di modello linguistico non è credibile come cringe umano. La skill
vieta in output il trattino lungo, i connettivi levigati, le triadi perfette, i paragrafi
tutti della stessa misura e il finale riassuntivo; e impone almeno un dettaglio concreto
inutile, un ritmo irregolare e una piccola sbavatura.

## Come si tara il livello

La leva non sono le emoji. È la **distanza fra l'evento raccontato e la morale che ci si
costruisce sopra**: più l'evento è minuscolo e la morale è cosmica, più alto il cringe.

## Esempi

### Livello 4: credibile

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
Tre hashtag, zero emoji. Passa inosservato nel feed.

### Livello 9: credibile

```
Ieri mattina sono entrato in una piccola pasticceria di provincia.

Erano le 7:40.

Dietro il bancone, una signora sui sessanta impastava a mano.
Da sola.
Come ogni mattina da 34 anni.

Le ho chiesto: "Signora, ma non ha mai pensato di assumere qualcuno?"

Lei non ha alzato la testa dall'impasto.

Ha detto solo tre parole:

"Insegnare a chi?"

Silenzio.

Sono rimasto lì, con il caffè in mano, a ripensare a tutte le aziende che ho
visto in 12 anni di consulenza.

Aziende da 40 dipendenti.
Aziende da 200.
Aziende con budget di formazione a sei cifre.

E nessuna capace di rispondere a quella domanda.

Il 78% dei manager che incontro mi parla di retention.
Nessuno mi parla di TRASMISSIONE.

Quella signora non ha un profilo LinkedIn.
Non ha un personal brand.
Non ha mai fatto un corso di leadership.

Ma ha capito prima di tutti noi una cosa semplice:

Non si costruisce un'azienda.
Si costruisce chi verrà dopo.

E tu, oggi, a chi stai insegnando? 👇

P.S. Ho preso tre paste. Le migliori della mia vita.
P.P.S. Ad ottobre apro le ultime 4 sessioni del mio percorso "Trasmissione".
Scrivimi in privato la parola PASTICCERIA.

#leadership #mindset #people #formazione #impresaitaliana #gratitudine
#crescitapersonale #softskills #madeinitaly #trasmissione

Hai letto fino a qui e volevi uccidermi? Non farlo, è semplicemente ironia.
```

Cinque moduli sovrapposti (`C19` `C02` `C04` `C13` `C30`), il P.P.S. che smaschera la
lead-gen, il muro di hashtag, una morale cosmica costruita su tre paste. Screenshottabile
, e ancora perfettamente credibile.

Altri livelli (7, 10, e una versione parodica) in
[`references/esempi.md`](.claude/skills/linkedin-cringe/references/esempi.md).

> **Nota.** Nessun esempio in questo repository è la trascrizione o il rimaneggiamento di
> un post reale. Sono tutti scritti da zero applicando la tassonomia e i moduli. Nomi,
> aziende, numeri e aneddoti sono inventati.

## Installazione

La skill vive in `.claude/skills/linkedin-cringe/` dentro questo repository, quindi
**clonando il repo è già installata**: apri Claude Code nella cartella e la trovi
disponibile senza fare altro.

```bash
git clone https://github.com/matteobaccan/LinkedInCringe.git
cd LinkedInCringe
```

### Per usarla in tutti i tuoi progetti

Copiala fra le skill personali. Da quel momento è disponibile ovunque, non solo qui.

**PowerShell (Windows):**

```powershell
Copy-Item -Recurse .claude\skills\linkedin-cringe "$env:USERPROFILE\.claude\skills\linkedin-cringe"
```

**Bash (macOS / Linux / Git Bash):**

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/linkedin-cringe ~/.claude/skills/linkedin-cringe
```

Se la installi in entrambi i posti tieni presente che diventano due copie indipendenti:
modificandone una, l'altra resta indietro.

### Per portarla in un altro progetto

Copia `.claude/skills/linkedin-cringe/` dentro il `.claude/skills/` del progetto di
destinazione e committala: così è disponibile a chiunque ci lavori.

### Verifica

Digita `/linkedin-cringe`. Se compare nell'elenco delle skill, è installata.

## Uso

```
/linkedin-cringe
```

e rispondi alle domande. Oppure in linguaggio naturale:

```
fammi un post cringe livello 8, credibile, voce da recruiter, tema colloqui
```

```
post livello 10 parodico su un founder che torna dalle ferie
```

```
rifallo con i moduli C15 e C18
```

## Struttura

```
.claude/skills/linkedin-cringe/
├── SKILL.md                    flusso, domande, regole di composizione, paletti
└── references/
    ├── tassonomia.md           definizione del cringe, scala 1-10, asse credibilità
    ├── moduli.md               catalogo dei 31 moduli C01-C31
    ├── lessico.md              itanglese, formule, hashtag, emoji, adattamento ad altre lingue
    └── esempi.md               post calibrati sui livelli 4, 7, 9, 10 e parodico
```

## Paletti

Anche in modalità "credibile" la skill non genera:

- post attribuiti a **persone reali** o firmati da **aziende esistenti**
- lutti, malattie o licenziamenti **reali** usati come materiale narrativo
- contenuti che imitino un profilo specifico per farlo passare per autentico

I nomi sono sempre di fantasia. È satira, non impersonificazione.

## Licenza

MIT.
