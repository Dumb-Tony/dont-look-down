"""Encode Higgsfield source PNGs as WebP and embed the asset pack in the standalone game."""
from pathlib import Path
from PIL import Image
import base64,json
root=Path(__file__).resolve().parent.parent
names={'cliff':'cliff-4k','valley':'valley','atlas':'climber-atlas'}
assets={}
for key,name in names.items():
 image=Image.open(root/'assets'/'higgsfield'/(name+'.png'))
 out=root/'assets'/'higgsfield'/(name+'.webp')
 image.save(out,format='WEBP',quality=90,method=6)
 assets[key]='data:image/webp;base64,'+base64.b64encode(out.read_bytes()).decode()
p=root/'index.html';s=p.read_text(encoding='utf-8');a=s.index('const assetSources=');b=s.index(';\nconst art=',a)
s=s[:a]+'const assetSources='+json.dumps(assets,separators=(',',':'))+s[b:];p.write_text(s,encoding='utf-8')
print('Embedded bytes:',sum((root/'assets'/'higgsfield'/(name+'.webp')).stat().st_size for name in names.values()))
