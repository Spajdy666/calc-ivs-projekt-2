# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 183)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(20, 100, 93, 28))
        self.addButton.setObjectName("addButton")
        self.subButton = QtWidgets.QPushButton(self.centralwidget)
        self.subButton.setGeometry(QtCore.QRect(110, 100, 93, 28))
        self.subButton.setObjectName("subButton")
        self.mulButton = QtWidgets.QPushButton(self.centralwidget)
        self.mulButton.setGeometry(QtCore.QRect(290, 100, 93, 28))
        self.mulButton.setObjectName("mulButton")
        self.divButton = QtWidgets.QPushButton(self.centralwidget)
        self.divButton.setGeometry(QtCore.QRect(200, 100, 93, 28))
        self.divButton.setObjectName("divButton")
        self.textField = QtWidgets.QLineEdit(self.centralwidget)
        self.textField.setGeometry(QtCore.QRect(140, 30, 113, 22))
        self.textField.setObjectName("textField")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.subButton.setText(_translate("MainWindow", "-"))
        self.mulButton.setText(_translate("MainWindow", "*"))
        self.divButton.setText(_translate("MainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())