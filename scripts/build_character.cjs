const fs=require('fs');
const {buildSync}=require('esbuild');
const path=require('path');
const root=path.resolve(__dirname,'..');
const code=buildSync({entryPoints:[path.join(root,'src/character3d.js')],bundle:true,minify:true,write:false,format:'iife',legalComments:'inline'}).outputFiles[0].text;
const asset=fs.readFileSync(path.join(root,'assets/character/climber.glb')).toString('base64');
const p=path.join(root,'index.html');let html=fs.readFileSync(p,'utf8').replace(/\r\n/g,'\n');
const block='<!-- CHARACTER_3D_START -->\n<script>'+code.replaceAll('</script','<\\/script')+'\nwindow.climberModelData="'+asset+'";</script>\n<!-- CHARACTER_3D_END -->';
if(html.includes('<!-- CHARACTER_3D_START -->'))html=html.replace(/<!-- CHARACTER_3D_START -->[\s\S]*?<!-- CHARACTER_3D_END -->/,()=>block);
else html=html.replace("<script>\n'use strict';",()=>block+"\n<script>\n'use strict';");
fs.writeFileSync(p,html);console.log('Embedded rig and renderer',code.length,asset.length);


