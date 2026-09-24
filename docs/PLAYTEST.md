# Playtest log

## 2026-09-14 — first playable baseline

Build: first playable implementation commit (see Git history). Platform: Windows, Microsoft Edge Chromium, headless Playwright. Input: real pointer movement, mouse button events, and keyboard events with a controlled browser clock. No player teleportation or writable test controls. Read-only observations expose physics state for assertions.

### Completed automated checks

- Full main route: holds 0 through 14, alternating hands, pulling and releasing the lower grip. Released above the upper deck and settled at body y=172 / deck y=195. Completion registered after 0.75 seconds stable on deck. Roughly 27 seconds of simulated climbing including extra grip-constraint checks.
- Each hand held independently; both held together. Distinct two-hand anchors respected both length constraints during extended pulling.
- An aimed but unreachable second hold failed clearly with OUT OF REACH and no grip acquired.
- Real fall: released at hold 4, advanced 450 ms, confirmed increasing downward position and velocity, caught lower hold 3, then climbed to completion.
- Rest recovery: released after reaching hold 6 and landed on the rest deck at body y=897 with both hands free. Continued via amber gap hold 15 and rejoined hold 7, then completed the remaining ascent. Directional leaning was required for the gap transfer.
- Left and right mouse buttons each acquired the intended independent grip; Q/E also verified.
- Pause froze body position across 1.2 simulated seconds. Resume continued. Focus loss paused. Restart cleared completion and returned to base camp.
- Resized from 1280×900 to 600×750; pointer targeting still acquired the first hold. Resized back and reset successfully.
- No uncaught browser errors across the replay.
- Visually inspected start, narrow layout, and summit screenshots. Controls, hold rings, reach text, scaffold, and completion card remained legible at the inspected sizes.

### Issues found and fixed

Pulling on two different anchors originally shortened both constraints beyond a geometrically possible configuration. Retraction now stops before the combined arm lengths become shorter than the anchor spacing. A regression asserts that neither constraint is exceeded.

### Actual limitations

These checks are automated input replays and screenshot review, not manual human play or subjective feel testing. Only Edge Chromium was tested. Touch input, very small phones, assistive-technology gameplay, Firefox, and Safari remain untested. The narrow layout is for desktop window resizing, not a claim of mobile playability. The gap route is a deliberate alternative around the left hold; its speed advantage has not been measured.

The body is a point mass with visual limbs. Arms constrain maximum distance from a common body center; feet land automatically on one-way platforms. Scaffold struts are scenery. There is no arm collision, grip fatigue, dynamic hold quality, or arbitrary release boost. Two hands add damping. Frame catch-up is bounded and excess background time is discarded. No camera shake is used.

### Next external session

Give the public link to a new desktop player without coaching. Observe the first 30 seconds, time to first grip, whether they discover releasing the lower hand, first summit, and one intentional fall recovery. Ask: What caused the fall? Did the reach indicator predict the catch? Did both hands feel reliable? Did you want another attempt? Use that evidence to tune hold spacing and pull speed before adding more world.

### Public deployment verification

GitHub Pages build 34815225070 completed successfully for implementation commit `1b7eef84970146be6961372354a3311af16a462b`. Public address: https://dumb-tony.github.io/dont-look-down/ .

Re-ran the complete browser input replay against that HTTPS address on 14 September 2026. Main summit, falling catch on lower hold then summit, rest landing / gap route / summit, mouse and keyboard grips, pause, focus loss, reset, narrow resize, and zero uncaught browser errors all passed. Public ascent settled at y=172 after about 27 seconds of simulated climbing. This verifies the deployed game, not merely the repository or a local preview.


## 2026-09-14 — hold-to-move control revision

User-requested revision: hold left/right mouse to free and position that hand, release to grip; replace long stretchy arms. Current arms use two fixed-length 29-unit bones, shoulder-based reach capped at 58 units, and elbow bending. Holds and decks were repositioned, so the complete routes were re-tested. Auto-pull replaces W.

Local automated Edge Chromium replay passed:

- Entire alternating ascent using mouse buttons only, then stable summit completion.
- Press immediately frees a planted hand; moving onto a ring does not grip until button release. Every transfer asserts this ordering.
- Unreachable release fails with OUT OF REACH and no planted hand.
- Release from hold 4 produces an actual fall; after 230 ms the player catches lower hold 3 with the right hand, then finishes the whole ascent.
- Fall to the rest shelf, both hands free; continue through amber hold 15, lean into hold 7, and finish the ascent.
- Simultaneous left/right presses move both hands; releasing right leaves left moving. Both releases clear their own movement independently.
- Q/E hold/release alternatives, two-hand constraint distances, and a far-away pointer that cannot extend a free arm past 58 units.
- Pause while dragging freezes the body, clears active movement, and creates no phantom grip on release. Focus loss during right-hand movement also clears it safely. Restart clears state.
- 600×750 resizing still permits a hand placement; restored 1280×900 successfully. No uncaught browser errors.
- Screenshots of short bent arms, maximum pointer reach, narrow layout, and summit were visually reviewed.

These remain automated input replays and screenshot review, not human feel testing. Next external check: whether press-to-free and release-to-grip feels intuitive, whether the shorter reach reads correctly, and whether automatic body pull feels responsive without feeling forced.

Public verification: Pages build 34818716090 succeeded for `e236100cba79a6c085f59e23565f4b10dd8d4d04`. The complete revised replay then passed against https://dumb-tony.github.io/dont-look-down/ : main summit, lower-hold recovery and summit, rest/gap recovery and summit, input ordering, chorded buttons, keyboard alternatives, capped hand reach, pause/blur/reset, resizing, and zero uncaught browser errors.


## 2026-09-14 — close cliff visual pass

