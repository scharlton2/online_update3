import subprocess
import os
import shutil

items = os.listdir('prod_src/packages')
for item in items:
    if item == 'gui.prepost':
        continue

    fullitem = 'prod_src/packages/'+ item

    shutil.rmtree(fullitem)

items = os.listdir('prod')
for item in items:
    fullitem = 'prod/' + item
    if not os.path.isdir(fullitem):
        continue
    if item == 'gui.prepost':
        continue

    shutil.rmtree(fullitem)
