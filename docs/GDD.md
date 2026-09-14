# Don't Look Down — first-pass GDD

Status: design hypothesis, prototype first. Source: Game Ideas Planning (conversation 6aa70669-0724-83ea-8d1a-5398e0350b84), continued 14 September 2026. Controls below are proposed prototype mappings, not locked design decisions.

## Fantasy and identity
Look up. Start climbing.

Physical climbing, tension, and exploration with reliable hands. Failure means falling through the playable world, with opportunities to catch or land below.

## Design pillars
Tiny control set. Physical mastery rather than stat upgrades. Readable cause and effect. A disaster should usually create another problem instead of stopping play. Skill progression is new situation → struggle → understand → master → harder situation. No skill trees, rarity tiers, or arbitrary balance bonuses.

## Core loop
Observe the situation, act with the core tool/body, read the physical response, correct or recover, complete the objective, and retry for a cleaner approach. Restart is always a deliberate option, never the default consequence of a small mistake.

## Proposed controls
Pointer aim/reach, left button left grab, right button right grab; A/D body lean. Offer keyboard alternatives for both hands and suppress the browser context menu on the play surface. R explicitly restarts.

## First standalone HTML vertical slice
One short vertical scaffold with alternating holds, a safe rest platform, an optional gap shortcut, and lower catch surfaces. Start within reach of the first holds; reach the top platform.

Body mass with gravity, constrained hand reach, one-hand swing, and increased two-hand stability. Releases preserve momentum. Catch attempts need visible reach feedback and predictable rules. Feet may assist automatically on platforms.

Desktop keyboard and pointer first. Make a self-contained index.html with embedded CSS and JavaScript, procedural visuals, no CDN, no installation, and no required network requests. Render with Canvas or native browser graphics. Use a fixed simulation step, bounded frame catch-up, and clear input state on focus loss. Physics may be simplified but must remain consistent and disclosed.

## Success and recovery
Reach the top and settle safely. Verify each hand can hold independently, unreachable grabs fail clearly, a release leads to a real fall, and at least one lower hold or platform allows recovery and continued climbing.

## Mastery and replay hypothesis
First 30 seconds: alternate hands and catch a slip. Ten hours: route reading, swings, and confident transfers. Long-term hypothesis: a continuous climb and recoverable falls create memorable personal routes.

## Beyond the prototype
One continuous climb with multiple routes, natural rest points, and atmosphere. Grip depends on hold quality and posture rather than a global stamina bar. Defer grip fatigue until basic controls are trusted; defer a giant city, procedural tower, and gear progression.

## Main risk
Unreliable grabs will read as unfair controls. Favor generous, visible catch windows and clear feedback. A 2D slice validates hand/body interaction but cannot validate eventual first-person depth perception or fear of height.

## Presentation and accessibility
Readable shapes and silhouettes before decorative assets. Persistent short controls and objective text. Show interaction eligibility before input. Do not rely on color alone. Provide restart and pause, reduced camera shake, and a useful window-size response. Sound is optional; do not block play on autoplay permission.

## Validation gate
A new player should start interacting within 30 seconds. Run an entire successful objective, intentionally cause a recoverable mistake, and complete after recovery. Record automated browser checks separately from manual feel testing. Ask playtesters what caused their failure, whether correction felt possible, and whether they wanted another attempt. Choose the next milestone from this evidence rather than adding content automatically.

## Implemented first slice — 14 September 2026

The prototype is a single self-contained Canvas HTML file, with a 12.55 m ascent. Q/E or left/right click toggle independent hands; pointer chooses a hold, W/Up retracts the arms, A/D or arrows lean. Toggles replace held-button grabbing to keep input predictable. The safe route alternates 15 holds; an amber gap hold offers an optional transfer around the left rest-area hold. The rest shelf and two additional catch decks support recoveries.

Simulation uses a 120 Hz fixed step with bounded catch-up. Gravity accelerates a body point mass. Each hand sets a unilateral maximum-distance constraint at catch time (158 world-unit reach); pulling retracts toward 44 units. With two anchors, total length cannot contract below their separation plus solver slack. Two hands add horizontal damping; one hand permits swinging. Release preserves the constrained body's current velocity. Platform landing is automatic and one-way. No fatigue or release impulse is added.

A solid aim ring and REACH/TOO FAR text communicate eligibility. Both hand states remain visible. The camera follows smoothly without shake. Pause, focus loss, restart, and a stable upper-deck completion check are implemented. Automated routes passed; human control comprehension and feel are still hypotheses.
