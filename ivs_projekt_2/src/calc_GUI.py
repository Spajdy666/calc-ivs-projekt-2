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
        mainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdd.setGeometry(QtCore.QRect(450, 350, 51, 51))
        self.buttonAdd.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonAdd.setObjectName("buttonAdd")
        self.buttonSub = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSub.setGeometry(QtCore.QRect(450, 300, 51, 51))
        self.buttonSub.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonSub.setObjectName("buttonSub")
        self.buttonMul = QtWidgets.QPushButton(self.centralwidget)
        self.buttonMul.setGeometry(QtCore.QRect(450, 250, 51, 51))
        self.buttonMul.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonMul.setObjectName("buttonMul")
        self.buttonDiv = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDiv.setGeometry(QtCore.QRect(450, 200, 51, 51))
        self.buttonDiv.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonDiv.setObjectName("buttonDiv")
        self.lineEditInput1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput1.setGeometry(QtCore.QRect(250, 140, 111, 31))
        self.lineEditInput1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInput1.setObjectName("lineEditInput1")
        self.lineEditInput2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInput2.setGeometry(QtCore.QRect(390, 140, 111, 31))
        self.lineEditInput2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditInput2.setObjectName("lineEditInput2")
        self.lineEditResult = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditResult.setGeometry(QtCore.QRect(250, 170, 251, 31))
        self.lineEditResult.setStyleSheet("")
        self.lineEditResult.setReadOnly(True)
        self.lineEditResult.setObjectName("lineEditResult")
        self.buttonEquals = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEquals.setGeometry(QtCore.QRect(450, 400, 51, 51))
        self.buttonEquals.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.buttonEquals.setObjectName("buttonEquals")
        self.buttonZero = QtWidgets.QPushButton(self.centralwidget)
        self.buttonZero.setGeometry(QtCore.QRect(250, 400, 101, 51))
        self.buttonZero.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonZero.setObjectName("buttonZero")
        self.buttonSeven = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSeven.setGeometry(QtCore.QRect(250, 250, 51, 51))
        self.buttonSeven.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonSeven.setObjectName("buttonSeven")
        self.buttonEight = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEight.setGeometry(QtCore.QRect(300, 250, 51, 51))
        self.buttonEight.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonEight.setObjectName("buttonEight")
        self.buttonNine = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNine.setGeometry(QtCore.QRect(350, 250, 51, 51))
        self.buttonNine.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonNine.setObjectName("buttonNine")
        self.buttonFive = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFive.setGeometry(QtCore.QRect(300, 300, 51, 51))
        self.buttonFive.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonFive.setObjectName("buttonFive")
        self.buttonFour = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFour.setGeometry(QtCore.QRect(250, 300, 51, 51))
        self.buttonFour.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonFour.setObjectName("buttonFour")
        self.buttonSix = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSix.setGeometry(QtCore.QRect(350, 300, 51, 51))
        self.buttonSix.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonSix.setObjectName("buttonSix")
        self.buttonTwo = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTwo.setGeometry(QtCore.QRect(300, 350, 51, 51))
        self.buttonTwo.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonTwo.setObjectName("buttonTwo")
        self.buttonOne = QtWidgets.QPushButton(self.centralwidget)
        self.buttonOne.setGeometry(QtCore.QRect(250, 350, 51, 51))
        self.buttonOne.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonOne.setObjectName("buttonOne")
        self.buttonThree = QtWidgets.QPushButton(self.centralwidget)
        self.buttonThree.setGeometry(QtCore.QRect(350, 350, 51, 51))
        self.buttonThree.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.buttonThree.setObjectName("buttonThree")
        self.buttonDot = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDot.setGeometry(QtCore.QRect(350, 400, 51, 51))
        self.buttonDot.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.buttonDot.setObjectName("buttonDot")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(300, 200, 101, 51))
        self.buttonClear.setStyleSheet("background-color: rgb(255, 100, 100);")
        self.buttonClear.setObjectName("buttonClear")
        self.lineEditSign = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSign.setGeometry(QtCore.QRect(360, 140, 31, 31))
        self.lineEditSign.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSign.setReadOnly(True)
        self.lineEditSign.setObjectName("lineEditSign")
        self.buttonRoot = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRoot.setGeometry(QtCore.QRect(400, 300, 51, 51))
        self.buttonRoot.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonRoot.setObjectName("buttonRoot")
        self.buttonPow = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPow.setGeometry(QtCore.QRect(400, 350, 51, 51))
        self.buttonPow.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonPow.setObjectName("buttonPow")
        self.buttonFact = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFact.setGeometry(QtCore.QRect(400, 250, 51, 51))
        self.buttonFact.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonFact.setObjectName("buttonFact")
        self.buttonLn = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLn.setGeometry(QtCore.QRect(400, 200, 51, 51))
        self.buttonLn.setStyleSheet("background-color: rgb(255, 238, 0);\n"
"")
        self.buttonLn.setObjectName("buttonLn")
        self.buttonHelp = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHelp.setGeometry(QtCore.QRect(250, 200, 51, 51))
        self.buttonHelp.setStyleSheet("background-color: rgb(199, 255, 255);")
        self.buttonHelp.setObjectName("buttonHelp")
        self.buttonAns = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAns.setGeometry(QtCore.QRect(400, 400, 51, 51))
        self.buttonAns.setStyleSheet("background-color: rgb(255, 220, 0);\n"
"")
        self.buttonAns.setObjectName("buttonAns")
        self.buttonSeven.raise_()
        self.buttonEight.raise_()
        self.buttonNine.raise_()
        self.buttonFour.raise_()
        self.buttonFive.raise_()
        self.buttonSix.raise_()
        self.buttonOne.raise_()
        self.buttonTwo.raise_()
        self.buttonThree.raise_()
        self.buttonZero.raise_()
        self.buttonDot.raise_()
        self.buttonLn.raise_()
        self.buttonDiv.raise_()
        self.buttonFact.raise_()
        self.buttonMul.raise_()
        self.buttonRoot.raise_()
        self.buttonPow.raise_()
        self.buttonSub.raise_()
        self.lineEditInput1.raise_()
        self.lineEditInput2.raise_()
        self.lineEditResult.raise_()
        self.buttonClear.raise_()
        self.lineEditSign.raise_()
        self.buttonHelp.raise_()
        self.buttonAdd.raise_()
        self.buttonAns.raise_()
        self.buttonEquals.raise_()
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
        self.buttonEquals.setText(_translate("mainWindow", "="))
        self.buttonZero.setText(_translate("mainWindow", "0"))
        self.buttonSeven.setText(_translate("mainWindow", "7"))
        self.buttonEight.setText(_translate("mainWindow", "8"))
        self.buttonNine.setText(_translate("mainWindow", "9"))
        self.buttonFive.setText(_translate("mainWindow", "5"))
        self.buttonFour.setText(_translate("mainWindow", "4"))
        self.buttonSix.setText(_translate("mainWindow", "6"))
        self.buttonTwo.setText(_translate("mainWindow", "2"))
        self.buttonOne.setText(_translate("mainWindow", "1"))
        self.buttonThree.setText(_translate("mainWindow", "3"))
        self.buttonDot.setText(_translate("mainWindow", ","))
        self.buttonClear.setText(_translate("mainWindow", "CA"))
        self.buttonRoot.setText(_translate("mainWindow", "√"))
        self.buttonPow.setText(_translate("mainWindow", "x^a"))
        self.buttonFact.setText(_translate("mainWindow", "!x"))
        self.buttonLn.setText(_translate("mainWindow", "ln(x)"))
        self.buttonHelp.setText(_translate("mainWindow", "?"))
        self.buttonAns.setText(_translate("mainWindow", "ANS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

