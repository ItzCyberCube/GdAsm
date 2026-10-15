# import gmdkit
import gmdkit.mappings.obj_prop
from gmdkit import Level, Object
from gmdkit.mappings import obj_id, obj_prop
from gmdkit.models.prop.remaps import RemapList
from gmdkit.models.prop.groups import *
# open file
level = Level.from_file("gmdkit.gmd")

f = open('code.txt')
code = []
for a in f:
    line = list(map(int, a.split()))
    # дозаполняю нулями функции
    while len(line) < 4:
        line.append(0)
    code.append(line)




# get inner level properties
start = level.start
obj_list = level.objects

for i in range(1,len(code)+1):
    for j in range(1,5):
        if code[i-1][j-1]==0: continue
        new_obj = Object.default(3619)
        new_obj.update(
            {
                obj_prop.Y: (20-i) * 30,
                obj_prop.X: (j) * 30,
                obj_prop.trigger.item_edit.TARGET_ITEM_ID: j*1000+i,
                obj_prop.trigger.item_edit.MOD: code[i-1][j-1]


            }
        )
        obj_list.append(new_obj)







# export level
level.update_file()
# set properties of object
# objects subclass dict() so they can use all dict methods alongside the ones defined by DictClass


# append object to the level's object list
# can also be done directly to level.objects or level['k4'].objects (which level.objects references)
# lvl_prop.level.OBJECT_STRING also maps to 'k4'


# export level
level.to_file("gmdkit.gmd")