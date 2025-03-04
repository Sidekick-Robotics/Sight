"""
An update manager which gets moved to appdata to run and git clone
the main directory.

This is currently for windows only!
"""
import os
import sys
import time
import ctypes
import shutil

from dulwich.porcelain import clone

# Git definitions
GIT_REPO = f"https://github.com/Sidekick-Robotics/Sight-updates.git"

def requires_admin():
    """Check if the updater needs admin permissions."""
    try:
        my_file = open(GIT_DES+SEP+"test.txt", "w", encoding="UTF-8")
        my_file.close()
    except PermissionError:
        return True
    return False

def is_admin():
    """Check if the updater manager has admin permissions."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Relaunch the script with admin privileges using UAC."""
    sys_args = f"\"{GIT_DES}\" {SEP}"
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys_args, None, 1)

def update_sight():
    """Git clone the latest repository."""
    clone(GIT_REPO, GIT_DES)

if __name__ == "__main__":
    GIT_DES = sys.argv[1]
    SEP = sys.argv[2]

    print(__file__)
    print(SEP, GIT_DES)

    time.sleep(2)

    # Run as admin if needed
    if requires_admin() and not is_admin():
        run_as_admin()
        sys.exit()

    # Manage the path if the path already exists
    if os.path.exists(GIT_DES):
        try:
            shutil.rmtree(GIT_DES)
        except PermissionError:
            pass
        try:
            os.mkdir(GIT_DES)
        except FileExistsError:
            pass

    update_sight()
