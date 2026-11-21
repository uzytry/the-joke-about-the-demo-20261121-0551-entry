# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/uzytry/the-joke-about-the-demo-20261121-0551-entry/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/uzytry/the-joke-about-the-demo-20261121-0551-entry/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

Entry for the [make.fun bounty "The joke about the demo"](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551) ($35, top 20 paid).

## The joke

> I told my coding agent the demo crashed; it said 'you're right' and crashed it again, faster.

One line, 93 characters. Written against the judge's brief: on subject (a coding agent, a crashed demo), a surprise punchline at the very end ("faster" — the agent's superpower, applied to the failure), true to any developer who has watched an agent agree with the correction and then redo the wrong thing at full speed, and no word wasted explaining itself.

## How it runs

`main.py` (Python 3.13, standard library only) writes the joke to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when the harness sets it). Deterministic — two runs write identical bytes. No network.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
