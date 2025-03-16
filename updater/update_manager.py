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

def delete_except(directory, keep_files):
    """Delete the files except the uninstall files."""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        if item in keep_files:
            print(f"Kept: {item_path}")
            continue
        
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Deleted file: {item_path}")
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Deleted folder: {item_path}")

def update_sight():
    """Git clone the latest repository."""
    try:
        os.mkdir(INSTALL_DIR)
    except Exception as e:
        print(e)
    clone(GIT_REPO, INSTALL_DIR)

def copy_directory_contents(src_dir: str, dest_dir: str):
    """
    Copies all contents from src_dir to dest_dir.
    If a file with the same name exists in dest_dir, it is overwritten.
    Existing files in dest_dir that do not exist in src_dir remain unchanged.
    """
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        if os.path.isdir(src_item):
            shutil.copytree(src_item, dest_item, dirs_exist_ok=True)  # Copies subdirectory recursively
        else:
            shutil.copy2(src_item, dest_item)  # Copies file with metadata
    
    # Copy all files from src_dir to dest_dir
    for file in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file)
        dest_file = os.path.join(dest_dir, file)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dest_file)  # Copy each file


if __name__ == "__main__":

    # Constant definitions
    GIT_DES = sys.argv[1]
    SEP = sys.argv[2]
    INSTALL_DIR = GIT_DES+SEP+"new_version"

    # Run as admin if needed
    if requires_admin():
        run_as_admin()
        sys.exit()

    # Manage the path if the path already exists
    delete_except(GIT_DES, ["unins000.dat", "unins000.exe"])

    # Install the update
    update_sight()

    # Move the new version
    copy_directory_contents(INSTALL_DIR, GIT_DES)