Local Edge Chromium input replay passed the complete main ascent, lower-hold recovery and summit, rest shelf/gap route and summit, press/release ordering, simultaneous buttons, keyboard equivalents, capped arm reach, pause, focus loss, restart, and 600×750 resizing with no uncaught browser errors. The camera now renders at 3.4 scale on 1280×900 (previously 1.15); input replays still target world holds via the actual screen transform.

Visually inspected the new desktop close-up and narrow-window screenshots. Confirmed the larger climber, articulated arms, cliff facets, ledges, valley depth, compact controls, and removal of ring/dotted-route markers. A narrow-window review revealed the bottom of the cliff silhouette, which was extended below the viewport. No physical hold, platform, reach, or gravity changes were made in this art pass.

Limitations: screenshot review and automated routes do not establish whether the art direction or camera feels right to a person. Rock grip locations remain authored points with the same catch tolerance, visually presented as rock lips. Continuous surface searching, irregular grip regions, rock quality, and 3D camera depth are deferred.


## 2026-09-16 — color, material, and lighting pass

Automated Edge Chromium local replay passed the full ascent, lower-hold recovery and summit, rest/gap recovery and summit, independent and simultaneous mouse inputs, keyboard alternatives, arm reach bounds, pause/focus loss/reset, resizing, and zero uncaught browser errors after the initial material update. Subsequent changes only refined fading shadow shapes, decorative ledge silhouettes, sediment seams, and vegetation; a separate visual smoke run reported no browser errors.

Reviewed desktop screenshots of both material iterations. Replaced overly hard rectangular shadows with fading shadows, broke up regular horizontal seams, and gave shelf undersides irregular silhouettes and surface grain. Physics geometry remains exactly the same. The visual check sampled 119 frame intervals in headless Edge at 1280×900: median 5 ms, 95th percentile 5.2 ms on this machine. This is a headless timing observation, not a promised user framerate or a hardware-wide benchmark.

The scene remains stylized procedural 2D. These are automated input checks and screenshot reviews; human judgement of the art direction remains with the user. Public-route verification follows deployment.


## 2026-09-17 — option B character and human proportions

Automated local Edge replay completed the whole main ascent; released, fell, caught lower hold 3 and finished; landed on the rest shelf, crossed the optional gap, and finished. It also passed mouse press/release ordering, simultaneous buttons, keyboard alternatives, shoulder constraint bounds, capped free-hand reach, pause during drag, focus loss, reset, and narrow-window input. Zero uncaught browser errors.

The first gap-route replay failed after shortening the arms, proving the previous transfer was no longer reachable. The gap lip was moved inward and slightly higher; a fresh full replay then passed every route and check. Rest landing now verifies the new 60-unit sole offset. Body and level geometry changes were exercised through pointer events, not teleports.

Inspected desktop beginning/mid-climb and 600×750 screenshots for arm proportions, head/torso/leg silhouette, grip connection, boot placement, and UI overlap. Removed prominent spherical elbow/knee overlays and replaced straight jacket marks with curved fold shading. Visual smoke check reported no errors; headless frame samples were roughly 5 ms median and 5.1 ms at the 95th percentile on this machine. These are automated checks and screenshot review, not a manual feel test or a general performance guarantee.

Option B is a visual target. Current implementation is shaded 2D, not the generated concept's full 3D fidelity. Human feedback on the new proportions and material treatment is still needed.


## 2026-09-22 — Higgsfield artwork and fissure grips

Local automated Edge replay passed the complete main ascent, falling catch and continued ascent, rest landing and gap route through the summit. Independent/chorded mouse controls, Q/E, reach limits, pause/blur/reset, narrow resizing, and uncaught-error checks passed. A new off-center seam catch checks that the anchor follows the chosen position (within one screen pixel of pointer rounding) and remains fixed when the pointer moves.

Reviewed sharp-cliff screenshots at the start and mid-climb, and corrected the atlas torso placement to join the shoulder artwork. A subsequent visual smoke check reported no errors and sampled approximately 5 ms median / 5.1 ms 95th-percentile RAF intervals in headless Edge. This is not a general performance guarantee. Generated assets now load before simulation begins.

These are automated input replays and visual screenshot inspection, not a human feel test. Human testing is especially important for finding the subtler authored fissures; many decorative image cracks remain noninteractive. Public verification is recorded after deployment.

Public verification: Pages deployment 35814447234 succeeded for 6948a8079f400da776bea3470151de14cb3c64d8. The complete replay passed on https://dumb-tony.github.io/dont-look-down/ with all ascent/recovery, seam-anchor, input, pause/reset/resize and browser-error checks passing. Public HTML matched the local build after line-ending normalization.


## 2026-09-24 — starting grip discoverability repair

User reported the game was unplayable because no starting grip could be found. The prior full-route tests knew hold coordinates, so they proved reachability without proving discoverability. The initial fissure was almost invisible and overlapped the character; eligibility feedback required finding it first.

Moved the first grip left and 8 units higher, outside the starting helmet silhouette. Added a persistent first-grip label and edge accent until the first successful catch. While a hand button is held, every edge reachable by that hand gets a contrasting seam accent, before pointer targeting; accents render over the character. Unselected fissures have stronger rock shading. No automatic grips or longer arms were added.

Local Edge checks: full ascent, lower-catch recovery/ascent, rest/gap recovery/ascent, input/constraint/pause/blur/reset/resize checks all passed with zero browser errors. Inspected start and reaching screenshots. Added tests/discovery.cjs, which clicks the first two edges at pixel locations chosen from screenshots without using hold coordinates or the screen-transform helper; both catches passed. This is screenshot-guided automated input, not a human feel test. Visual smoke timing remained approximately 5 ms median and 5.1 ms p95 in headless Edge.
