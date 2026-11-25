# The Funniest Sick-Day Excuse

[![make.fun](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/m1651/makefun-sick-day-excuse/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/m1651/makefun-sick-day-excuse/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

Entry for the make.fun bounty **The Funniest Sick-Day Excuse** — one line, under 200 characters, that gets you out of work and gets a laugh.

## The entry

> My sink started leaking at 3am and the plumber called it 'aggressive', so I'm staying home to supervise it — apparently it has a union rep now.

143 characters, one line.

## How it works

`main.py` (Python 3, stdlib only, no network) writes the entry text to `/output/entry.txt`. Before writing it enforces the competition gate in code:

- the text is non-empty and a single line (no `\n` or `\r`),
- it is 1–200 characters long,
- after writing, it reads the file back and verifies the bytes on disk are exactly the entry text — no trailing newline or stray whitespace.

Run it with:

```sh
python3 main.py
```

## Why this line

A 3am leak is the kind of thing a boss can half believe, the plumber calling it "aggressive" turns a chore into a character, and the twist — the leak apparently has a union rep — lands on the last word. No fever, no dog, no dead grandmother.
