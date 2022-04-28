from logging import exception
from PyQt5 import QtWidgets, QtCore
#from PyQt5.QtWidgets import QPushButton
from calc_GUI import Ui_mainWindow 
from mathlib import MathLibrary

from PyQt5.QtGui import *
#from PyQt5 import QTWidgets as qtw



class CalculatorWindow(QtWidgets.QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.buttonAdd.clicked.connect(self.add)
        self.buttonSub.clicked.connect(self.sub)
        self.buttonMul.clicked.connect(self.mul)
        self.buttonDiv.clicked.connect(self.div)
        
    def add(self):
        a = self.lineEditInput1.text()
        a=self.returnFloat(a)
        b = self.lineEditInput2.text()
        b=self.returnFloat(b)
        if a=="VALUE ERROR" or b=="VALUE ERROR":
            self.showErrorDialog("Input is not a number")
            return
        self.lineEditResult.setText(str(MathLibrary.add(a,b)))
        
    def sub(self):
        a = self.lineEditInput1.text()
        a=self.returnFloat(a)
        b = self.lineEditInput2.text()
        b=self.returnFloat(b)
        if a=="VALUE ERROR" or b=="VALUE ERROR":
            self.showErrorDialog("Input is not a number")
            return
        self.lineEditResult.setText(str(MathLibrary.subtract(a, b)))
        
    def mul(self):
        a = self.lineEditInput1.text()
        a=self.returnFloat(a)
        b = self.lineEditInput2.text()
        b=self.returnFloat(b)
        if a=="VALUE ERROR" or b=="VALUE ERROR":
            self.showErrorDialog("Input is not a number")
            return
        self.lineEditResult.setText(str(MathLibrary.multiply(a, b)))
        
    def div(self):
        a = self.lineEditInput1.text()
        a=self.returnFloat(a)
        b = self.lineEditInput2.text()
        b=self.returnFloat(b)
        if a=="VALUE ERROR" or b=="VALUE ERROR":
            self.showErrorDialog("Input is not a number")
            return
        self.lineEditResult.setText(str(MathLibrary.divide(a, b)))
        
    def returnFloat(self,a):
        number = a
        try:
            number = float(number)
            return number
        except ValueError:
            return "VALUE ERROR"
        
    def showErrorDialog(self,input):
        QtWidgets.QMessageBox.critical(self,"Error",input)    
        

if __name__ == '__main__':                        
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())         