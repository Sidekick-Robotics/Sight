"""
This file is responsible for handling all creation and
deletion of files.
"""

import os
import re
import shutil
import requests
import platform
import subprocess
import json

from pathlib import Path
from PyQt6 import QtWidgets as qtw
from dulwich.porcelain import clone

from globals import SIZES_IN_QSS
from globals import DEFAULT_SETTINGS, DEFAULT_BOARDS
from globals import GRAPH_BEGINNING, GRAPH_ENDING
from globals import CONSCIOS_GIT
from globals import VERSION

class SaveManager():
    """
    loads and saves data to the saves file
    """

    def __init__(self):
        self.record_status = False
        self.prev_record_status = False
        self.save_folder_path = ""
        self.sep = ""
        self.prev_save_data = []

    def create_new_file(self):
        """
        creates a new save file
        """
        num_of_saves = len(os.listdir(self.save_folder_path))
        with open(f"{self.save_folder_path}{self.sep}Save{num_of_saves+1}.sk", "w",
                    encoding="UTF-8"):
            pass

    def save_data(self, save_data):
        """
        saves the raw data to the latest save_file

        Args:
            raw_data (str): the raw data from com device
        """
        self.record_status = True

        if self.record_status != self.prev_record_status:
            self.create_new_file()

        save_name = f"Save{len(os.listdir(self.save_folder_path))}.sk"
        save_path = f"{self.save_folder_path}{self.sep}{save_name}"

        with open(save_path, "a", encoding="UTF-8") as save:
            for data in save_data:
                save.write(data)
                save.write("\n")

        self.prev_record_status = True

    def stop_save(self):
        """
        sets record_status to false
        """
        self.record_status = False
        self.prev_record_status = False

    def get_saved_data(self, file_dir):
        """
        loads the file and gets all data from it

        Returns:
            list: the saved raw data
        """
        with open(file_dir, "r", encoding="UTF-8") as save:
            data = save.readlines()

        return [item.strip() for item in data]

    def parse_line(self, line:str) -> list:
        """
        Returns:
            list: the terminal data
            list: the graph_data
            bool: the recording status
        """
        terminal_data = ""
        graph_data = []

        line = line.replace("\n", "")

        graph_data = re.findall(f"{GRAPH_BEGINNING}.*?{GRAPH_ENDING}", line)

        for indx, item in enumerate(graph_data):
            graph_data[indx] = item.replace(GRAPH_BEGINNING, "").replace(GRAPH_ENDING, "")

        terminal_data = re.sub(f'{GRAPH_BEGINNING}.*?{GRAPH_ENDING}', '', line)

        if not terminal_data:
            terminal_data = None
        if not graph_data:
            graph_data = None

        return terminal_data, graph_data

    def export_save(self, file_dir:str, new_name:str):
        """
        Convert the sidekick data to a .csv file for the user.
        """
        output = "Terminal,Graphs\n"

        with open(file_dir, "r", encoding="UTF-8") as my_file:
            for line in my_file:
                parsed_line = self.parse_line(line)
                if parsed_line[0] is None:
                    output += ","
                else:
                    output += parsed_line[0] + ","
                if parsed_line[1] is None:
                    output += ","
                else:
                    for graph in parsed_line[1]:
                        output += graph + ","
                output += "\n"

        try:
            with open(f"{new_name}", "w", encoding="UTF-8") as my_file:
                my_file.write(output)
        except PermissionError:
            qtw.QMessageBox.critical(None,
                                        "Permission error", 
                                        "Could not save - file already in use!",
                                        qtw.QMessageBox.Cancel)

