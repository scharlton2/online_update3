# How to build iRIC installer
iRIC installer can be created using Qt Installer Framework.

## Install Qt installer Framework
Qt Installer Framework can be installed using Qt Maintainance tool.
Qt installer framework is located at Qt/Tools/Qt Installer Framework 2.0 in the tree of components.
When you find it, please check it, and press next buttons, to install it.

## How to update files in installer
1. Files to be included in installer are in packages/(packagename)/data folder. Overwrite the files you want to update.
2. Update version. Version number is in the following files. Update both to the same version.
    - packages/(packagename)/data/definition.xml
    - packages/(packagename)/meta/package.xml

## Build offline installer
You can build installer with the following command:

`binarycreator --offline-only -c config/config.xml -p packages installer_offline`

This will create installer_offline.exe.

## Build repository files

You can build archive files that you should upload to repository. By uploading these files, user can obtain updated files through iRIC Maintainance Tool.

`repogen -p packages repo`

This will create repo folder, that includes 7z files.

Currently, the repository to distribute updates are at the following URL. It was created onlyl for testing so maybe this will be changed in the near future.
https://i-ric.org/svn/iric/qt_dev

## Reference Documentation
Documentation of Qt Installer Framework can be hound in the following URL:
http://doc.qt.io/qtinstallerframework/
