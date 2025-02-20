"""
Configure all files necessary to run the sidekick application.
NOTE: WINDOWS ONLY
"""
import os
import time

def change_user():
    """
    Uses the template in this directory to update
    the "Arduino15" files
    """

    print("<<< RUNNING >>> Updating the sidekick config")

    with open(f".{SEP}cli_yaml_example.yaml", "r", encoding="UTF-8") as yaml:
        yaml_file = yaml.read()

    downloads = ARDUINO + "staging"
    libraries = DOCUMENTS + "SideKick" + SEP + "Libraries"

    directories = f"directories:\n\
    data: {ARDUINO}\n\
    downloads: {downloads}\n\
    user: {libraries}"

    yaml_file = yaml_file.replace("directories:", directories)

    with open(f"{ARDUINO}{SEP}arduino-cli.yaml", "w", encoding="UTF-8") as yaml:
        yaml.write(yaml_file)

def install_boards():
    """
    Installs all of the key boards such as:
    Raspberry PI Pico
    Arduino Uno, nano, etc..
    Teensy 4.1, 4.0, 3.6, etc...
    """

    print("<<< RUNNING >>> Installing your boards")

    os.system(CLI + " core install arduino:avr")
    os.system(CLI + " core install teensy:avr")
    os.system(CLI + " core install arduino:mbed_rp2040")

if __name__ == "__main__":
    print("RUNNING - printing current paths:")
    print(os.listdir("..\\"))
    time.sleep(3)

    USER = os.getlogin()

    SEP = "\\"
    CLI = "..\\Externals\\arduino-cli-windows.exe"
    DOCUMENTS = f"C:\\Users\\{USER}\\Documents\\"
    ARDUINO = f"C:\\Users\\{USER}\\AppData\\Local\\Arduino15\\"
    TYPE = ".bat"

    os.system(CLI + " config init")
    change_user()
    install_boards()