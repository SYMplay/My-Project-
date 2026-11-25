[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/SYMplay/My-Project-/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/SYMplay/My-Project-/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
# The World in One Day — 24 November 2026

Entry for the make.fun competition
[`news-image-20261124`](https://make.fun/bounty/news-image-20261124):
sum up 24 November 2026's world news in one image.

## The image

`entry.png` (1024 × 1024, PNG) is a newspaper front page:

- **Lead story** — oil tankers ablaze in the Strait of Hormuz: Iran says
  three tankers struck naval mines and caught fire; the claims are
  unverified and maritime authorities keep the threat level at "severe".
- **Nvidia** — Jensen Huang returns as CEO; shares jump about 30%.
- **Ukraine** — Ukraine sinks a Russian warship off Libya; a Russian strike
  on Zaporizhzhia kills 2 and wounds about 40.
- **Gaza** — Israeli strikes kill Hamas security chief Naeem Abu Nahel.
- **Law & Tech** — Oregon and Virginia sue SpaceX over Grok images.
- **Climate** — COP31 collapses without a deal on fossil fuels.
- **Washington** — Rep. Jimmy Gomez resigns after ethics findings.

Sources: Reuters, AP, BBC, The New York Times, Just Security — all stories
reported 24 November 2026.

## How it was made

The image was drawn programmatically with Python (Pillow) from a script
kept by the author; the finished PNG is bundled in this repository.
`main.py` simply copies it to `/output/entry.png`, so it is deterministic
(identical bytes on every run) and makes no network requests.

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## License

MIT — see `LICENSE`.
