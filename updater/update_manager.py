"""
An update manager which gets moved to appdata to run and git clone
the main directory.

This is currently for windows only!
"""
import os
import sys
import ctypes
import shutil

from dulwich.porcelain import clone

# Git definitions
GIT_EXE = f".\\Git\\cmd\\git.exe"
GIT_REPO = f"\"https://github.com/Sidekick-Robotics/Sight-updates\""

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
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def update_sight():
    """Git clone the latest repository."""
    clone(GIT_REPO, GIT_DES)

if __name__ == "__main__":
    GIT_DES = sys.argv[1]
    SEP = sys.argv[2]

    print(SEP, GIT_DES)

    # Run as admin if needed
    if requires_admin() and not is_admin():
        run_as_admin()
        sys.exit()

    # Manage the path if the path already exists
    if os.path.exists(GIT_DES):
        shutil.rmtree(GIT_DES)
        os.mkdir(GIT_DES)

    update_sight()
