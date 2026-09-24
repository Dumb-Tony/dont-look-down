# Editable metre-scale climber; execute in Higgsfield 3D Jutsu / Blender.
import bpy, math
from mathutils import Vector
from math import sin, cos, pi
for obj in list(bpy.data.objects): bpy.data.objects.remove(obj, do_unlink=True)
def mat(name,color,rough=.7,metal=0):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
 return m
teal=mat('Teal woven shell',(.035,.23,.28));darkteal=mat('Reinforced jacket panels',(.025,.13,.17));pants=mat('Navy stretch trousers',(.045,.065,.105));rubber=mat('Climbing rubber',(.023,.026,.031));orange=mat('Orange helmet',(.85,.23,.025),.32);ochre=mat('Harness webbing',(.58,.34,.065));skin=mat('Warm skin',(.55,.32,.20),.76);hair=mat('Brown hair',(.055,.034,.019));metal=mat('Brushed aluminium',(.42,.47,.50),.3,.75);chalk=mat('Chalk bag canvas',(.62,.20,.045));stitch=mat('Jacket seam piping',(.065,.30,.35));black=mat('Helmet vents',(.011,.017,.022))
arm=bpy.data.armatures.new('Climber humanoid skeleton');rig=bpy.data.objects.new('ClimberRig',arm);bpy.context.collection.objects.link(rig);bpy.context.view_layer.objects.active=rig;rig.select_set(True);bpy.ops.object.mode_set(mode='EDIT')
def bone(name,head,tail,parent=None):
 b=arm.edit_bones.new(name);b.head=head;b.tail=tail
 if parent:b.parent=arm.edit_bones[parent]
 return b
bone('Root',(0,0,0),(0,0,.15));bone('Pelvis',(0,0,.96),(0,0,1.08),'Root');bone('Spine',(0,0,1.08),(0,0,1.25),'Pelvis');bone('Chest',(0,0,1.25),(0,0,1.44),'Spine');bone('Neck',(0,0,1.44),(0,0,1.57),'Chest');bone('Head',(0,0,1.57),(0,0,1.79),'Neck')
for side,sgn in [('L',1),('R',-1)]:
 def P(x,y,z):return(sgn*x,y,z)
 bone('Clavicle.'+side,P(.035,0,1.44),P(.176,0,1.44),'Chest')
 bone('UpperArm.'+side,P(.176,0,1.44),P(.512,0,1.44),'Clavicle.'+side)
 bone('Forearm.'+side,P(.512,0,1.44),P(.816,0,1.44),'UpperArm.'+side)
 bone('Hand.'+side,P(.816,0,1.44),P(.866,0,1.44),'Forearm.'+side)
 for f,y,length in [('Index',-.024,.046),('Middle',-.008,.046),('Ring',.008,.043),('Little',.024,.034)]:
  start=.866
  for j in range(3):bone(f+str(j+1)+'.'+side,P(start+j*length/3,y,1.44),P(start+(j+1)*length/3,y,1.44),('Hand.' if j==0 else f+str(j)+'.')+side)
 bone('Thumb1.'+side,P(.829,-.027,1.44),P(.852,-.046,1.435),'Hand.'+side);bone('Thumb2.'+side,P(.852,-.046,1.435),P(.878,-.053,1.431),'Thumb1.'+side)
 bone('Thigh.'+side,P(.088,0,.96),P(.10,-.006,.50),'Pelvis');bone('Shin.'+side,P(.10,-.006,.50),P(.10,0,.095),'Thigh.'+side);bone('Foot.'+side,P(.10,0,.095),P(.10,-.13,.045),'Shin.'+side);bone('Toe.'+side,P(.10,-.13,.045),P(.10,-.21,.045),'Foot.'+side)
bpy.ops.object.mode_set(mode='OBJECT');rig.select_set(False)
def mesh(name,verts,faces,material,weights):
 data=bpy.data.meshes.new(name);data.from_pydata(verts,[],faces);data.update();o=bpy.data.objects.new(name,data);bpy.context.collection.objects.link(o);data.materials.append(material)
 for p in data.polygons:p.use_smooth=True
 groups={n:o.vertex_groups.new(name=n) for n in {n for ws in weights for n in ws}}
 for idx,ws in enumerate(weights):
  for n,w in ws.items():
   if w>0:groups[n].add([idx],w,'REPLACE')
 o.parent=rig;mod=o.modifiers.new('Skeleton skin weights','ARMATURE');mod.object=rig
 return o
def ell(name,center,radii,material,joint,segments=24,rings=12):
 v=[];f=[]
 for j in range(rings+1):
  t=pi*j/rings
  for k in range(segments):
   a=2*pi*k/segments;v.append((center[0]+radii[0]*sin(t)*cos(a),center[1]+radii[1]*sin(t)*sin(a),center[2]+radii[2]*cos(t)))
 for j in range(rings):
  for k in range(segments):a=j*segments+k;b=j*segments+(k+1)%segments;f.append((a,b,b+segments,a+segments))
 return mesh(name,v,f,material,[{joint:1} for _ in v])
