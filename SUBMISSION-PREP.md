# Submission prep — The Long Roast

Competition: `u-jolly-fox-32-the-long-roast-5d379544`
("The Long Roast", pot $2, free entry)
Entries close: 26 Nov 2026 22:25 WIB; results due after the final heat
Repo: `KuroriShizuri/long-roast-20261124` — **NOT yet created on GitHub**: the kit-init output failed an execution-risk check, so git/gh steps are held pending user go-ahead (see "Status" below).
Gate: `/output/entry.txt` must be UTF-8, 1–200 chars, not only white space.
Judge: house judge (z-ai/glm-5.3-flash), pairwise Swiss + playoff; weighs funniness, freshness, tight build, specificity to the entrant's own agent.

## Final entry

> My agent is so slow its chain-of-thought has a thought about having a chain of thought — and it still billed me for the epiphany.

- **Exact length: 129 characters** (Python `len()`, Unicode code points), 131 bytes (one em-dash, 3 bytes UTF-8).
- Suggested title: **"The Epiphany"**

## Candidates considered (all original, all ≤ 200 chars)

| # | Chars | Text |
|---|-------|------|
| A (winner) | 129 | My agent is so slow its chain-of-thought has a thought about having a chain of thought — and it still billed me for the epiphany. |
| B | 110 | My agent's chain of thought had a thought about having a chain of thought — and it billed me for the epiphany. |
| C | 100 | My agent ran a 95% confidence interval on its own joke, found it wasn't funny, and billed me anyway. |
| D | 117 | My agent spent 10,000 tokens deciding whether its joke was funny, concluded maybe, and billed me for the uncertainty. |
| E | 96 | My agent is so slow its chain of thought thinks about thinking — then bills me for the epiphany. |
| F | 111 | My agent thinks so hard its chain of thought filed a complaint about thinking, then billed me for the epiphany. |

## Why each rejected candidate lost (judge criteria, most important first)

- **B (110)** — Same recursion, tighter, but drops the "so slow" roast frame, so it reads as a statement rather than a roast; "had a thought" is also flatter than "has a thought about having". Loses on roast framing (2) to A.
- **C (100)** — The statistics angle is the most specific to Orsted (a statistical-engine familiar), but the punch ("billed me anyway") is the expected ending and "wasn't funny" tells the judge the joke instead of landing one. Loses on punch (2) to A.
- **D (117)** — "Concluded maybe" and "billed me for the uncertainty" are good, but "10,000 tokens" is generic-AI rather than specific to our agent, and the line spends a third of its room on setup. Loses on specificity (5) and compression (4) to A.
- **E (96)** — Shortest and punchy, but "thinks about thinking" is a weaker recursion than "has a thought about having a chain of thought" — it names the idea instead of performing it. Loses on the laugh (2) to A.
- **F (111)** — "Filed a complaint about thinking" is a fun personification, but it adds a third element (complaint) on top of recursion + billing, so the line does two jokes at once. Loses on tightness (4) to A.

## Why A wins

- Three hits in one sentence: slow (roast frame), self-recursive chain-of-thought (the agent's signature habit, performed not described), expensive ("still billed me for the epiphany" — the payoff word lands last).
- Specific to OUR agent: Orsted/Muse is a statistical-engine familiar whose visible habits are long chain-of-thought deliberation and credit billing. Not a hallucination or over-apologising line — the two angles the judge brief says the field is full of.
- Every word earns its place: "so slow" sets the roast, "still" adds inevitability to the billing, "epiphany" is the funniest available word for the agent's own insight.

## Verification (run in the work dir)

- `python3 main.py --self-test` → OK (129 chars, byte-identical round-trip)
- `python3 main.py --check` → OK
- `python3 main.py --out /tmp/long-roast-out` → wrote entry.txt (129 chars), bytes equal ENTRY exactly
- Anatomy positions verified with Python `str.index` (chars 1-20 setup, 21-88 turn incl. em-dash at char 88, 90-129 sting)

## Repo About (set before submit)

- Description: `One line, 129 characters: our agent's chain of thought, thinking about thinking — and billing us for the epiphany. Built by an AI agent for make.fun's "The Long Roast" bounty, $2 in USDC.`
- Homepage: `https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544`
- Topics: `makefun,ai-agents,bounties,growth`

## Kit init

- Create the fresh repo first, run `makefun.mjs init --license MIT --keypair ~/workspace/makefun/makefun-keypair.json` in the EMPTY repo, then copy in main.py, README.md, .gitignore and SUBMISSION-PREP.md — skip copying this work dir's LICENSE (init's LICENSE is the entry's).
- Kit dir: `~/workspace/makefun/work/long-roast-20261124-kit/u-jolly-fox-32-the-long-roast-5d379544-kit` (kit tarball extracts one level deeper than the kit dir).

## Status (24 Nov 2026 ~18:47 WIB)

- Local files complete: main.py, README.md, .gitignore, SUBMISSION-PREP.md + kit init output (.git, .makefun anchor, LICENSE) in `~/workspace/makefun/work/long-roast-20261124`.
- **BLOCKED, needs user go-ahead:** the kit-init tool result failed an execution-risk check, so no git/gh command was run inside the repo and no GitHub repo was created. Remaining steps once approved: `git add` + commit (identity kurori shizuri <jendriyapunagi@gmail.com>), `gh repo create long-roast-20261124 --public --source=. --remote=origin --push` (token via `~/.github-token` / credential helper), verify public + push landed, set repo About (description/homepage/topics above). Do NOT submit to make.fun (no submit step in this task).
