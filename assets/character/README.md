# Rigged climber asset

Higgsfield 3D Jutsu project: https://higgsfield.ai/3d-jutsu/303d3c6a-8a99-4434-b1c7-ea8cb64b77ce
Committed revision: 2. Blender 5.2. 50 bones, 51 skinned mesh pieces, one shared humanoid skeleton. All geometry and weights are editable in climber.blend. climber.glb is the portable in-game asset. climber.png is the inspected studio render.

This character was modeled through Blender scene tools; it is not the output of an image-to-3D conversion. reference.png was generated in Higgsfield with GPT Image 2.5 (job 7cd000d6-a9c7-4206-8b5d-6f04db6aed31), using the existing climber atlas as the outfit reference. Prompt requested a complete normally proportioned adult climber in a rig-friendly A pose, teal jacket, orange helmet, navy trousers, ochre harness, black/ochre shoes and bare hands.

The construction is recorded in scripts/build_climber.py. Bone lengths are measured in metres and the game scales them by 62.5 world units per metre. Upper arm 0.336 m, forearm 0.304 m, hand approximately 0.096 m. Runtime IK uses the actual middle-finger end effector. The reference image is more detailed than the modeled asset; this is a stylized rigged foundation.

Runtime cloth maps sample the existing Higgsfield atlas; lighting, skinning and poses are rendered by the embedded Three.js renderer. No scene-builder service calls are required to play.
