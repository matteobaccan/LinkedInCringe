<img src="assets/banner.svg" width="560" alt="LINKEDIN CRINGE — A post. A moral. No connection between the two. Agree? 👇 #mindset #leadership #grateful #hustle">

🇮🇹 [Versione italiana](README.md) — the full README; this is the short tour.

# LinkedIn Cringe

Two skills for Claude Code that close the loop:

- **`linkedin-cringe`** generates cringe LinkedIn posts — the real kind, the
  kind that gets screenshotted and passed around in group chats;
- **`linkedin-cringe-analytics`** scrapes the comments once the post is
  published and measures what happened: how many believed it, how many got
  the joke, the top ten comments by reactions, the tones, the involuntary
  cringe of the comments themselves.

What the second skill discovers feeds back into the first: the catalog
improves with real data, not opinions.

The generator doesn't produce "bad posts". It produces **vicarious
embarrassment**: posts whose author truly believes them, claims a depth the
text doesn't have, and is selling something while pretending to sell nothing.

## Generation

Invoked bare, the skill asks four questions: **cringe level** (4 mild ·
7 embarrassing · 9 unbearable · 10 legendary), **credibility** (believable
vs. declared parody), **voice** (hustle guru, founder/CEO, HR/recruiter,
boomer with advice), and which of the **33 cringe modules** (`C01`…`C33`)
to build on — forced parables, moralistic plot twists, strategic
vulnerability, toxic hustle, fake-precise numbers, broetry, planted logical
errors, and more. Spell everything out in the request and it skips the
questions.

Italian is the default, but cringe is not an Italian phenomenon: ask for
another language and the skill **regenerates from the modules** instead of
translating (a translated post sounds translated, and stops being
believable). The jargon layer, hashtags and culture-bound modules are
rebuilt on the local job market.

Every generated post ends, after the hashtags, with one line revealing the
joke. Field-tested finding: the hashtag wall genuinely buries it — on one
viral post, a third of commenters believed the post anyway.

The skill also bans AI flavor (em-dashes, polished connectives, perfect
triads, uniform paragraphs) and, at delivery, proposes a ready-to-use
image-generation prompt that won't get debunked by commenters zooming in.

> **Note.** No example in this repository transcribes or reworks a real
> post. Everything is written from scratch from the taxonomy and modules;
> names, companies, numbers and anecdotes are invented.

## Analytics

Give `linkedin-cringe-analytics` a LinkedIn post URL and you get a markdown
report: believers 😇 vs. in-on-the-joke 🎭 (with honest denominators), top
ten comments by reactions, recurring phenomena, tone distribution,
commenter-category × outcome cross-table, and a cringe-meter of the most
earnest comments. With the **Claude in Chrome** extension it collects the
comments by itself in your logged-in browser; without it, pasting the page
text is enough.

Two fixed rules: commenters are **always anonymized** in reports, and
coverage is always declared ("read X comments of a counter showing Y").

Field results so far, from two really-published posts: on a viral level-7
post about **36% of commenters believed it**; on a level-9 post caught early,
~86% got the joke. The difference isn't the text — it's the audience that
virality brings in.

## Installation

The skills live in `.claude/skills/` inside this repository, so **cloning
the repo installs them**: open Claude Code in the folder and they're
available.

```bash
git clone https://github.com/matteobaccan/LinkedInCringe.git
cd LinkedInCringe
```

To use them everywhere, copy the two folders under `~/.claude/skills/`
(details in the [Italian README](README.md#installazione)).

## Usage

```
/linkedin-cringe
```

```
write me a level 8 cringe post, believable, recruiter voice, topic: job interviews
```

```
/linkedin-cringe-analytics https://www.linkedin.com/posts/...
```

## Guardrails

Even in "believable" mode the generator never produces posts attributed to
**real people** or signed by **existing companies**, never uses real grief,
illness or layoffs as material, and never imitates a specific profile to
pass it off as authentic. Names are always fictional: it's satire, not
impersonation. The analytics skill always anonymizes commenters, judges
comments and never people, and keeps raw data out of the repository.

## Send us your cringe

The catalog improves with real data, and the real data is in your feed: the
hustle-guru post that made you close the app, the recruiter-philosopher, the
one *you* wrote in 2019 that still keeps you up at night. Open an
[issue](https://github.com/matteobaccan/LinkedInCringe/issues) with the text
(anonymized: no real names, no recognizable companies), tell us whether it
was found in the wild or self-produced, and — if you dare — guess its level
and modules. If it fits none of the 33, you may have just discovered `C34`.
Accepted submissions land in [`community/`](community/).

## Thanks

To [**Maicol Pirozzi**](https://youtube.com/playlist?list=PLCj24iwop8vijRvocuUO85rEqRU4-o2Mv)
and the [r/LinkedInCringeIT](https://www.reddit.com/r/LinkedInCringeIT/)
community, for the endless inspiration.

## License

MIT.