def tube(name,sections,material,weightfn,axis='z',segments=24):
 v=[];f=[];w=[]
 for i,(x,y,z,r1,r2) in enumerate(sections):
  for k in range(segments):
   a=2*pi*k/segments
   p=(x+r1*cos(a),y+r2*sin(a),z) if axis=='z' else (x,y+r1*cos(a),z+r2*sin(a))
   v.append(p);w.append(weightfn(i,p))
 for j in range(len(sections)-1):
  for k in range(segments):a=j*segments+k;b=j*segments+(k+1)%segments;f.append((a,b,b+segments,a+segments))
 f.append(tuple(reversed(range(segments))));f.append(tuple((len(sections)-1)*segments+k for k in range(segments)))
 return mesh(name,v,f,material,w)
def rigid(name,sections,material,joint,axis='z',segments=24):return tube(name,sections,material,lambda i,p:{joint:1},axis,segments)
def torsoWeight(i,p):
 z=p[2]
 if z<1.06:return {'Pelvis':1}
 if z<1.23:
  t=(z-1.06)/.17;return {'Spine':t,'Pelvis':1-t}
 t=min(1,(z-1.23)/.12);return {'Chest':t,'Spine':1-t}
tube('Jacket continuous trunk',[(0,0,z,x,y) for z,x,y in [(1.015,.142,.095),(1.04,.148,.10),(1.10,.145,.104),(1.17,.15,.11),(1.25,.174,.115),(1.34,.199,.12),(1.41,.202,.105),(1.46,.15,.087),(1.50,.078,.067)]],teal,torsoWeight)
ell('Trouser pelvis',(0,0,.96),(.158,.103,.137),pants,'Pelvis')
ell('Neck skin',(0,0,1.55),(.055,.055,.08),skin,'Neck')
ell('Head',(0,-.008,1.665),(.088,.089,.122),skin,'Head')
ell('Hair at nape',(0,.056,1.655),(.085,.045,.089),hair,'Head')
ell('Helmet protective shell',(0,0,1.748),(.112,.117,.095),orange,'Head',32,18)
for x in [-.069,-.033,.033,.069]:ell('Helmet rear vent',(x,.103,1.757),(.010,.012,.022),black,'Head',12,8)
for x in [-.043,.043]:
 ell('Eye',(x,-.091,1.675),(.012,.008,.007),black,'Head',12,8)
ell('Nose',(0,-.10,1.65),(.017,.022,.025),skin,'Head',16,10)
# Hood lies around neck and folds onto upper back.
rigid('Hood collar',[(0,0,1.48,.102,.09),(0,0,1.51,.094,.084),(0,0,1.535,.078,.075)],darkteal,'Neck')
ell('Folded hood',(0,.099,1.423),(.112,.044,.07),teal,'Chest')
for side,sgn in [('L',1),('R',-1)]:
 upper='UpperArm.'+side;fore='Forearm.'+side
 def aw(i,p):
  x=abs(p[0]);t=max(0,min(1,(x-.475)/.075));return {upper:1-t,fore:t}
 tube('Continuous jacket sleeve '+side,[(sgn*x,0,1.44,r,r*.92) for x,r in [(.145,.072),(.19,.074),(.25,.069),(.35,.060),(.43,.053),(.475,.051),(.512,.052),(.548,.05),(.59,.049),(.68,.045),(.77,.036),(.806,.033)]],teal,aw,'x')
 rigid('Dark cuff '+side,[(sgn*x,0,1.44,.034,.032) for x in [.787,.811]],darkteal,fore,'x')
 ell('Palm '+side,(sgn*.839,0,1.44),(.038,.034,.019),skin,'Hand.'+side)
 for f,y,length in [('Index',-.024,.046),('Middle',-.008,.046),('Ring',.008,.043),('Little',.024,.034)]:
  sections=[(sgn*(.861+j*length/6),y,1.44,.0073 if j<5 else .005,.008 if j<5 else .0055) for j in range(7)]
  def fw(i,p,f=f,side=side):
   t=max(0,min(2,i/2-.5));j=int(t);return {f+str(j+1)+'.'+side:1-(t-j),f+str(min(3,j+2))+'.'+side:t-j} if j<2 else {f+'3.'+side:1}
  tube(f+' finger '+side,sections,skin,fw,'x',12)
 ell('Thumb base '+side,(sgn*.844,-.03,1.437),(.024,.016,.017),skin,'Thumb1.'+side,16,10)
 ell('Thumb tip '+side,(sgn*.865,-.047,1.433),(.022,.01,.012),skin,'Thumb2.'+side,16,10)
 def lw(i,p):
  t=max(0,min(1,(.55-p[2])/.10));return {'Thigh.'+side:1-t,'Shin.'+side:t}
 tube('Continuous trouser leg '+side,[(sgn*x,y,z,r1,r2) for x,y,z,r1,r2 in [(.087,0,.97,.09,.089),(.088,0,.88,.085,.087),(.092,0,.76,.071,.078),(.10,-.005,.62,.061,.065),(.10,-.006,.54,.057,.059),(.10,-.006,.50,.056,.058),(.10,-.003,.46,.054,.056),(.10,0,.38,.06,.06),(.10,0,.26,.049,.051),(.10,0,.14,.034,.04),(.10,0,.10,.032,.038)]],pants,lw)
 ell('Reinforced knee '+side,(sgn*.10,-.051,.51),(.053,.012,.077),darkteal,'Shin.'+side)
 ell('Shoe '+side,(sgn*.10,-.066,.061),(.049,.142,.054),rubber,'Foot.'+side)
 ell('Shoe rand '+side,(sgn*.10,-.073,.040),(.051,.143,.016),ochre,'Foot.'+side)
 ell('Shoe heel '+side,(sgn*.10,.051,.085),(.031,.02,.033),ochre,'Foot.'+side)
 rigid('Harness leg loop '+side,[(sgn*.088,0,z,.091,.091) for z in [.884,.908]],ochre,'Thigh.'+side)