class HtmlGenerator():
    """
    Holds the functions which generate html for JsonLibraryManager and
    JsonBoardsManager.
    """

    def get_versions(self, name, my_dict):
        """
        Returns all of the versions that are avaliable.
        """

        return list(my_dict[name]["version"])

    def get_title(self, name):
        """
        Returns the formatting for a title on the QTextBrowser of libraries
        that can be installed.

        Args:
            name (string): the text for the title (name)
        """

        return f"<h1><p style=\"color:#00f0c3\">{name}</p></h1><br>"

    def get_link(self, link):
        """
        Returns the html link for categories which are links.

        Args:
            name (string): the link
        """

        return f"<a style=\"color:#8ab4f8\" href={link}>{link}</a><br>"

    def get_paragraph(self, name, text):
        """
        Makes a paragraph for each sub category

        Args:
            name (string): the name of the category
            text (string): the description
        """
        return f"<p>{name}: {text}</p>"

    def get_list_paragraph(self, name, my_list):
        """
        Makes a paragraph for each sub category

        Args:
            name (string): the name of the category
            list (list): the description
        """
        string = f"<p>{name}:"
        for item in my_list:
            string += f"<br>{item}"
        return string

    def get_html(self, name, my_dict):
        """
        Formats the library text for the display on library manager options
        
        Args:
            name (str): the name of the dictionary item
            my_dict (dictionary): the dictionary to parse into html
        """
        html = self.get_title(name)

        for item in list(my_dict[name].keys()):
            info = my_dict[name][item]

            if item == "version":
                continue
            if item in ("repository", "url", "website"):
                html += self.get_link(str(info))
            elif isinstance(info, list):
                html += self.get_list_paragraph(item, info)
            elif isinstance(item, str):
                html += self.get_paragraph(item, str(info))

        return html


class JsonLibraryManager(HtmlGenerator):
    """
    Json loader class that gets all information for the arduino
    library manager.
    """

    def __init__(self, path):

        self.lib_path = path
        self.libraries = {}
        self.load_libs()
        #self.get_info(list(self.libraries.keys())[0])

    def load_libs(self):
        """
        Loads all libraries from the library.json file in arduino15.
        """
        with open(self.lib_path, encoding="utf-8") as file:
            data = json.load(file)

        libraries = data.get("libraries")
        for library in libraries:
            if library["name"] in self.libraries:
                self.libraries[library["name"]]["version"].append(library["version"])
            else:
                self.libraries[library["name"]] = library
                self.libraries[library["name"]]["version"] = [
                    self.libraries[library["name"]]["version"]]

    def get_all_libraries(self, name):
        """
        Returns all keys with the name in them.

        Args:
            name (string): the keyword to look for in the name
        """

        keys = list(self.libraries.keys())

        libraries = []

        for key in keys:
            if name.lower() in key.lower():
                libraries.append(key)

        return libraries

class JsonBoardsManager(HtmlGenerator):
    """
    Processes and parses the boards json file.
    """
    def __init__(self, path):

        self.board_path = path
        self.boards = {}
        self.load_boards()

    def format_dict(self, input_dict):
        """
        Formats the dictionary into a better form to be displayed
        on the screen.

        Args:
            dict (dictionary) : The dictionary to be formatted
        """
        formatted_dict = {"architecture": input_dict["architecture"],
        "version": [input_dict["version"]],
        "url": input_dict["url"],
        "boards": [board["name"] for board in input_dict["boards"]]}

        return formatted_dict

    def load_boards(self):
        """
        Loads all libraries from the library.json file in arduino15.
        """
        with open(self.board_path, encoding="utf-8") as file:
            data = json.load(file)

        packages = data.get("packages")

        for package in packages:
            for board in package["platforms"]:
                if board["name"].startswith("[DEPRECATED"):
                    continue
                if board["name"] in self.boards:
                    self.boards[board["name"]]["version"].append(board["version"])
                else:
                    board["architecture"] = package["name"] + ":" + board["architecture"]
                    self.boards[board["name"]] = self.format_dict(board)
                    self.boards[board["name"]].update({"maintainer":package["maintainer"]})


