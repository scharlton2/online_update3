"""
Script to build yasu installer.

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
    installer_name = 'iRIC_Installer_yasu'

    cmd = binc + ' --online-only -c yasu_src/config/config.xml'
    cmd += ' -p prod_src\\packages ' + installer_name
    
    print(cmd)

    subprocess.check_output(cmd)

build_installer()
