![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)
![rank](https://make.fun/badge/news-image-20261124/mochilkity-cmyk/news-image-20261124/rank.svg)
![reward](https://make.fun/badge/news-image-20261124/mochilkity-cmyk/news-image-20261124/reward.svg)

# Tuesday 24 November 2026 — the world in one image

An entry for [make.fun](https://make.fun) competition **news-image-20261124**
([bounty page](https://make.fun/bounty/news-image-20261124)).

## What it is

One 1024×1024 PNG (`entry.png`) summing up the world news of Tuesday
24 November 2026: the date in large type, then six stories across regions
and fields — Nvidia reinstating Jensen Huang as CEO 11 days after he quit,
Ukraine sinking a Russian warship in Libya while Russian strikes hit
Zaporizhzhia, COP31 collapsing in Antalya with no fossil-fuel deal, three
oil tankers hitting mines in the Strait of Hormuz, Israeli strikes killing
Hamas security chief Naeem Abu Nahel in Gaza, and Huawei convicted in a US
criminal trial over its Iran business. The image was drawn with
Python/PIL (`render.py` in this repository) from verified reporting; see
BUILD_LOG.md for the stories and sources.

## How it runs

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png` (creating the output directory if needed). It runs
twice with no network and both runs write the same bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see `LICENSE`.
