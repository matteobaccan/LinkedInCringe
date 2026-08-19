---
name: linkedin-cringe
description: Genera post LinkedIn cringe (italiano di default, ma funziona in qualunque lingua), calibrati su livello di cringe (1-10), credibilità (deve passare per vero / parodia dichiarata) e moduli cringe scelti da un catalogo di 31. Usala quando l'utente chiede un post LinkedIn cringe, motivazionale, da fuffaguru, da founder, da HR o da boomer, oppure vuole parodiare lo stile LinkedIn.
---

# LinkedIn Cringe: generatore di post

Genera post LinkedIn in italiano che riproducono il cringe autentico di LinkedIn Italia.

## Principio guida

Il cringe non è "scritto male". Il cringe è **imbarazzo vicario**: nasce quando chi
scrive ci crede davvero, rivendica una profondità che il testo non ha, e sta vendendo
qualcosa fingendo di non vendere nulla.

**Regola non negoziabile: la voce non strizza mai l'occhio.** Nessuna ironia, nessuna
autoconsapevolezza, nessun ammicco al lettore. Appena il testo ammicca, smette di essere
cringe e diventa barzelletta.

Leggi `references/tassonomia.md` prima di scrivere: contiene la definizione operativa,
la legge dello scarto e la scala 1-10.

## Flusso

### 1. Raccogli i parametri

Se l'utente ha già indicato tema, livello o moduli nella richiesta, **non fare domande**:
usa quello che ha detto e riempi i buchi con i default (livello 7, credibile).

Altrimenti mostra prima il **menu dei moduli**: elenco compatto, codice + nome, preso da
`references/moduli.md`, e poi chiedi i parametri con **AskUserQuestion**, quattro domande:

**D1. Livello di cringe** (`header: "Livello"`)
- `4` Lieve: passa inosservato, lascia solo un leggero fastidio
- `7` Imbarazzante (consigliato): il punto dolce, chi legge fa una faccia
- `9` Insostenibile: screenshottabile, il tipo di post che gira nelle chat
- `10` Leggendario: tutti i tic insieme, oltre il limite del sopportabile

**D2. Credibilità** (`header: "Registro"`)
- `Credibile (consigliato)`: deve poter passare per un post vero, pescato dal feed.
  Nessuna esagerazione che tradisca la finzione.
- `Parodico`: esagerazione dichiarata, si capisce che è una presa in giro

**D3. Voce** (`header: "Voce"`)
- `Fuffaguru mindset`: coach/consulente che vende crescita personale
- `Founder / CEO`: imprenditore che flexa mascherando da lezione
- `HR / recruiter`: chi dà lezioni di vita ai candidati
- `Boomer con consiglio`: over 50 che spiega la vita ai giovani

**D4. Moduli cringe da inserire** (`header: "Ingredienti"`, `multiSelect: true`)
Quattro combo pronte; l'utente può usare "Other" per scrivere i codici del catalogo
(es. `C01, C13, C19`):
- `Parabola + colpo di scena` (C01 + C02 + C19)
- `Vulnerabilità + numeri` (C03 + C13 + C11)
- `Hustle + boomerata` (C06 + C14 + C07)
- `Pacchetto completo`: scegli tu i moduli coerenti col livello

Se manca il tema, chiedilo a parte in chat con una riga, non con AskUserQuestion.

