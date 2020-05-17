"""
Script to migrate softwares in dev environment to prod environment.

To run this script, copy qt_ifw_path.template.py to qt_ifw_path.py,
and modify the path to fit your environment.
"""

from datetime import datetime
import subprocess
import os
import shutil
from qt_ifw_path import QT_IFW_PATH

def copy_dev_src():
    """Copy dev_src folder to prod_src folder"""

    shutil.copytree('dev_src/packages', 'prod_src/packages')
    print('prod_src copied')

def copy_dev():
    """Copy folders under dev folder prod folder"""

    items = os.listdir('dev')
    for item in items:
        fullitem = os.path.join('dev', item)
        if not os.path.isdir(fullitem):
            continue

        shutil.copytree('dev/' + item, 'prod/' + item)

    os.remove('prod/Updates.xml')
    shutil.copy('dev/Updates.xml', 'prod/Updates.xml')

    print('prod copied')

def modify_qs():
    """Modify iRIC GUI installscript.qs, RivMaker installscript.qs"""

    qs_path = 'prod_src/packages/gui.prepost/meta/installscript.qs'
    f = open(qs_path, 'r')
    content = f.read()
    f.close()

    # Remove "(develop)"
    content = content.replace('(develop)', '')

    # Add Operation to register "ipro" file as iRIC project
    placeHolder = '"@StartMenuDir@/Uninstall iRIC.lnk", "workingDirectory=@TargetDir@");\n'

    additional = (
        '\tcomponent.addOperation("RegisterFileType", "ipro", "@TargetDir@\\\\guis\\\\prepost\\\\iRIC.exe" + " \\"%1\\"",\n' +
        '\t\t"iRIC Project file", "application/iric",\n' +
        '\t\t"@TargetDir@/guis/prepost/iconiRICFile.ico", "ProgId=iRICProject.ipro");\n')

    content = content.replace(placeHolder + additional, placeHolder)
    content = content.replace(placeHolder, placeHolder + additional)

    f = open(qs_path, 'w')
    f.write(content)
    f.close()

    print('iRIC GUI installscript.qs modified')

    qs_path = 'prod_src/packages/gui.rivmaker/meta/installscript.qs'
    if not os.path.exists(qs_path):
        return

    f = open(qs_path, 'r')
    content = f.read()
    f.close()

    # Add Operation to register "rpro" file as RivMaker project
    placeHolder = '"@StartMenuDir@/Rivmaker.lnk", "workingDirectory=@TargetDir@/guis/rivmaker");\n'

    additional = (
        '\tcomponent.addOperation("RegisterFileType", "rpro", "@TargetDir@\\\\guis\\\\rivmaker\\\\Rivmaker.exe" + " \\"%1\\"",\n' +
        '\t\t"RivMaker Project file", "application/rivmaker",\n' +
        '\t\t"@TargetDir@/guis/rivmaker/iconRivMakerFile.ico", "ProgId=RivMakerProject.rpro");\n')
    content = content.replace(placeHolder + additional, placeHolder)
    content = content.replace(placeHolder, placeHolder + additional)

    f = open(qs_path, 'w')
    f.write(content)
    f.close()

    print('RivMaker installscript.qs modified')

def build_repository():
    """Run repogen to build files for online update"""

    repogen = QT_IFW_PATH + '\\bin\\repogen.exe'
    cmd = repogen + ' -p prod_src\\packages --update --include gui.prepost prod'
    subprocess.check_output(cmd)
    print('Online update repository updated')

def build_installer():
    """Run binarycreator to build offline installer"""

    binc = QT_IFW_PATH + '\\bin\\binarycreator.exe'
    now = datetime.now()
    installer_name = 'iRIC_Installer_' + now.strftime('%y%m%d')

    cmd = binc + ' --offline-only -c prod_src/config/config.xml'
    cmd += ' -p prod_src\\packages prod\\' + installer_name

    subprocess.check_output(cmd)

copy_dev_src()
copy_dev()
modify_qs()
build_repository()
build_installer()
