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
        
        self.buttonPow.clicked.connect(self.pow)
        self.buttonRoot.clicked.connect(self.root)
        self.buttonFact.clicked.connect(self.fact)
        self.buttonLn.clicked.connect(self.ln)
        
        self.buttonEquals.clicked.connect(self.equals)
        
        self.buttonClear.clicked.connect(self.clearAll)
        
        self.buttonAns.clicked.connect(self.ans)
        
        self.buttonZero.clicked.connect(lambda: self.number(0))
        self.buttonOne.clicked.connect(lambda: self.number(1))
        self.buttonTwo.clicked.connect(lambda: self.number(2))
        self.buttonThree.clicked.connect(lambda: self.number(3))
        self.buttonFour.clicked.connect(lambda: self.number(4))
        self.buttonFive.clicked.connect(lambda: self.number(5))
        self.buttonSix.clicked.connect(lambda: self.number(6))
        self.buttonSeven.clicked.connect(lambda: self.number(7))
        self.buttonEight.clicked.connect(lambda: self.number(8))
        self.buttonNine.clicked.connect(lambda: self.number(9))
        
    def number(self,num):
        #print(num)
        current=self.lineEditInput1.text()
        next=current+str(num)
        self.lineEditInput1.setText(str(next))
        
    def ans(self):
        resultLine=self.lineEditResult.text()
        sides=resultLine.split('=')
        self.clearAll()
        self.lineEditInput1.setText(str(sides[1]))
        
    def clearAll(self):
        self.lineEditInput1.clear()
        self.lineEditInput2.clear()
        self.lineEditResult.clear()
        self.lineEditSign.clear()
                
    def add(self):
        self.lineEditSign.setText('+')
        return
        
    def sub(self):
        self.lineEditSign.setText('-')
        return
        
    def mul(self):
        self.lineEditSign.setText('*')
        return
        
    def div(self):
        self.lineEditSign.setText('/')
        return
            
    def pow(self):
        self.lineEditSign.setText('^')
        return
    
    def fact(self):
        self.lineEditSign.setText('!')
        return
        
    def root(self):
        self.lineEditSign.setText('√')
        return
        
    def ln(self):
        self.lineEditSign.setText("ln")
        return
    
    def equals(self):
        sign = self.lineEditSign.text()
        a = self.lineEditInput1.text()
        a=self.returnFloat(a)
        b = self.lineEditInput2.text()
        b=self.returnFloat(b)
        try:
            if sign=='^':
                result=MathLibrary.power(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='√':
                result=MathLibrary.root(a,b)
                resultLine = "{0}{1}{2}={3}".format(b,sign,a,result)
            elif sign=='!':
                result=MathLibrary.fact(a)
                resultLine = "{0}{1}={2}".format(a,sign,result)
            elif sign=="ln":
                result=MathLibrary.ln(a)
                resultLine = "{0}({1})={2}".format(sign,a,result)
            elif sign=='+':
                result=MathLibrary.add(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='-':
                result=MathLibrary.subtract(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='*':
                result=MathLibrary.multiply(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='/':
                result=MathLibrary.divide(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            self.lineEditResult.setText(str(resultLine))
        except ValueError as e:
            self.showErrorDialog(str(e))
    
        
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