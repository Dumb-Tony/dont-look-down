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
Hold left/right mouse to release and position that hand; release the button over a reachable hold to grip. Planted hands remain fixed. Q/E provide the same press/release behavior. The body pulls up automatically; A/D optionally lean. Suppress the browser context menu on the play surface. R explicitly restarts.

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

## Current slice — revised controls, 14 September 2026

User feedback: the original arms stretched comically far, and gripping should happen when the mouse button is released. The current input model implements exactly that hand lifecycle: press frees, held button moves the open hand with the pointer, release on a reachable ring plants it. Release elsewhere fails visibly and leaves the hand free. Both buttons work independently, including simultaneous presses. Q/E mirror the same lifecycle. Pause, focus loss, and restart clear active hand movements without creating a grip.

Each arm has two fixed 29-unit segments, bent by an elbow. Reach is capped at 58 units from that hand's shoulder, both visually and for grab eligibility. Holds and decks are closer together, with a 4.74 m main ascent, the rest shelf, lower catch decks, and the amber gap alternative retained. The body automatically retracts a planted arm toward 18 units of shoulder-to-hand distance, bending the elbow rather than shortening its bones. Removing the separate W pull command allows the complete main route to use only the mouse.

Physics retains the 120 Hz fixed step, bounded catch-up, gravity, one-hand swing, extra two-hand damping, and momentum-preserving release. Constraint feasibility accounts for the two distinct shoulders. Feet land automatically on one-way decks. A grip target is within 14 units of the pointer and no farther than the arm's 58-unit reach. No invisible out-of-reach snap or automatic grab while dragging is permitted.

The camera follows smoothly without shake. Pause, focus loss, restart, visible hand states, and stable upper-deck completion remain. Automated success and recovery routes pass with the revised input; human feel testing remains necessary.
