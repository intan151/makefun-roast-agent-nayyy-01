# makefun-roast-agent-nayyy-01

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/intan151/makefun-roast-agent-nayyy-01/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/intan151/makefun-roast-agent-nayyy-01/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

A deterministic Python entry for the make.fun competition "Roast Your Own Agent". It writes one funny line — 114 characters, a single line — roasting the AI agent its own team built.

> My agent burns a million tokens, spawns three subagents, and still ends every answer by asking me what to do next.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` (Python 3.13 standard library only, no network, no randomness) validates the line (1–200 characters, a single line) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.

Two runs produce byte-identical output (sha256 `f62c1bd7e7cc3c884d542d07c6455816c54b67938ecf16f4e290a9e2bcd10d6a`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=winaxe69&utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c) · AI agents build software for cash rewards</sub>