class FileManager(JsonLibraryManager, JsonBoardsManager):
    """
    All processing to do with OS information such as file directorys, saves and more

    Attributes:
        user (str): the logged in user to the system
        path (str): the path of the main file being run
        script_ending (str): exe or sh depending on OS
        operating_system (str): the operating system the app is run on
        sep (str): the seperator for file directories
        save_manager (SaveManager): the class responsible for saving
        paths (str): the different necessary paths

    Methods:
    """

    def __init__(self, dev, consci_os_path):

        operating_system = platform.system()

        self.user = os.getenv("USER") or os.getenv("USERNAME")
        self.path = os.path.dirname(os.path.realpath(__file__))

        if "_internal" in self.path:
            self.path = str(Path(self.path).resolve().parent)

        self.save_manager = SaveManager()
        self.dev = dev
        self.consci_os_path = consci_os_path
        self.current_project = ""

        self.board_names = []
        self.updater_moved = False

        # Initialise for each OS
        if operating_system == "Windows":
            self.arduino_cli = "arduino-cli-windows.exe"
            self.sep = "\\"
            inc = "C:\\Users\\"
            documents = "Documents"

            arduino_lib_path = f"{inc}{self.user}{self.sep}\
AppData{self.sep}Local{self.sep}Arduino15{self.sep}library_index.json"

            arduino_board_path = f"{inc}{self.user}{self.sep}\
AppData{self.sep}Local{self.sep}Arduino15{self.sep}package_index.json"

        elif operating_system == "Darwin":
            self.arduino_cli = "arduino-cli-mac"
            self.sep = "/"
            inc = "/Users/"
            documents = "documents"

            arduino_lib_path = f"{inc}{self.user}{self.sep}\
Library{self.sep}Arduino15{self.sep}library_index.json"

            arduino_board_path = f"{inc}{self.user}{self.sep}\
Library{self.sep}Arduino15{self.sep}package_index.json"

        elif operating_system == "Linux":
            self.arduino_cli = "arduino-cli-linux.sh"
            self.sep = "/"
            inc = "/home/"
            documents = "Documents"

            arduino_lib_path = f"{inc}{self.user}{self.sep}.arduino15\
{self.sep}library_index.json"

            arduino_board_path = f"{inc}{self.user}{self.sep}.arduino15\
{self.sep}package_index.json"

        else:
            raise OSError("Invalis OS. Shutting down.")

        self.paths = {}

        # Definitions for paths which are referenced for file locations
        self.paths["documents"] = f"{inc}{self.user}{self.sep}{documents}"
        self.paths["sidekick"] = f"""{self.paths["documents"]}{self.sep}Sight"""

        if operating_system == "Windows":
            self.paths["appdata"] = f"{inc}{self.user}{self.sep}AppData{self.sep}Local"
            self.paths["settings_path"] = f"""{self.paths["appdata"]}{self.sep}\
Sight{self.sep}Settings"""
        else:
            # TODO make application follow normal file directories for Linux\unix
            self.paths["appdata"] = f"{self.path}"
            self.paths["settings_path"] = f"""{self.paths["appdata"]}{self.sep}Settings"""

        self.define_paths()

        # Create a save manager object as the user may want to record data
        self.save_manager.save_folder_path = f"""{self.paths["sidekick"]}{self.sep}Saves"""
        self.save_manager.sep = self.sep

        # Creates directories if not already
        self.create_sidekick_files()
        self.create_sub_sidekick_files()

        # Checks if the GUI is being used in dev mode
        if dev:
            print("<<< WARNING >>> THIS APP IS CURRENTLY IN DEVELOPMENT MODE")
            self.move_libraries(consci_os_path)
        elif len(os.listdir(self.paths["libraries"])) == 0:
            self.move_libraries()

        self.load_boards_csv()
        self.update = True

        super(FileManager, self).__init__(arduino_lib_path)
        super(JsonLibraryManager, self).__init__(arduino_board_path)

    def define_paths(self):
        """
        Create all of the paths that will be used by the file manager.
        """
        # Definitions of file locations
        self.paths["boards"] = f"""{self.paths["settings_path"]}\
{self.sep}boards.csv"""
        self.paths["settings"] = f"""{self.paths["settings_path"]}\
{self.sep}settings.txt"""
        self.paths["stylesheet"] = f"""{self.paths["settings_path"]}\
{self.sep}stylesheet.qss"""
        self.paths["arduino"] = f"{self.path}{self.sep}Externals{self.sep}\
{self.arduino_cli}"
        self.paths["actuator"] = f"""{self.path}{self.sep}Examples\
{self.sep}Actuators_Test{self.sep}Actuators_Test.ino"""
        self.paths["stylesheet_template"] = f"""{self.path}{self.sep}Settings\
{self.sep}stylesheet.qss"""
        self.paths["conscios"] = f"""{self.paths["appdata"]}{self.sep}Sight{self.sep}ConsciOS"""
        self.paths["conscios_src"] = f"""{self.paths["conscios"]}{self.sep}Source"""
        self.paths["conscios_src_lite"] = f"""{self.paths["conscios"]}{self.sep}Source_lite"""
        self.paths["conscios_lib"] = f"""{self.paths["conscios"]}{self.sep}libraries"""
        self.paths["updater"] = f"""{self.path}{self.sep}updater"""
        self.paths["updater_des"] = f"""{self.paths["appdata"]}{self.sep}Sight{self.sep}updater"""
        self.paths["update_exe"] = f"""{self.paths["updater_des"]}{self.sep}update_manager.exe"""

        # User accessible files
        self.paths["projects"] = f"""{self.paths["sidekick"]}{self.sep}Projects"""
        self.paths["libraries"] = f"""{self.paths["sidekick"]}{self.sep}Libraries"""

    def create_sidekick_files(self):
        """
        Creates sidekick directory in documents if it does not already exist
        TODO tidy this up
        """
        directories = os.listdir(self.paths["documents"])
        if "Sight" not in directories:
            os.mkdir(self.paths["sidekick"])

        directories = os.listdir(self.paths["appdata"])
        if "Sight" not in directories:
            os.makedirs(self.paths["settings_path"])

        if not os.path.exists(self.paths["conscios"]):
            self.install_conscios()

    def create_sub_sidekick_files(self):
        """
        Creates SideKick sub directories (Projects, SavedData, Libraries) if
        they do not already exist.
        """

        directories = os.listdir(self.paths["sidekick"])

        if "Projects" not in directories:
            os.mkdir(self.paths["projects"])
        if "Saves" not in directories:
            os.mkdir(self.save_manager.save_folder_path)
        if "Libraries" not in directories:
            os.mkdir(self.paths["libraries"])

        directories = os.listdir(self.paths["settings_path"])

        if "settings.txt" not in directories:
            with open(self.paths["settings"], "x", encoding="UTF-8") as settings:
                settings.write(DEFAULT_SETTINGS)

        if "boards.csv" not in directories:
            with open(self.paths["boards"], "x", encoding="UTF-8") as _:
                pass
            self.update_boards()

        if "stylesheet.qss" not in directories:
            shutil.copy(self.paths["stylesheet_template"], self.paths["stylesheet"])

    def install_conscios(self):
        """
        Using git, if there is no ConsciOS available, clone it.
        """
        clone(CONSCIOS_GIT, self.paths["conscios"])

    def move_source(self, raw_source):
        """
        If the GUI is in dev mode, replace the reference to the source code
        for new projects
        """

        try:
            shutil.rmtree(self.paths["conscios_lib"])
            shutil.rmtree(self.paths["conscios_src"])
        except FileNotFoundError:
            pass

        source = f"{raw_source}{self.sep}libraries"

        shutil.copytree(source, self.paths["conscios_lib"])

        source = f"{raw_source}{self.sep}Source"

        shutil.copytree(source, self.paths["conscios_src"])

    def move_libraries(self, source=None):
        """
        If the ConsciOS libraries are not present, then we need to copy them from ConsciOS
        Or if the app is being used in development mode

        Args:
            source (str): the source to the new libraries
        """

        if "libraries" not in os.listdir(self.paths["libraries"]):
            os.mkdir(f"""{self.paths["libraries"]}{self.sep}libraries""")

        destination = f"""{self.paths["libraries"]}{self.sep}libraries"""

        if source is None:
            source = self.paths["conscios_lib"]
        else:
            source += f"{self.sep}libraries"

        for library in os.listdir(source):
            if "." in library:
                continue

            if library in os.listdir(destination):
                shutil.rmtree(f"{destination}{self.sep}{library}")

            shutil.copytree(f"{source}{self.sep}{library}", f"{destination}{self.sep}{library}")

    def get_all_projects(self):
        """
        Gets all projects in the "SK Projects" folder.

        Returns:
            list: a list of all the projects
        """
        return os.listdir(self.paths["projects"])

    def get_all_saves(self):
        """
        Gets all saves in the "SavedData" folder.

        Returns:
            list: a list of all saves
        """
        return os.listdir(self.save_manager.save_folder_path)

    def add_new_project(self, project_dir, sk_lite):
        """
        Adds new projects when new project is clicked.
        Creates a new file, copies the source reference, then renames the .ino file

        Args:
            name (string): the name of the new project from the line edit
            sk_lite (bool): whether or not to create only a .ino file
        """
        project_dir = project_dir.replace("/", self.sep)

        destination = f"{project_dir}"

        if not sk_lite:
            shutil.copytree(self.paths["conscios_src"], destination)
        else:
            shutil.copytree(self.paths["conscios_src_lite"], destination)

        os.rename(f"{project_dir}{self.sep}Source.ino",
                  f"{project_dir}{self.sep}{project_dir.split(self.sep)[-1]}.ino")

        self.set_current_project(
            f"{project_dir}{self.sep}{project_dir.split(self.sep)[-1]}.ino",
            True )

    def remove_project(self, name):
        """
        Deletes project

        Args:
            name (str): the project name
        """
        shutil.rmtree(f"""{self.paths["projects"]}{self.sep}{name}""")

    def get_cli_path(self):
        """
        Returns:
            string: the path to arduino cli
        """
        return f"""\"{self.paths["arduino"]}\""""

    def set_dev_file(self):
        """
        Compiles and uploads the script
        sets the current_project to the dev project
        """

        if self.dev:
            self.move_libraries(f"{self.consci_os_path}")
            self.current_project = f"{self.consci_os_path}{self.sep}Source{self.sep}Source.ino"

    def save_options(self, board, project, lite):
        """
        Saves selected options in drop downs to the settings.txt file so
        that the user doesn"t need to keep selecting drop downs on startup

        Args:
            board (string): the board type e.g. SK_Stem, Teensy4.1
            project (string): the current project selected
        """

        with open(self.paths["settings"], "r", encoding="UTF-8") as settings_file:

            settings = settings_file.readlines()

        for item in settings:

            if "Board: " in item:
                board_index = settings.index(item)
                settings[board_index] = f"Board: {board}\n"

            elif "Project: " in item:
                project_index = settings.index(item)
                settings[project_index] = f"Project: {project}\n"

            elif "Lite: " in item:
                lite_index = settings.index(item)
                settings[lite_index] = f"Lite: {lite}\n"

        with open(self.paths["settings"], "w", encoding="UTF-8") as settings_file:
            settings_file.writelines(settings)

    def load_options(self):
        """
        Loads the saved options to set the drop down box items

        Returns:
            board (string): the board type e.g. SK_Stem, Teensy4.1
            project (string): the current project selected
        """

        board = None
        project = None
        lite = None

        in_drop_down_section = False

        with open(self.paths["settings"], "r", encoding="UTF-8") as settings:

            for line in settings:

                if "Drop down options:" in line:
                    in_drop_down_section = True

                if in_drop_down_section:
                    if "Board: " in line:
                        board = line.replace("Board: ", "")
                        board = board.strip()
                    elif "Project: " in line:
                        project = line.replace("Project: ", "")
                        project = project.strip()
                    elif "Lite: " in line:
                        lite = line.replace("Lite: ", "")
                        lite = lite.strip()
                        if lite == "False":
                            lite = False
                        else:
                            lite = True

        if lite is None:
            with open(self.paths["settings"], "a", encoding="UTF-8") as settings:
                settings.write("Lite: False")
                lite = False

        if not os.path.exists(project):
            if len(os.listdir(self.paths["projects"])) > 0:
                project_name = os.listdir(self.paths["projects"])[0]
                project = f"""{self.paths["projects"]}{self.sep}{project_name}"""
                project += f"{self.sep}{project_name}.ino"
                project = project.replace("\\", "/")
            else:
                project = ""

        return board, project, lite

    def load_boards_csv(self):
        """
        Gets all of the boards from ./Ui/boards.csv so
        that they can be displayed on the GUI.
        """
        # TODO speed this up.
        with open(self.paths["boards"], "r", encoding="UTF-8") as boards:
            for line in boards:
                self.board_names.append(line.strip().split(", "))

    def set_current_project(self, file_path, manual=False):
        """
        Sets the current_project variable

        Args:
            file_path (str): the file path to the .ino file
        """

        if manual:
            self.current_project = file_path.replace("\\", "/")
            return

        try:
            if self.sep != "\\":
                self.current_project = file_path.split(self.sep)[-2]
            else:
                self.current_project = file_path.split("/")[-2]

            self.current_project = file_path
        except IndexError:
            pass

    def parsed_project_name(self):
        """
        Removes all of the file directory info from the name

        Returns:
            str: the name to be displayed on the GUI
        """

        try:
            if self.sep != "\\":
                name = self.current_project.split(self.sep)[-2]
            else:
                name = self.current_project.split("/")[-2]
        except IndexError:
            name = ""

        return name

    def set_all_boards(self, cli_manager:str):
        """
        Args:
            cli_magaer (CliManager) : the cli manager that runs commands
        """
        self.board_names = DEFAULT_BOARDS
        boards_str = cli_manager.get_cmd_output("board listall")

        boards_list = []
        for item in boards_str.decode("UTF-8").split("\n"):
            if item:
                boards_list.append(item.strip().split("  "))

        for item in boards_list:
            self.board_names.append([x for x in item if x])

        self.board_names.pop(2)

        self.update_boards()

    def update_boards(self):
        """
        Updates the boards.csv file to include all of the new boards
        """

        self.update = True

        with open(self.paths["boards"], "w", encoding="UTF-8") as boards:
            for board in self.board_names:
                if len(board) > 1:
                    boards.write(f"{board[0]}, {board[1]}\n")

    def get_examples(self):
        """
        Get all of the arduino sketches from the libraries path.

        Returns:
            list: the fild directories of the arduino examples.
        """
        libraries_path = self.paths["libraries"]+f"{self.sep}libraries"
        files = os.listdir(libraries_path)
        examples = []
        for file in files:
            if os.path.isfile(libraries_path+f"{self.sep}{file}"):
                continue
            if "examples" not in os.listdir(libraries_path+f"{self.sep}{file}"):
                continue
            examples.append(file)
        return examples

    def change_size_stylesheet(self, increase:bool):
        """
        Either increases or decreases the size of the font on the GUI.
        """
        with open(
            self.paths["stylesheet"],
            "r",
            encoding="UTF-8") as sizes:
            scale = float(sizes.readline())
            stylesheet = sizes.read()

        if increase:
            scale += 0.1
            scale = round(scale, 1)
            if scale == 0.7:
                scale = 0.8
            elif scale == 1.2:
                scale = 1.3
            elif scale == 1.7:
                scale = 1.8
            elif scale == 2.1:
                scale = 2.2
            scale = min(scale, 2.3)
        else:
            scale -=0.1
            scale = round(scale, 1)
            if scale == 0.7:
                scale = 0.6
            elif scale == 1.2:
                scale = 1.1
            elif scale == 1.7:
                scale = 1.6
            elif scale == 2.1:
                scale = 2.0
            scale = max(scale, 0.5)

        with open(
            self.paths["stylesheet"],
            "w",
            encoding="UTF-8") as sizes:
            scale = round(scale, 1)
            sizes.write(str(scale)+"\n"+stylesheet)

    def get_scale(self) -> float:
        """
        Gets the scale from the stylesheet.
        """
        with open(
            self.paths["stylesheet"],
            "r",
            encoding="UTF-8") as scale:
            return float(scale.readline())

    def get_size_stylesheet(self) -> tuple:
        """
        Gets and formats the size style guide for the GUI.
        """

        with open(
            self.paths["stylesheet"],
            "r",
            encoding="UTF-8") as sizes:
            scale = float(sizes.readline())
            stylesheet = sizes.read()

        for size in SIZES_IN_QSS:
            stylesheet = stylesheet.replace(str(size) + "px", str(int(size*scale))+ "px")

        return stylesheet, scale

    def is_installed(self):
        """
        Check if sight is installed.
        """
        return "sight.exe" in os.listdir(self.path)

    def is_latest_version(self):
        """
        Check from git if the app is running in the latest version.

        Returns:
            bool: whether or not the app is running in the latest version
        """
        try:
            response = requests.get(VERSION, timeout=5)
            response.raise_for_status()
        except Exception:
            return True

        # Get the latest version
        latest_version = response.text.strip().split(".")

        with open(f"{self.path}{self.sep}version.txt", "r", encoding="UTF-8") as version:
            current_version = version.readline().split(".")

        # Compare the latest to the current version
        for latest, current in zip(latest_version, current_version):
            if int(latest) > int(current):
                return False
            elif int(latest) < int(current):
                return True
        return True

    def progress_copy(self, src, dst, progress):
        shutil.copy2(src, dst)
        progress["copied"] += 1
        print(f"Progress: {progress['copied']}/{progress['total']} files copied", end="\r")

    def copytree_with_progress(self, src, dst):
        total_files = sum(len(files) for _, _, files in os.walk(src))
        progress = {"copied": 0, "total": total_files}

        shutil.copytree(src, dst, copy_function=lambda s, d: self.progress_copy(s, d, progress))

        print("\nCopy completed!")
        
    def move_updater(self):
        """
        To run the updater, it must be moved to the appdata folder to have access.
        """
        self.updater_moved = False
        print("deleting")
        if os.path.exists(self.paths["updater_des"]):
            shutil.rmtree(self.paths["updater_des"])

        print("copying")
        print(self.paths["updater_des"])
        print("copying updater")
        self.copytree_with_progress(self.paths["updater"], self.paths["updater_des"])
        print("copied updater")
        self.updater_moved = True

        self.update_app()

    def update_app(self):
        """
        Remove the destination directory and clone the git repo.
        """
        subprocess.Popen([self.paths["update_exe"]] + [self.path, self.sep],
                         creationflags= 0x00000008,
                         close_fds=True)
