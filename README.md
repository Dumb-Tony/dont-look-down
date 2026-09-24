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

## Rigged 3D character

The playable climber is now a real skinned 3D mesh, built in Blender through Higgsfield 3D Jutsu. Its 50-bone hierarchy includes spine, clavicles, arms, wrists, individual fingers, hips, legs and feet. Weighted sleeve and trouser vertices deform across joints; the old flat body-part sprites are no longer rendered. The accepted teal jacket / orange helmet design remains the visual reference.

Arm IK drives the skeleton from the physical fingertip targets. The wrist is solved behind the hand rather than placed on the rock. The mesh uses real-time lighting and fabric textures sampled from the generated atlas. This is a stylized base rig, with simpler geometry and surface detail than the reference image; the cliff and gameplay remain 2D.

Editable source: `assets/character/climber.blend`; portable rig: `assets/character/climber.glb`. `src/character3d.js` contains the renderer and IK, and `scripts/build_climber.py` records the Blender construction. Run `npm ci` then `node scripts/build_character.cjs` to embed the renderer and model in the standalone HTML. WebGL2 is required to render the character; playing still requires no network requests or separate runtime files.

## Visual direction

Higgsfield-generated sandstone fills the close cliff view, with detailed fissures, mineral grain, golden-hour lighting, and an atmospheric canyon background. Small authored crack patches replace the separate block-shaped holds. Aim along a patch and release: the hand plants at that position on the seam, rather than snapping to its center. Grip seams are thin, solid dark lines; a text cue confirms a usable edge while reaching.

The grip patches and resting surfaces remain authored; decorative cracks are not all climbable, and the game does not infer grip quality from image pixels. Route readability needs human playtesting. The 3D character is rendered into the existing cliff scene; the environment remains a painted 2D surface.

Generated source PNGs, encoded WebPs, and provenance are in `assets/higgsfield/`. Run `python scripts/embed_assets.py` with Pillow to rebuild the embedded pack. The standalone HTML includes all images, the model and the 3D renderer, and works offline.

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

Runtime dependencies are embedded in the HTML. Optional regression tooling requires Node, Playwright, and installed Microsoft Edge: run `node tests/playtest.cjs` with Playwright available, or set `PLAYWRIGHT_MODULE` to its module path. Set `PLAYTEST_URL` to test a deployed copy instead of the local file. Screenshots are generated into `tests/` and excluded from Git.

## Finding your first grip

The starting edge is marked beside the climber's head. Hold the left mouse button, move onto that edge, then release. Look closely for solid dark seams in the cliff. Their appearance stays the same while holding either mouse button; the text cue confirms reachability. The first-grip label disappears once you catch. The first two catches are also checked using screenshot-selected pixel positions (`tests/discovery.cjs`), alongside the complete route replays.

## Character articulation

The character's torso is masked to remove baked-in duplicate sleeves. Rebalanced head/body/leg proportions and separate shoulder, elbow, wrist and fingertip joints make the articulated silhouette more coherent. Grips and pointer targets correspond to fingertips; the hand sits between the wrist and the rock instead of extending beyond the contact. Total reach remains 46 units.
