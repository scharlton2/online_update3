# How to migrate data from dev env to prod env

iRIC installer has two version: one for developers (dev), another for 
end users (prod).

The workflow is as follows:
  - When releasing new version, it is at first registered at dev environment.
    iRIC developers test the new version.

  - When we think it is OK, we distribute it at prod environment.

To do this, we follow the procedure below. To use it, you need python3 installed.

1. run python migrate_dev_to_prod1.py
2. Commit changes made by the script to server (remove old files from prod)
3. run python migrate_dev_to_prod2.py
4. Commit changes made by the script to server (copy files from dev to prod)

The process 3. takes some time, because you need to build repository for prod with
slightly different setting than dev: It is to make iRIC shortcut on Desktop, with
name "iRIC", not "iRIC(develop)".


When you've upgraded only solvers, not GUI, you should use python scripts
with suffix "_no_gui_update". These scripts are faster, and consume less storage
on subversion server.
