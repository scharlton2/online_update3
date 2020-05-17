"""
Script to build dev installer.

To run this script, copy qt_ifw_path.template.py to qt_ifw_path.py,
and modify the path to fit your environment.
"""

import subprocess
import os
import shutil
from qt_ifw_path import QT_IFW_PATH

def build_installer():
    """Run binarycreator to build online installer"""

    binc = QT_IFW_PATH + '\\bin\\binarycreator.exe'
    installer_name = 'iRIC_Installer_dev'

    cmd = binc + ' --online-only -c dev_src/config/config.xml'
    cmd += ' -p dev_src\\packages ' + installer_name
    
    print(cmd)

    subprocess.check_output(cmd)

build_installer()
