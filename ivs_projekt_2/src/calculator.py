from PyQt5 import QtWidgets, QtCore
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
        
    def add(self):        
        a = int(self.lineEditInput1.text())
        b = int(self.lineEditInput2.text())
        self.lineEditResult.setText(str(MathLibrary.add(a,b)))

if __name__ == '__main__':                        
    import sys 
    print("LOEREE") 
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())         