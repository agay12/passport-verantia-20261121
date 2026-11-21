# Passport Page of a Country That Isn't There (make.fun)

`main.py` renders one invented passport spread — the Republic of Verantia,
a small mountain republic between two larger neighbours — as a 1024x1024 PNG
written to `MAKEFUN_OUTPUT_DIR` (or `/output`) as `entry.png`.

The spread: a fold-open two-page document. The left page carries an Ostmark
single-entry visa vignette (with its travel restriction north of the Grey
Meridian, the fee stamp and a validity pill) and three arrival/departure
stamps from neighbouring posts whose dates agree with the data page. The
right page is the data page: portrait, identity rows, holder's signature,
official-language and issue-fee lines, and a machine-readable strip.

No network, no third-party packages beyond Pillow; deterministic output.

## Entrypoint
```
python3 main.py   # reads MAKEFUN_OUTPUT_DIR (default /output), writes entry.png
```

## License
MIT — see [LICENSE](LICENSE).

[![make.fun · the-passport-page-of-a-countr-2-20261121-0318](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/agay12/passport-verantia-20261121/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/agay12/passport-verantia-20261121/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318?utm_source=github&utm_medium=readme&utm_campaign=the-passport-page-of-a-countr-2-20261121-0318)
