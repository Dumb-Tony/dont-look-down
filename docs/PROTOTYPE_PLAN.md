# Don't Look Down: first build milestone

## M0 — repository and design
Own Git repository, focused GDD, standalone browser entry point plan, playtest log, and sharing guide.

## M1 — playable core slice
1. Create index.html with embedded styles, code, controls, pause, and restart.
2. Implement the smallest readable scene: One short vertical scaffold with alternating holds, a safe rest platform, an optional gap shortcut, and lower catch surfaces. Start within reach of the first holds; reach the top platform.
3. Implement consistent physical response: Body mass with gravity, constrained hand reach, one-hand swing, and increased two-hand stability. Releases preserve momentum. Catch attempts need visible reach feedback and predictable rules. Feet may assist automatically on platforms.
4. Add objective detection: Reach the top and settle safely. Verify each hand can hold independently, unreachable grabs fail clearly, a release leads to a real fall, and at least one lower hold or platform allows recovery and continued climbing.
5. Complete a success route and a recovery route, and inspect browser errors and resizing.
6. Commit a playable baseline and document controls, known simplifications, and checks actually performed.

## Scope gate
No campaign, progression economy, networking, asset pipeline, or dependency-heavy framework. Do not substitute a generic movement demo for the central mechanic. If a feature is too risky, document the reduction and preserve the core hypothesis.

## Later sharing milestone
Use this repository's own remote and static hosting; follow the parent project's standing instructions when shipping. Keep published contents limited to this game. Record the verified public URL and commit in README. First request prepares for later external testing; never report a public link before deployment succeeds.

## M1 outcome — 14 September 2026

Implemented and verified locally. Main ascent, fall/lower-hold recovery, and rest/gap recovery all finish on the upper deck through browser input replays. Pause, restart, resizing, independent hands, unreachable grabs, and two-anchor pulling are checked. See PLAYTEST.md for actual evidence and limits. Human playtesting remains the next validation gate.

## Control revision — 14 September 2026

Replaced toggle grips with hold-to-move/release-to-grip, shortened arms with fixed limb segments, and re-spaced the routes. Full mouse-only ascent and recovery routes pass. See current GDD and PLAYTEST for the superseding control rules and actual checks.

## Visual milestone — close cliff view

Implement a closer third-person camera and cliff art, retaining the accepted mouse controls. Replace ring markers with rock lips and aimed-only edge feedback. Re-run full success/recovery routes because zoom changes pointer-to-world mapping. Defer continuous rock-surface grip discovery to a later milestone.
