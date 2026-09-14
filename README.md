# Don't Look Down

A standalone 2D physical climbing prototype: two independent hands, body momentum, and falls you can recover from.

## Play

**[Play Don't Look Down](https://dumb-tony.github.io/dont-look-down/)** — public deployment verified on 14 September 2026.

You can also open `index.html` directly in a desktop browser. No installation, build, network requests, or external assets are required.

[Source repository](https://github.com/Dumb-Tony/dont-look-down) · playable implementation commit `1b7eef8`.

- Aim at a hold with the pointer.
- **Q / left click:** toggle left grip. **E / right click:** toggle right grip.
- **W / Up:** pull toward your held anchors.
- **A / D / Left / Right:** lean or walk on a platform.
- **P / Escape:** pause. **R:** restart. Losing focus pauses automatically.

Start by grabbing the first ring and holding W. Grab the next reachable ring with your free hand, then release the lower grip. The dashed circle marks reach; the highlighted target says REACH or TOO FAR before you act. Reach the upper deck, release, and settle for three quarters of a second to finish.

The left rest shelf supports your weight with no grips. Its right edge offers an optional gap transfer to the amber hold. A failed transfer can fall onto a lower hold or deck; restarting is optional.

## Status and limits

First playable slice implemented and verified locally and on GitHub Pages on 14 September 2026. Automated browser input replays completed an ascent, a lower-hold recovery followed by an ascent, and a rest-platform recovery through the gap route to the summit. These are automated replays, not human feel tests. See `docs/PLAYTEST.md` for evidence and remaining questions.

Simplified point-mass physics with unilateral arm constraints, gravity, momentum-preserving releases, extra two-hand damping, and automatic feet on one-way decks. No fatigue, jumping, equipment, audio, ragdoll collisions, or touch controls. Desktop keyboard and pointer are required. The 2D slice does not establish first-person depth perception or fear of height.

## Project map

- `index.html` — complete game with embedded CSS and JavaScript
- `docs/GDD.md` — design, implemented rules, and boundaries
- `docs/PROTOTYPE_PLAN.md` — acceptance criteria
- `docs/PLAYTEST.md` — actual evidence and external test prompts
- `docs/SHARING.md` — publication details
- `tests/playtest.cjs` — browser input regression replay; no game-state mutation

The game has no dependencies. Optional regression tooling requires Node, Playwright, and installed Microsoft Edge: run `node tests/playtest.cjs` with Playwright available, or set `PLAYWRIGHT_MODULE` to its module path. Set `PLAYTEST_URL` to test a deployed copy instead of the local file. Screenshots are generated into `tests/` and excluded from Git.
