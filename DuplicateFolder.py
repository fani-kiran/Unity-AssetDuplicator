import fnmatch
import os
import argparse
import uuid

# PARAMETERS
parser = argparse.ArgumentParser(description='Rearrange a Unity\'s project folder guids.')
parser.add_argument('-i, --input',  metavar='FOLDER', type=str, nargs=1, required=True, dest='input_folder',
    help='input folder')
args = parser.parse_args()
input_folder = None if args.input_folder is None else args.input_folder[0]
if not os.path.isdir(input_folder):
    print('ERROR: Path not found.')
    quit(1)

# SCAN FILES
 
register_list = []
print('')
metas = dict()
mats = []
prefabs = []
controllers = []
scenes = []
anims = []
spriteAtlases = []
scriptableObjects = []

for root, folders, files in os.walk(input_folder):
    for fname in files:
        if fnmatch.fnmatch(fname, '*.meta'):
            metaname = root + os.sep + fname
            file = open(metaname, 'r')
            for line in file:
                elements = line.split(': ')
                if elements[0] == 'guid':
                    id = elements[1].replace('\n', '')
                    metas.update({id: [metaname, uuid.uuid4().hex]})
            file.close()
        if fnmatch.fnmatch(fname, '*.mat'):
            mats += [root + os.sep + fname]
        if fnmatch.fnmatch(fname, '*.prefab'):
            prefabs += [root + os.sep + fname]
        if fnmatch.fnmatch(fname, '*.controller'):
            controllers += [root + os.sep + fname]
        if fnmatch.fnmatch(fname, '*.unity'):
            scenes += [root + os.sep + fname]
        if fnmatch.fnmatch(fname, '*.anim'):
            anims += [root + os.sep + fname]
        if fnmatch.fnmatch(fname, '*.spriteatlas'):
            spriteAtlases += [root + os.sep + fname]
        if fnmatch.fnmatch(fname, '*.asset'):
            scriptableObjects += [root + os.sep + fname]
            

# CHANGE METAS

for k, v in metas.items():
    file = open(v[0], 'r')
    met = file.readlines()
    for i, l in enumerate(met):
        if 'guid:' in l:
            met[i] = l.replace(k, v[1])

    file.close()
    file = open(v[0], 'w')
    file.writelines(met)
    file.close()
    

#CHANGE EVERYTHING [Prefab,Texture,Sound,Material,Animation:Controller+File+Keyframes,Scene,SpriteAtlas,ScriptableObject]

for pname in prefabs + mats + controllers + scenes + anims + spriteAtlases + scriptableObjects:
    file = open(pname, 'r')
    changed = False
    segregate = file.readlines()
    for i, l in enumerate(segregate):
        if 'guid:' in l:
            key = None
            for k in metas.keys():
                if k in l:
                    key = k
                    changed = True
            if key is not None:
                segregate[i] = l.replace(key, metas[key][1])
                print(segregate[i], end='')
                print(key, '->', metas[key][1])
            else:
                print(segregate[i])
    file.close()
    if changed:
        file = open(pname, 'w')
        file.writelines(segregate)
        file.close()

        
