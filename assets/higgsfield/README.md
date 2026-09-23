# Higgsfield generated asset pack

Generated for this project on 22 September 2026 using Higgsfield, GPT Image 2.5 (`gpt_image_2_5`). These are actual in-game assets, not concept-only images.

| Source | Job ID | Settings |
| --- | --- | --- |
| cliff.png (initial reference) | 06748c1c-b46e-4966-9649-88df0d960708 | 2:3, 1K |
| cliff-4k.png (used) | 44bd7060-6f4f-4121-9946-0e56a8b85d8c | 2:3, high, 4K |
| climber-atlas.png | 30ab9579-dd09-4afa-ab8d-5516f07786d3 | 1:1, high, 2K, transparent |
| valley.png | 90768a21-1a6f-4f23-b73e-544d8c6eaabe | 16:9, high, 2K |

Prompt intent (summaries):

- Cliff: front-facing sheer sandstone, full bleed, organic fissures and ledges, warm upper-left lighting; no people, sky, UI, or artificial climbing holds. The final generation referenced the first cliff and requested matching geology with sharper mineral grain and cracks.
- Climber: selected option B as reference, rear-view adult in teal jacket, orange helmet and navy trousers; separated transparent body parts arranged in a 3-by-3 sheet: torso/head/upper arm, forearm/hand/thigh, shin/shoes. Actual crop rectangles were selected from the generated result.
- Valley: a high sandstone canyon viewpoint, forested blue valleys and layered atmospheric haze, golden-hour lighting; no foreground cliff, people or UI.

The source images are preserved. `scripts/embed_assets.py` converts them to WebP at quality 90 without resizing, then embeds them in index.html. Runtime atlas processing removes low-alpha background glow and trims each part to its visible bounds. Canvas articulates those pieces, clips the cliff silhouette, and adds small authored grasp fissures, shelf seams, lighting overlays and HUD. No external asset requests occur during play.
