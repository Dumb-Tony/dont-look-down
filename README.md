# Don't Look Down

A standalone 2D physical climbing prototype: two independent hands, body momentum, and falls you can recover from.

## Play

**[Play Don't Look Down](https://dumb-tony.github.io/dont-look-down/)** — public deployment verified on 22 September 2026.

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

## Selected character direction

[Option B — stylized 3D reference](docs/art-direction/option-b.png) is the accepted visual target. The playable character uses a Higgsfield-generated transparent body-part atlas, articulated with the existing arm constraints. Adult proportions and 23-unit arm bones are retained. This is a 2D game using generated raster artwork, not a 3D character model.

## Visual direction

Higgsfield-generated sandstone fills the close cliff view, with detailed fissures, mineral grain, golden-hour lighting, and an atmospheric canyon background. Small authored crack patches replace the separate block-shaped holds. Aim along a patch and release: the hand plants at that position on the seam, rather than snapping to its center. A restrained highlight and message appear while probing a usable edge.

The grip patches and resting surfaces remain authored; decorative cracks are not all climbable, and the game does not infer grip quality from image pixels. Route readability needs human playtesting. The character atlas is articulated in Canvas, with simpler movement and depth than the visual reference.

Generated source PNGs, encoded WebPs, and provenance are in `assets/higgsfield/`. Run `python scripts/embed_assets.py` with Pillow to rebuild the embedded pack. The approximately 6.2 MB standalone HTML includes every runtime image and works offline.

## Status and limits

First playable slice implemented and verified locally and on GitHub Pages on 14 September 2026. Automated browser input replays completed an ascent, a lower-hold recovery followed by an ascent, and a rest-platform recovery through the gap route to the summit. These are automated replays, not human feel tests. See `docs/PLAYTEST.md` for evidence and remaining questions.

Short arms with fixed-length upper/lower segments and bending elbows. Holds and decks have been repositioned for a 4.81 m ascent within that reach. Simplified point-mass physics with shoulder-based unilateral arm constraints, gravity, momentum-preserving releases, extra two-hand damping, and automatic feet on one-way decks. No fatigue, jumping, equipment, audio, ragdoll collisions, or touch controls. Desktop pointer play is supported; a keyboard provides optional lean, shortcuts, and alternate hand inputs. The 2D slice does not establish first-person depth perception or fear of height.

## Project map

- `index.html` — complete game with embedded CSS and JavaScript
- `docs/GDD.md` — design, implemented rules, and boundaries
- `docs/PROTOTYPE_PLAN.md` — acceptance criteria
- `docs/PLAYTEST.md` — actual evidence and external test prompts
- `docs/SHARING.md` — publication details
- `tests/playtest.cjs` — browser input regression replay; no game-state mutation

The game has no dependencies. Optional regression tooling requires Node, Playwright, and installed Microsoft Edge: run `node tests/playtest.cjs` with Playwright available, or set `PLAYWRIGHT_MODULE` to its module path. Set `PLAYTEST_URL` to test a deployed copy instead of the local file. Screenshots are generated into `tests/` and excluded from Git.

## Finding your first grip

The starting edge is marked beside the climber's head. Hold the left mouse button, move onto that edge, then release. Whenever you hold either hand's button, reachable edges light up before you aim at them. These are temporary discovery cues; the first-grip label disappears once you catch. The first two catches are also checked using screenshot-selected pixel positions (`tests/discovery.cjs`), alongside the complete route replays.
