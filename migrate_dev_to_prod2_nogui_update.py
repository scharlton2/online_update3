"""
Script to migrate softwares in dev environment to prod environment.

To run this script, copy qt_ifw_path.template.py to qt_ifw_path.py,
and modify the path to fit your environment.
"""

from datetime import datetime
import subprocess
import os
import re
import shutil

def copy_dev_src():
    """Copy dev_src folder to prod_src folder, except for gui.prepost"""

    items = os.listdir('dev_src/packages')
    for item in items:
        if item == 'gui.prepost':
            continue

        shutil.copytree('dev_src/packages/' + item, 'prod_src/packages/' + item)

    print('prod_src copied')

def copy_dev():
    """Copy folders under dev folder prod folder, except for gui.prepost"""

    items = os.listdir('dev')
    for item in items:
        if item == 'gui.prepost':
            continue

        fullitem = 'dev/' + item
        if not os.path.isdir(fullitem):
            continue

        shutil.copytree('dev/' + item, ' prod/' + item)

    print('prod copied')

def prepost_update(str):
    p = re.compile(r"<PackageUpdate>.+?</PackageUpdate>", re.DOTALL)
    updates = p.findall(str)
    for u in updates:
        if 'gui.prepost' in u:
            return u

    return None

def setup_updates():
    """Copy Updates.xml from dev to prod"""

    prod_update_path = 'prod/Updates.xml'
    f = open(prod_update_path, 'r')
    prod_updates = f.read()
    f.close()

    prod_gui_update = prepost_update(prod_updates)

    dev_update_path = 'dev/Updates.xml'
    f = open(dev_update_path, 'r')
    dev_updates = f.read()
    f.close()

    dev_gui_update = prepost_update(dev_updates)

    new_prod_updates = dev_updates.replace(dev_gui_update, prod_gui_update)

    f = open(prod_update_path, 'w')
    f.write(new_prod_updates)
    f.close()
    print('Updates.xml updated')

copy_dev_src()
copy_dev()
setup_updates()
