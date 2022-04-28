# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdd.setGeometry(QtCore.QRect(150, 230, 93, 28))
        self.buttonAdd.setObjectName("buttonAdd")
        self.buttonSub = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSub.setGeometry(QtCore.QRect(240, 230, 93, 28))
        self.buttonSub.setObjectName("buttonSub")
        self.buttonMul = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMul.setGeometry(QtCore.QRect(330, 230, 93, 28))
        self.buttonMul.setObjectName("buttonMul")
        self.buttonDiv = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDiv.setGeometry(QtCore.QRect(420, 230, 93, 28))
        self.buttonDiv.setObjectName("buttonDiv")
        self.lineEditInput1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput1.setGeometry(QtCore.QRect(190, 180, 113, 22))
        self.lineEditInput1.setObjectName("lineEditInput1")
        self.lineEditInput2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput2.setGeometry(QtCore.QRect(360, 180, 113, 22))
        self.lineEditInput2.setObjectName("lineEditInput2")
        self.lineEditResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResult.setGeometry(QtCore.QRect(280, 290, 113, 22))
        self.lineEditResult.setObjectName("lineEditResult")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "RealRavers.txt kalkulačka"))
        self.buttonAdd.setText(_translate("mainWindow", "+"))
        self.buttonSub.setText(_translate("mainWindow", "-"))
        self.buttonMul.setText(_translate("mainWindow", "*"))
        self.buttonDiv.setText(_translate("mainWindow", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

