import * as T from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
const v=()=>new T.Vector3();
window.createClimber3D=async function(base64,atlas){
 const renderer=new T.WebGLRenderer({alpha:true,antialias:true,preserveDrawingBuffer:true});renderer.setSize(576,640,false);renderer.setClearColor(0,0);renderer.outputColorSpace=T.SRGBColorSpace;renderer.toneMapping=T.ACESFilmicToneMapping;renderer.toneMappingExposure=1.05;
 const scene=new T.Scene(),camera=new T.OrthographicCamera(-90,90,100,-100,.1,1000);camera.position.set(0,0,300);camera.lookAt(0,0,0);
 scene.add(new T.HemisphereLight(0xe5f1ff,0x6b5841,2));const key=new T.DirectionalLight(0xffdfac,3);key.position.set(-90,120,140);scene.add(key);const fill=new T.DirectionalLight(0x98cfff,1.4);fill.position.set(90,20,100);scene.add(fill);
 const bytes=Uint8Array.from(atob(base64),c=>c.charCodeAt(0));const gltf=await new GLTFLoader().parseAsync(bytes.buffer,'');
 const model=gltf.scene;scene.add(model);model.scale.setScalar(62.5);model.rotation.y=Math.PI;model.position.y=-60;
 const bones={},rest=new Map();let meshes=0;
 function fabric(x,y,w,h){const c=document.createElement('canvas');c.width=256;c.height=256;c.getContext('2d').drawImage(atlas,x,y,w,h,0,0,256,256);const t=new T.CanvasTexture(c);t.colorSpace=T.SRGBColorSpace;t.wrapS=t.wrapT=T.RepeatWrapping;t.anisotropy=4;return t;}
 const jacketTexture=fabric(270,265,215,210),trouserTexture=fabric(1590,920,170,250);
 function cloth(o){
  const m=o.material;if(!/Teal woven|Navy stretch/.test(m.name))return;
  const g=o.geometry,pos=g.attributes.position,box=new T.Box3().setFromBufferAttribute(pos),size=box.getSize(v()),arm=o.name.includes('sleeve'),uv=[];
  for(let i=0;i<pos.count;i++){
   const x=pos.getX(i),y=pos.getY(i),z=pos.getZ(i);
   if(arm)uv.push((Math.atan2(z,y-1.44)+Math.PI)/(2*Math.PI)*2,(x-box.min.x)/size.x*2);
   else uv.push((x-box.min.x)/Math.max(.001,size.x),(y-box.min.y)/Math.max(.001,size.y)*1.8);
  }
  g.setAttribute('uv',new T.Float32BufferAttribute(uv,2));m.map=m.name.includes('Teal')?jacketTexture:trouserTexture;m.color.set(0xffffff);m.bumpMap=m.map;m.bumpScale=.0015;m.roughness=.88;m.needsUpdate=true;
 }

 model.traverse(o=>{if(o.isLight)o.visible=false;if(o.isBone){bones[o.name.replaceAll('.','')]=o;rest.set(o,o.quaternion.clone());}if(o.isSkinnedMesh){meshes++;if(o.material.name==='Orange helmet')o.material.color.set(0xe96a21);cloth(o);o.frustumCulled=false;o.material.roughness=Math.max(.55,o.material.roughness);}});
 function B(name){const b=bones[name.replaceAll('.','')];if(!b)throw new Error('Missing rig bone '+name);return b;}
 model.updateMatrixWorld(true);
 const axes=new Map();for(const b of Object.values(bones)){const child=b.children.find(c=>c.isBone);if(child)axes.set(b,child.position.clone().normalize());}
 function point(b){return b.getWorldPosition(v());}
 function aim(name,to){const b=B(name),origin=point(b),parentQ=b.parent.getWorldQuaternion(new T.Quaternion()),dir=to.clone().sub(origin).normalize().applyQuaternion(parentQ.invert());const axis=axes.get(b)||new T.Vector3(0,1,0);b.quaternion.setFromUnitVectors(axis,dir);b.updateWorldMatrix(false,true);}
 const handLengths={};for(const side of ['L','R']){const hand=B('Hand.'+side),end=B('Middle3.'+side),tip=end.localToWorld(new T.Vector3(0,.046/3,0)),axis=hand.worldToLocal(tip.clone());handLengths[side]=axis.length()*62.5;axes.set(hand,axis.normalize());}
 let contacts=[],lastPose=[];
 function draw(ctx,player,poses,planted,time){
  for(const [b,q] of rest)b.quaternion.copy(q);
  model.updateMatrixWorld(true);contacts=[];lastPose=[];
  for(let i=0;i<2;i++){
   const side=i===0?'L':'R',p=poses[i];
   const to3=(p,z=0)=>new T.Vector3(p.x-player.x,player.y-p.y,z);
   const shoulder=point(B('UpperArm.'+side)),tip=to3(p.tip,0);
   // Analytic arm IK retains the rig's measured bone lengths. Fingertips are
   // the end effector, with a separate wrist and elbow in the hierarchy.
   const direction=tip.clone().sub(shoulder),distance=direction.length(),d=Math.max(4.001,Math.min(46,distance));direction.normalize();
   const lowerLength=19+handLengths[side],along=(21*21-lowerLength*lowerLength+d*d)/(2*d),height=Math.sqrt(Math.max(0,21*21-along*along));
   const pole=new T.Vector3(i?1:-1,-.45,.32);pole.addScaledVector(direction,-pole.dot(direction)).normalize();
   const elbow=shoulder.clone().addScaledVector(direction,along).addScaledVector(pole,height);
   const lower=tip.clone().sub(elbow).normalize(),wrist=tip.clone().addScaledVector(lower,-handLengths[side]);
   aim('UpperArm.'+side,elbow);aim('Forearm.'+side,wrist);aim('Hand.'+side,tip);
   // Straight middle fingertip defines the exact rock contact. Other fingers
   // curl gently around that contact when planted, without shifting it.
   for(const finger of ['Index','Ring','Little'])for(let j=1;j<=3;j++){const b=B(finger+j+'.'+side);b.rotateX(planted[i]?.16:0);}
   model.updateMatrixWorld(true);
   const end=B('Middle3.'+side),actual=end.localToWorld(new T.Vector3(0,.046/3,0));
   contacts.push({x:actual.x+player.x,y:player.y-actual.y,z:actual.z,error:actual.distanceTo(tip)});
   lastPose.push({shoulder:shoulder.toArray(),elbow:elbow.toArray(),wrist:wrist.toArray(),target:tip.toArray()});
  }
  // Legs are driven through their bones as well, with a slight climbing bend.
  for(let i=0;i<2;i++){const s=i?'R':'L',side=i?1:-1;aim('Thigh.'+s,new T.Vector3(side*6,-29,player.ground?0:4));aim('Shin.'+s,new T.Vector3(side*6,-54,0));}
  model.updateMatrixWorld(true);renderer.render(scene,camera);ctx.drawImage(renderer.domElement,player.x-90,player.y-100,180,200);
 }
 return{draw,inspect:()=>({type:'skinned-3d',boneCount:Object.keys(bones).length,skinnedMeshes:meshes,contacts:contacts.map(p=>({...p})),poses:lastPose}),dispose:()=>renderer.dispose()};
};
