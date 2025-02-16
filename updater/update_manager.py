"""
An update manager which gets moved to appdata to run and git clone
the main directory.
"""
import os
import sys
import ctypes
import time
import shutil

def run_as_admin():
    """Relaunch the script with admin privileges using UAC."""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def update_dir():
    """TODO"""

GIT_EXE = "./Git/cmd/git.exe"
GIT_REPO = "https:/github.com/Sidekick-Robotics/Sight-updates"

if __name__ == "__main__":
    GIT_DES = f"C:\\Program Files (x86)\\Sight"

    try:
        shutil.rmtree(GIT_DES)
    except PermissionError:
        run_as_admin()
        sys.exit()

    GIT_CMD = f"{GIT_EXE} clone {GIT_REPO} {GIT_DES}"

    os.system(GIT_CMD)
    time.sleep(5)
    print("Done")