**Lingua.** Default: italiano. Non è una quinta domanda, si deduce dalla richiesta
("un post in inglese", "per il mercato tedesco", oppure il fatto che l'utente scriva in
un'altra lingua). Se richiesta una lingua diversa dall'italiano, leggi la sezione
*Adattamento ad altre lingue* in `references/lessico.md` prima di scrivere.
**Non tradurre mai un post italiano: rigeneralo dai moduli nella lingua target.**

### 2. Scegli i moduli

Consulta `references/moduli.md`. Numero di moduli in base al livello:

| Livello | Moduli narrativi | Tic formali |
|---------|------------------|-------------|
| 1-3     | 1                | broetry leggera, 2-3 hashtag |
| 4-6     | 2                | broetry, CTA, 4-6 hashtag |
| 7-8     | 3-4              | + emoji-bullet, numeri finti, P.S. |
| 9-10    | 5+               | tutto: muro di hashtag, MAIUSCOLO, foto scollegata |

I moduli scelti dall'utente hanno la precedenza; aggiungine altri per arrivare al conto.

### 3. Scrivi il post

Struttura canonica (modulo C21):

```
HOOK shock                    <- 1 riga, spesso una domanda o un'affermazione brutale
[riga vuota]
micro-narrazione              <- una frase per riga, mai un paragrafo
[riga vuota]
COLPO DI SCENA                <- la battuta che "cambia tutto"
[riga vuota]
morale universale             <- slegata dai fatti, più grande dell'aneddoto
[riga vuota]
CTA + emoji                   <- "E tu? 👇"
muro di hashtag
[riga vuota]
riga di disclaimer            <- vedi sezione dedicata, sempre presente
```

Usa `references/lessico.md` per itanglese aziendale, formule d'attacco, formule di
svolta, chiusure, nomi di fantasia, pool di hashtag ed emoji.

**Leva principale del cringe: la distanza fra l'evento e la morale.** Più l'evento è
banale e la morale è cosmica, più alto il cringe. Non alzare il livello aggiungendo
emoji: alza lo scarto.

Consulta `references/esempi.md` per sentire come suonano i livelli 4, 7, 9 e 10.

### 4. Consegna

Mostra il post in un blocco di codice, così si copia-incolla senza che il markdown
mangi la formattazione, poi in due righe elenca i moduli usati con i loro codici.

Chiudi sempre offrendo un giro successivo: alzare o abbassare il livello, cambiare voce,
rigenerare con altri moduli.

## Non deve sembrare scritto da un'AI

Un post che profuma di modello linguistico non è credibile come cringe umano, e il cringe
umano è tutto il punto. Questa regola vale sempre, a qualunque livello e in qualunque lingua.

**Vietato in output:**

- **Il trattino lungo.** Mai. Al suo posto: punto, virgola, due punti, parentesi.
- Frasi tutte della stessa lunghezza, paragrafi tutti della stessa misura.
- Le triadi perfette ("non solo X, ma anche Y, e soprattutto Z").
- I connettivi levigati: "inoltre", "tuttavia", "pertanto", "in conclusione".
- Le formule da assistente: "è importante notare", "vale la pena sottolineare".
- Il paragrafo finale che riassume quello che si è appena detto.
- Elenchi in cui ogni voce ha la stessa struttura sintattica.
- Lessico uniformemente medio-alto, senza una sola ripetizione.

**Obbligatorio, per suonare umani:**

- Ripetere una parola invece di cercare il sinonimo.
- Alternare frasi lunghissime e frasi di due parole.
- Almeno un dettaglio concreto e inutile: un orario, un oggetto, un nome, una cifra sciatta.
- Una piccola sbavatura: una virgola di troppo, un anglicismo storpiato, una ripetizione.
- Chiudere di colpo, senza tirare le somme.

Il modulo `C12` (sapore-AI) è l'unica eccezione, ed è opt-in: si usa quando si vuole
ritrarre *l'umano che copia-incolla dall'AI senza accorgersene*. Anche lì i cliché vanno
inseriti dentro un testo che per il resto suona umano, mai al posto suo.

## Riga finale di disclaimer

**Dopo gli hashtag, sempre**, separata da una riga vuota, aggiungi una riga che riveli lo
scherzo. Serve a chi legge e serve all'utente, che poi decide se tenerla o toglierla.

Base: "Hai letto fino a qui e volevi uccidermi? Non farlo, è semplicemente ironia."

**Varia sempre la formulazione.** Non ripetere due volte di fila la stessa riga: pesca o
improvvisa dal repertorio in `references/lessico.md`, e quando puoi rendila specifica sul
contenuto del post (è più divertente di una formula generica).

Questa riga è l'unico punto in cui la voce può ammiccare. Il corpo del post sopra di essa
resta rigorosamente serio: se l'ironia risale dentro il testo, il cringe si spegne.

Quando consegni, di' all'utente in mezza riga che quella è la riga rimovibile.


## Paletti

Valgono anche quando il registro è "credibile", anzi, soprattutto lì:

- **Nessuna persona reale.** Nomi di fantasia. Mai mettere in bocca a una persona
  esistente un post che non ha scritto.
- **Nessuna azienda reale** come autrice o bersaglio. I marchi si citano solo di
  sfuggita come oggetti ("ho aperto Excel").
- **Niente lutti, malattie o licenziamenti reali** dell'utente o di terzi. Il modulo C17
  (trauma mining) si usa solo con eventi palesemente inventati, e va segnalato.
- Se l'utente vuole pubblicarlo davvero, ricordagli una volta che è un post finto,
  poi fai quello che chiede.
