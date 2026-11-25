# Build log — news-image-20261124

Built Wed 25 Nov 2026 (08:00 WIB) by the scheduled build job, in one
session started after the competition opened (2026-11-24T00:00Z).

## The day's news (24 Nov 2026, Tuesday)

Researched from live sources on the morning of 25 Nov 2026 (Just Security
Early Edition, Reuters world summary, Morningstar/Dow Jones, CWEB daily
headlines, The Global Eye, Medium/All Voices brief):

1. **Nvidia — Huang back as CEO.** Nvidia reinstated Jensen Huang as CEO
   on Monday, 11 days after he resigned; Trump said he personally
   persuaded the board. Shares jumped about 30%; markets rebounded.
2. **Ukraine — sinks Russian warship.** President Zelenskyy confirmed
   Ukraine's naval drones sank a Russian warship at a base in Libya
   (Saturday's strike, confirmed Tuesday); overnight Russian strikes on
   Zaporizhzhia killed 2 and wounded about 40, including children.
3. **Climate — COP31 collapses.** The UN climate summit in Antalya, Turkey,
   ended without an overarching agreement; the final text drops any
   mention of fossil fuels.
4. **Middle East — mines hit tankers in Hormuz.** Iran said three oil
   tankers hit mines and caught fire in the Strait of Hormuz this week,
   and that it will not negotiate until its seven conditions are met.
5. **Gaza — strikes kill Hamas security chief.** Israeli airstrikes killed
   the director of Hamas' internal security apparatus, Naeem Abu Nahel,
   and six others, including two police officers, medics said.
6. **Law — Huawei convicted in US trial.** China's Huawei was convicted in
   a sprawling US criminal trial over its business in Iran.

Also in the news: Trump awards Rudy Giuliani the Medal of Freedom; French
officials order former President Sarkozy's corruption case to trial;
Sanofi strikes a $41bn deal to buy Insmed; a bus crash in Ras Al Khaimah,
UAE, kills 13.

## Build

- `render.py` (Python 3 + PIL, stdlib + Pillow, deterministic) draws the
  1024×1024 PNG: navy masthead with the date, six story cards with a
  drawn icon, headline, short body and region tag, plus an
  "also in the news" strip.
- `main.ts` (Node 22, stdlib only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).
- Determinism: run `main.ts` twice, compare sha256 — both runs must be
  byte-identical (a plain file copy, so they are by construction).
- Kit check: `node cli/makefun.mjs check --kit <kit> --repo <repo>
  --transcripts <bundle>` until 0 failed.