# Belt, back equipment and seam details; each is attached to an actual bone.
rigid('Harness waist belt',[(0,0,z,.154,.109) for z in [1.015,1.048]],ochre,'Pelvis')
ell('Orange chalk bag',(0,.13,.96),(.066,.047,.087),chalk,'Pelvis')
rigid('Chalk bag rim',[(0,.13,z,.065,.044) for z in [1.025,1.038]],rubber,'Pelvis')
for side,sgn in [('L',1),('R',-1)]:
 ell('Metal gear loop '+side,(sgn*.14,.07,1.00),(.01,.016,.045),metal,'Pelvis',16,10)
# Back yoke seam as slender shaped strip.
rigid('Jacket back yoke seam',[(-.172,.10,1.358,.003,.003),(-.09,.12,1.358,.003,.003),(0,.122,1.358,.003,.003),(.09,.12,1.358,.003,.003),(.172,.10,1.358,.003,.003)],stitch,'Chest','x',8)
# Correct mirrored tube normals for portable one-sided materials.
import bmesh
for o in bpy.data.objects:
 if o.type=='MESH':
  bm=bmesh.new();bm.from_mesh(o.data);bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bm.to_mesh(o.data);bm.free()
# Delivery scene and a restrained reach animation for inspection.
scene=bpy.context.scene;scene.render.engine='BLENDER_EEVEE';scene.render.resolution_x=720;scene.render.resolution_y=900;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.render.image_settings.media_type='IMAGE';scene.world=bpy.data.worlds.new('Studio ambient');scene.world.color=(.18,.18,.18)
def light(name,loc,power,color):
 d=bpy.data.lights.new(name,'POINT');d.energy=power;d.shadow_soft_size=2;o=bpy.data.objects.new(name,d);bpy.context.collection.objects.link(o);o.location=loc;o.rotation_euler=(Vector((0,0,1))-o.location).to_track_quat('-Z','Y').to_euler();d.color=color
light('Warm key',(-3,4,5),450,(1,.88,.73));light('Cool fill',(3,2,3),240,(.75,.85,1))
camd=bpy.data.cameras.new('Climber review camera');cam=bpy.data.objects.new('Climber review camera',camd);bpy.context.collection.objects.link(cam);cam.location=(2.4,5,2.5);cam.rotation_euler=(Vector((0,0,.98))-cam.location).to_track_quat('-Z','Y').to_euler();camd.type='ORTHO';camd.ortho_scale=2.35;scene.camera=cam
scene.render.film_transparent=False
scene.frame_start=1;scene.frame_end=60;scene.render.fps=30
for name in ['UpperArm.L','UpperArm.R','Forearm.L','Forearm.R']:
 p=rig.pose.bones[name];p.rotation_mode='XYZ';p.rotation_euler=(0,0,0);p.keyframe_insert('rotation_euler',frame=1)
rig.pose.bones['UpperArm.L'].rotation_euler[0]=-.7;rig.pose.bones['UpperArm.L'].keyframe_insert('rotation_euler',frame=30)
rig.pose.bones['Forearm.L'].rotation_euler[0]=-.6;rig.pose.bones['Forearm.L'].keyframe_insert('rotation_euler',frame=30)
for name in ['UpperArm.L','UpperArm.R','Forearm.L','Forearm.R']:
 p=rig.pose.bones[name];p.rotation_euler=(0,0,0);p.keyframe_insert('rotation_euler',frame=60)
scene.frame_set(1)
target=artifacts.file(name='rigged-climber-review.png',media_type='image/png');scene.render.filepath=target.path;bpy.ops.render.render(write_still=True);target.publish()
result={'bones':len(arm.bones),'meshes':len([o for o in bpy.data.objects if o.type=='MESH']),'rig':'ClimberRig','heightMeters':1.843,'fingerTipBones':['Middle3.L','Middle3.R']}


