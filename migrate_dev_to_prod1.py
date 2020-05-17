import subprocess
import os
import shutil

shutil.rmtree('prod_src/packages')

items = os.listdir('prod')
for item in items:
    fullitem = os.path.join('prod', item)
    if not os.path.isdir(fullitem):
        continue

    shutil.rmtree(fullitem)
