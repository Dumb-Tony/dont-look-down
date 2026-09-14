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
