"""
An update manager which gets moved to appdata to run and git clone
the main directory.

This is currently for windows only!
"""
import os
import sys
import ctypes
import requests
import shutil

# Git definitions
GIT_EXE = f".\\Git\\cmd\\git.exe"
GIT_REPO = f"\"https://github.com/Sidekick-Robotics/Sight-updates\""

def is_admin():
    """Check if the updater manager has update permissions"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Relaunch the script with admin privileges using UAC."""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def update_sight():
    """Git cloen the latest repository."""
    GIT_CMD = f"{GIT_EXE} clone {GIT_REPO} {GIT_DES}"
    print(GIT_CMD)
    os.system(GIT_CMD)


if __name__ == "__main__":
    GIT_DES = f"\"C:\\Program Files (x86)\\Sight\""

    # Run as admin if updating and not admin
    if not is_admin():
        run_as_admin()
        sys.exit()

    # Manage the path if the path already exists
    if os.path.exists(GIT_DES):
        shutil.rmtree(GIT_DES)
        os.mkdir(GIT_DES)

    update_sight()
