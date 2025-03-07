# Form implementation generated from reading ui file '.\GraphingUi.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1303, 785)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_grid = QtWidgets.QGridLayout()
        self.main_grid.setContentsMargins(0, 0, 0, 20)
        self.main_grid.setSpacing(0)
        self.main_grid.setObjectName("main_grid")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.main_grid.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.main_grid.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.main_grid.addItem(spacerItem2, 4, 3, 1, 1)
        self.home_screen = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_screen.sizePolicy().hasHeightForWidth())
        self.home_screen.setSizePolicy(sizePolicy)
        self.home_screen.setObjectName("home_screen")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.home_screen)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.terminal_container = QtWidgets.QWidget(parent=self.home_screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal_container.sizePolicy().hasHeightForWidth())
        self.terminal_container.setSizePolicy(sizePolicy)
        self.terminal_container.setStyleSheet("")
        self.terminal_container.setObjectName("terminal_container")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.terminal_container)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.terminal = QtWidgets.QTextEdit(parent=self.terminal_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.terminal.sizePolicy().hasHeightForWidth())
        self.terminal.setSizePolicy(sizePolicy)
        self.terminal.setStyleSheet("")
        self.terminal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.terminal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.terminal.setObjectName("terminal")
        self.gridLayout_4.addWidget(self.terminal, 2, 2, 1, 1)
        self.title = QtWidgets.QLabel(parent=self.terminal_container)
        self.title.setObjectName("title")
        self.gridLayout_4.addWidget(self.title, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 2, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout_4.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.terminal_container, 0, 1, 3, 1)
        self.bottom_widget = QtWidgets.QWidget(parent=self.home_screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom_widget.sizePolicy().hasHeightForWidth())
        self.bottom_widget.setSizePolicy(sizePolicy)
        self.bottom_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.bottom_widget.setStyleSheet("")
        self.bottom_widget.setObjectName("bottom_widget")
        self.gridLayout_3.addWidget(self.bottom_widget, 2, 3, 1, 1)
        self.top_widget = QtWidgets.QWidget(parent=self.home_screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_widget.sizePolicy().hasHeightForWidth())
        self.top_widget.setSizePolicy(sizePolicy)
        self.top_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.top_widget.setStyleSheet("")
        self.top_widget.setObjectName("top_widget")
        self.gridLayout_3.addWidget(self.top_widget, 0, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem6, 1, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 1, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_3.addItem(spacerItem10, 3, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(3, 3)
        self.main_grid.addWidget(self.home_screen, 2, 2, 1, 1)
        self.top_bar = QtWidgets.QFrame(parent=self.centralwidget)
        self.top_bar.setStyleSheet("/*General Styling*/\n"
"* {\n"
"  background-color: #25252f;\n"
"}\n"
"\n"
"/*Button Styling*/\n"
"\n"
"QPushButton:hover:!pressed{\n"
"  background-color: #151525;\n"
"}")
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file = QtWidgets.QPushButton(parent=self.top_bar)
        self.file.setMinimumSize(QtCore.QSize(0, 0))
        self.file.setObjectName("file")
        self.horizontalLayout.addWidget(self.file)
        self.device = QtWidgets.QPushButton(parent=self.top_bar)
        self.device.setMinimumSize(QtCore.QSize(0, 0))
        self.device.setObjectName("device")
        self.horizontalLayout.addWidget(self.device)
        self.upload = QtWidgets.QPushButton(parent=self.top_bar)
        self.upload.setMinimumSize(QtCore.QSize(0, 0))
        self.upload.setObjectName("upload")
        self.horizontalLayout.addWidget(self.upload)
        self.compile = QtWidgets.QPushButton(parent=self.top_bar)
        self.compile.setMinimumSize(QtCore.QSize(0, 0))
        self.compile.setObjectName("compile")
        self.horizontalLayout.addWidget(self.compile)
        self.com_ports = QtWidgets.QComboBox(parent=self.top_bar)
        self.com_ports.setMinimumSize(QtCore.QSize(0, 0))
        self.com_ports.setObjectName("com_ports")
        self.horizontalLayout.addWidget(self.com_ports)
        self.record = QtWidgets.QPushButton(parent=self.top_bar)
        self.record.setMinimumSize(QtCore.QSize(0, 0))
        self.record.setObjectName("record")
        self.horizontalLayout.addWidget(self.record)
        self.record_light = QtWidgets.QLabel(parent=self.top_bar)
        self.record_light.setText("")
        self.record_light.setObjectName("record_light")
        self.horizontalLayout.addWidget(self.record_light)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.top_update = QtWidgets.QLabel(parent=self.top_bar)
        self.top_update.setMinimumSize(QtCore.QSize(400, 0))
        self.top_update.setMaximumSize(QtCore.QSize(400, 16777215))
        self.top_update.setText("")
        self.top_update.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.top_update.setObjectName("top_update")
        self.horizontalLayout.addWidget(self.top_update)
        self.help = QtWidgets.QPushButton(parent=self.top_bar)
        self.help.setMinimumSize(QtCore.QSize(0, 0))
        self.help.setObjectName("help")
        self.horizontalLayout.addWidget(self.help)
        self.main_grid.addWidget(self.top_bar, 0, 0, 1, 4)
        self.debugger = QtWidgets.QFrame(parent=self.centralwidget)
        self.debugger.setObjectName("debugger")
        self.gridLayout = QtWidgets.QGridLayout(self.debugger)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem13, 1, 0, 1, 1)
        self.debugger_coloured = QtWidgets.QFrame(parent=self.debugger)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.debugger_coloured.sizePolicy().hasHeightForWidth())
        self.debugger_coloured.setSizePolicy(sizePolicy)
        self.debugger_coloured.setStyleSheet("")
        self.debugger_coloured.setObjectName("debugger_coloured")
        self.debugger_1 = QtWidgets.QGridLayout(self.debugger_coloured)
        self.debugger_1.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.debugger_1.setContentsMargins(-1, 0, -1, -1)
        self.debugger_1.setObjectName("debugger_1")
        self.full_screen = QtWidgets.QPushButton(parent=self.debugger_coloured)
        self.full_screen.setStyleSheet("")
        self.full_screen.setObjectName("full_screen")
        self.debugger_1.addWidget(self.full_screen, 1, 1, 1, 1)
        self.quit = QtWidgets.QPushButton(parent=self.debugger_coloured)
        self.quit.setStyleSheet("")
        self.quit.setObjectName("quit")
        self.debugger_1.addWidget(self.quit, 1, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.debugger_1.addItem(spacerItem14, 1, 0, 1, 1)
        self.debug_log = QtWidgets.QTextBrowser(parent=self.debugger_coloured)
        self.debug_log.setMinimumSize(QtCore.QSize(0, 150))
        self.debug_log.setStyleSheet("")
        self.debug_log.setObjectName("debug_log")
        self.debugger_1.addWidget(self.debug_log, 2, 0, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.debugger_1.addItem(spacerItem15, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.debugger_coloured, 1, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout.addItem(spacerItem16, 2, 3, 1, 1)
        self.main_grid.addWidget(self.debugger, 3, 2, 1, 1)
        self.bottom_bar = QtWidgets.QFrame(parent=self.centralwidget)
        self.bottom_bar.setObjectName("bottom_bar")
        self._2 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(0)
        self._2.setObjectName("_2")
        spacerItem17 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self._2.addItem(spacerItem17)
        self.message = QtWidgets.QLineEdit(parent=self.bottom_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setObjectName("message")
        self._2.addWidget(self.message)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self._2.addItem(spacerItem18)
        self.bottom_update = QtWidgets.QLabel(parent=self.bottom_bar)
        self.bottom_update.setText("")
        self.bottom_update.setObjectName("bottom_update")
        self._2.addWidget(self.bottom_update)
        spacerItem19 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self._2.addItem(spacerItem19)
        self._2.setStretch(1, 2)
        self._2.setStretch(2, 1)
        self._2.setStretch(3, 1)
        self.main_grid.addWidget(self.bottom_bar, 4, 2, 1, 1)
        self.side_menu = QtWidgets.QFrame(parent=self.centralwidget)
        self.side_menu.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setMinimumSize(QtCore.QSize(300, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.side_menu.setStyleSheet("/*Button Styling*/\n"
"QPushButton{\n"
"  background-color: #25252f;\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"    background-color: #151525;\n"
"}\n"
"\n"
"/*Combo Box Styling*/\n"
"QComboBox {\n"
"  background-color: #25252f;\n"
"}\n"
"\n"
"")
        self.side_menu.setObjectName("side_menu")
        self.dhsgd = QtWidgets.QVBoxLayout(self.side_menu)
        self.dhsgd.setContentsMargins(20, -1, 20, -1)
        self.dhsgd.setObjectName("dhsgd")
        spacerItem20 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.dhsgd.addItem(spacerItem20)
        self.logo = QtWidgets.QLabel(parent=self.side_menu)
        self.logo.setMinimumSize(QtCore.QSize(0, 50))
        self.logo.setMaximumSize(QtCore.QSize(16777215, 50))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.dhsgd.addWidget(self.logo)
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.dhsgd.addItem(spacerItem21)
        self.device_settings = QtWidgets.QFrame(parent=self.side_menu)
        self.device_settings.setObjectName("device_settings")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.device_settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.device_settings)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tune_actuators = QtWidgets.QPushButton(parent=self.device_settings)
        self.tune_actuators.setObjectName("tune_actuators")
        self.verticalLayout.addWidget(self.tune_actuators)
        self.sensor_test = QtWidgets.QPushButton(parent=self.device_settings)
        self.sensor_test.setEnabled(False)
        self.sensor_test.setObjectName("sensor_test")
        self.verticalLayout.addWidget(self.sensor_test)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem22)
        self.label_5 = QtWidgets.QLabel(parent=self.device_settings)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.baud_rate = QtWidgets.QComboBox(parent=self.device_settings)
        self.baud_rate.setObjectName("baud_rate")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.baud_rate.addItem("")
        self.verticalLayout.addWidget(self.baud_rate)
        self.supported_boards = QtWidgets.QComboBox(parent=self.device_settings)
        self.supported_boards.setObjectName("supported_boards")
        self.verticalLayout.addWidget(self.supported_boards)
        self.boards_manager = QtWidgets.QPushButton(parent=self.device_settings)
        self.boards_manager.setObjectName("boards_manager")
        self.verticalLayout.addWidget(self.boards_manager)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem23)
        self.disconnect = QtWidgets.QPushButton(parent=self.device_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnect.sizePolicy().hasHeightForWidth())
        self.disconnect.setSizePolicy(sizePolicy)
        self.disconnect.setObjectName("disconnect")
        self.verticalLayout.addWidget(self.disconnect)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem24)
        self.dhsgd.addWidget(self.device_settings)
        self.settings = QtWidgets.QFrame(parent=self.side_menu)
        self.settings.setObjectName("settings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selected_project = QtWidgets.QLabel(parent=self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_project.sizePolicy().hasHeightForWidth())
        self.selected_project.setSizePolicy(sizePolicy)
        self.selected_project.setText("")
        self.selected_project.setScaledContents(True)
        self.selected_project.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.selected_project.setObjectName("selected_project")
        self.verticalLayout_2.addWidget(self.selected_project)
        self.select_project = QtWidgets.QPushButton(parent=self.settings)
        self.select_project.setObjectName("select_project")
        self.verticalLayout_2.addWidget(self.select_project)
        self.new_project = QtWidgets.QPushButton(parent=self.settings)
        self.new_project.setObjectName("new_project")
        self.verticalLayout_2.addWidget(self.new_project)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem25)
        self.label = QtWidgets.QLabel(parent=self.settings)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.show_save = QtWidgets.QPushButton(parent=self.settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_save.sizePolicy().hasHeightForWidth())
        self.show_save.setSizePolicy(sizePolicy)
        self.show_save.setMinimumSize(QtCore.QSize(0, 0))
        self.show_save.setObjectName("show_save")
        self.verticalLayout_2.addWidget(self.show_save)
        self.export_save = QtWidgets.QPushButton(parent=self.settings)
        self.export_save.setObjectName("export_save")
        self.verticalLayout_2.addWidget(self.export_save)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem26)
        self.label_4 = QtWidgets.QLabel(parent=self.settings)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.library_manager = QtWidgets.QPushButton(parent=self.settings)
        self.library_manager.setObjectName("library_manager")
        self.verticalLayout_2.addWidget(self.library_manager)
        self.arduino_cli = QtWidgets.QPushButton(parent=self.settings)
        self.arduino_cli.setObjectName("arduino_cli")
        self.verticalLayout_2.addWidget(self.arduino_cli)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem27)
        self.label_2 = QtWidgets.QLabel(parent=self.settings)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.data_points = QtWidgets.QSlider(parent=self.settings)
        self.data_points.setMaximum(5000)
        self.data_points.setProperty("value", 2500)
        self.data_points.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.data_points.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.data_points.setObjectName("data_points")
        self.verticalLayout_2.addWidget(self.data_points)
        self.sk_lite = QtWidgets.QPushButton(parent=self.settings)
        self.sk_lite.setObjectName("sk_lite")
        self.verticalLayout_2.addWidget(self.sk_lite)
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem28)
        self.dhsgd.addWidget(self.settings)
        spacerItem29 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.dhsgd.addItem(spacerItem29)
        self.main_grid.addWidget(self.side_menu, 2, 1, 3, 1)
        self.gridLayout_2.addLayout(self.main_grid, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sight"))
        self.terminal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto \'; font-size:14px;\"><br /></p></body></html>"))
        self.title.setText(_translate("MainWindow", "Terminal"))
        self.file.setText(_translate("MainWindow", "Menu"))
        self.device.setText(_translate("MainWindow", "Device"))
        self.upload.setText(_translate("MainWindow", "Upload"))
        self.compile.setText(_translate("MainWindow", "Verify"))
        self.record.setText(_translate("MainWindow", "Record"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.full_screen.setText(_translate("MainWindow", "Expand"))
        self.quit.setText(_translate("MainWindow", "x"))
        self.debug_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto \'; font-size:14px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Testing"))
        self.tune_actuators.setText(_translate("MainWindow", "Actuator Test"))
        self.sensor_test.setText(_translate("MainWindow", "Sensor Test"))
        self.label_5.setText(_translate("MainWindow", "Manage Boards"))
        self.baud_rate.setItemText(0, _translate("MainWindow", "115200"))
        self.baud_rate.setItemText(1, _translate("MainWindow", "57600"))
        self.baud_rate.setItemText(2, _translate("MainWindow", "38400"))
        self.baud_rate.setItemText(3, _translate("MainWindow", "9600"))
        self.boards_manager.setText(_translate("MainWindow", "Boards Manager"))
        self.disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.select_project.setText(_translate("MainWindow", "Select Project"))
        self.new_project.setText(_translate("MainWindow", "New Project"))
        self.label.setText(_translate("MainWindow", "Manage Saves"))
        self.show_save.setText(_translate("MainWindow", "Show Save"))
        self.export_save.setText(_translate("MainWindow", "Export Save"))
        self.label_4.setText(_translate("MainWindow", "Manage setup"))
        self.library_manager.setText(_translate("MainWindow", "Library Manager"))
        self.arduino_cli.setText(_translate("MainWindow", "Arduino CLI"))
        self.label_2.setText(_translate("MainWindow", "Advanced"))
        self.sk_lite.setText(_translate("MainWindow", "SideKick Lite:OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
