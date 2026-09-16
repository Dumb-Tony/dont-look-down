# Don't Look Down

A standalone 2D physical climbing prototype: two independent hands, body momentum, and falls you can recover from.

## Play

**[Play Don't Look Down](https://dumb-tony.github.io/dont-look-down/)** — public deployment verified on 14 September 2026.

You can also open `index.html` directly in a desktop browser. No installation, build, network requests, or external assets are required.

[Source repository](https://github.com/Dumb-Tony/dont-look-down).

- **Hold left mouse:** release the left hand and move it with the pointer.
- **Hold right mouse:** release the right hand and move it with the pointer.
- **Let go over a reachable rock edge:** that hand grips and stays planted.
- **Q / E:** keyboard alternatives with the same hold-to-move, release-to-grip behavior.
- **A / D / Left / Right:** optional lean or walk on a platform.
- **P / Escape:** pause. **R:** restart. Losing focus pauses automatically.

The body pulls up naturally after a grip; W is no longer needed. Start by holding left mouse, moving to the first rock edge, and letting go. Place the right hand above it. Hold left again to free the lower hand and move it upward. Continue alternating. Aim at the top lip of a projecting rock flake. Its edge gets a subtle light highlight when reachable, or a muted rust highlight when too far; there are no ring markers or dotted route. Letting go away from a rock edge leaves the hand free. Settle on the summit ledge for three quarters of a second to finish.

The left rest shelf supports your weight with no grips. Its right edge offers an optional gap transfer to the rock lip to the right. A failed transfer can fall onto a lower hold or deck; restarting is optional.

## Visual direction

Close third-person cliff view, roughly three times the original desktop zoom. The golden-hour art pass adds warm sandstone grain and mineral bands, cool shaded crevices, fading cast shadows, olive lichen and ferns, layered blue mountain ridges and mist, and drifting sunlit flecks. The climber wears a teal jacket with fabric seams, a shaded orange helmet, a harness, and metal gear. This is an incremental art pass. Grab spots still use the tested fixed locations underneath the rock shapes; this is not yet a continuous surface with dynamically discovered grip quality. The next step is less regular rock geometry and judging usable features from their shape.

## Status and limits

First playable slice implemented and verified locally and on GitHub Pages on 14 September 2026. Automated browser input replays completed an ascent, a lower-hold recovery followed by an ascent, and a rest-platform recovery through the gap route to the summit. These are automated replays, not human feel tests. See `docs/PLAYTEST.md` for evidence and remaining questions.

Short arms with fixed-length upper/lower segments and bending elbows. Holds and decks have been repositioned for a 4.74 m ascent within that reach. Simplified point-mass physics with shoulder-based unilateral arm constraints, gravity, momentum-preserving releases, extra two-hand damping, and automatic feet on one-way decks. No fatigue, jumping, equipment, audio, ragdoll collisions, or touch controls. Desktop pointer play is supported; a keyboard provides optional lean, shortcuts, and alternate hand inputs. The 2D slice does not establish first-person depth perception or fear of height.

## Project map

- `index.html` — complete game with embedded CSS and JavaScript
- `docs/GDD.md` — design, implemented rules, and boundaries
- `docs/PROTOTYPE_PLAN.md` — acceptance criteria
- `docs/PLAYTEST.md` — actual evidence and external test prompts
- `docs/SHARING.md` — publication details
- `tests/playtest.cjs` — browser input regression replay; no game-state mutation

The game has no dependencies. Optional regression tooling requires Node, Playwright, and installed Microsoft Edge: run `node tests/playtest.cjs` with Playwright available, or set `PLAYWRIGHT_MODULE` to its module path. Set `PLAYTEST_URL` to test a deployed copy instead of the local file. Screenshots are generated into `tests/` and excluded from Git.
