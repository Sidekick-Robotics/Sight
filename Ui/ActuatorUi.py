# Form implementation generated from reading ui file '.\ActuatorUi.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 526)
        MainWindow.setMinimumSize(QtCore.QSize(750, 464))
        MainWindow.setStyleSheet("QScrollBar\n"
"{\n"
"    width: 20px;\n"
"    border:none;\n"
"    border-radius: 10px;\n"
"    background: #32323C;\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page \n"
"{\n"
"    background-color: #32323C;\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line \n"
"{\n"
"    background-color: #32323C;\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"    background-color: grey;\n"
"    min-height: 30px;\n"
"    border-radius: 10px;\n"
"    border:none;\n"
"}\n"
"QScrollBar::up-arrow\n"
"{\n"
"    background: none;\n"
"}\n"
"QScrollBar::down-arrow\n"
"{\n"
"    background: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loading = QtWidgets.QFrame(parent=self.centralwidget)
        self.loading.setObjectName("loading")
        self.loading_screen = QtWidgets.QVBoxLayout(self.loading)
        self.loading_screen.setObjectName("loading_screen")
        self.uploading_screen = QtWidgets.QTextBrowser(parent=self.loading)
        self.uploading_screen.setStyleSheet("")
        self.uploading_screen.setObjectName("uploading_screen")
        self.loading_screen.addWidget(self.uploading_screen)
        self.progressBar = QtWidgets.QProgressBar(parent=self.loading)
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"    border: solid grey;\n"
"    border-radius: 15px;\n"
"    color: black;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #00f0c3;\n"
"    border-radius:15px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.loading_screen.addWidget(self.progressBar)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.loading_screen.addItem(spacerItem)
        self.verticalLayout.addWidget(self.loading)
        self.options_widget = QtWidgets.QFrame(parent=self.centralwidget)
        self.options_widget.setObjectName("options_widget")
        self.temp = QtWidgets.QHBoxLayout(self.options_widget)
        self.temp.setObjectName("temp")
        self.name = QtWidgets.QLineEdit(parent=self.options_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setObjectName("name")
        self.temp.addWidget(self.name)
        self.pin = QtWidgets.QLineEdit(parent=self.options_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pin.sizePolicy().hasHeightForWidth())
        self.pin.setSizePolicy(sizePolicy)
        self.pin.setObjectName("pin")
        self.temp.addWidget(self.pin)
        self.min = QtWidgets.QLineEdit(parent=self.options_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min.sizePolicy().hasHeightForWidth())
        self.min.setSizePolicy(sizePolicy)
        self.min.setObjectName("min")
        self.temp.addWidget(self.min)
        self.max = QtWidgets.QLineEdit(parent=self.options_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max.sizePolicy().hasHeightForWidth())
        self.max.setSizePolicy(sizePolicy)
        self.max.setObjectName("max")
        self.temp.addWidget(self.max)
        self.type = QtWidgets.QComboBox(parent=self.options_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.temp.addWidget(self.type)
        self.add = QtWidgets.QPushButton(parent=self.options_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setObjectName("add")
        self.temp.addWidget(self.add)
        self.verticalLayout.addWidget(self.options_widget)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 895, 70))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name_1 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.name_1.setMinimumSize(QtCore.QSize(100, 50))
        self.name_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.name_1.setObjectName("name_1")
        self.horizontalLayout_2.addWidget(self.name_1)
        self.value = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents)
        self.value.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.value.setObjectName("value")
        self.horizontalLayout_2.addWidget(self.value)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.upload = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload.sizePolicy().hasHeightForWidth())
        self.upload.setSizePolicy(sizePolicy)
        self.upload.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.upload.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.upload.setObjectName("upload")
        self.horizontalLayout_6.addWidget(self.upload)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Actuator Test"))
        self.uploading_screen.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto \'; font-size:14px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto \'; font-size:14px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto \'; font-size:14px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto \'; font-size:14pt; font-weight:600;\">Uploading sketch please wait</span></p></body></html>"))
        self.type.setItemText(0, _translate("MainWindow", "Servo"))
        self.type.setItemText(1, _translate("MainWindow", "Pin"))
        self.add.setText(_translate("MainWindow", "Add Actuator"))
        self.name_1.setText(_translate("MainWindow", "   All   "))
        self.upload.setText(_translate("MainWindow", "Upload Tester"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
