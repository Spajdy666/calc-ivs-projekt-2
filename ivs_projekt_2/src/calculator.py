import sys

from logging import exception
from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import Qt
#from PyQt5.QtWidgets import QPushButton
from calc_GUI import Ui_mainWindow 
from mathlib import MathLibrary

from PyQt5.QtGui import *
#from PyQt5 import QTWidgets as qtw

global focused
focused=1

global help
help=0

class CalculatorWindow(QtWidgets.QMainWindow,Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.setFocus()
        
        self.lineEditInput1.setFocus()
        #self.lineEditResult.selectionChanged.connect(lambda: self.lineEditResult.setSelection(0, 0))
        
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
        
        self.buttonHelp.clicked.connect(self.setHelp)
        
        self.buttonDot.clicked.connect(self.printDot)
        
    def printDot(self):
        global help
        if help==1:
            self.showInfoDialog("Klávesa přidá do daného textového pole desetinnou čárku, pokud již tam není")
            return
        if focused==1:
            current=self.lineEditInput1.text()
            if "." not in current:
                next=current+str(".")
                self.lineEditInput1.setText(str(next))
        elif focused==2:
            current=self.lineEditInput2.text()
            if "." not in current:
                next=current+str(".")
                self.lineEditInput2.setText(str(next))
        
    def setHelp(self):
        global help
        if help==1:
            help=0
        elif help==0:
            msg = """Vítejte v nápovědním režimu! Po kliknutí na dané tlačítko se zobrazí jeho popis!
Pro ukončení nápovědy stiskněte znovu toto tlačítko"""
            self.showInfoDialog(msg)
            help=1
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            self.add()
        elif event.key() == Qt.Key_Minus:
            self.sub()
        elif event.key() == Qt.Key_Asterisk:
            self.mul()
        elif event.key() == Qt.Key_Slash:
            self.div()
        elif event.key() == Qt.Key_Equal:
            self.equals()
        
    def changeFocus1(self):
        global focused
        focused=1
        #self.lineEditInput1.setFocus()
        
    def changeFocus2(self):
        global focused
        focused=2
        #self.lineEditInput1.setFocus()
        
    def number(self,num):
        global help
        if help==1:
            self.showInfoDialog("Numerická klávesa sloužící k číselnému vstupu")
            return
        if focused==1:
            current=self.lineEditInput1.text()
            next=current+str(num)
            self.lineEditInput1.setText(str(next))
        elif focused==2:
            current=self.lineEditInput2.text()
            next=current+str(num)
            self.lineEditInput2.setText(str(next))
        
    def ans(self):
        if help==1:
            self.showInfoDialog("Klávesa zkopíruje výsledek výrazu do pravého vstupu")
            return
        resultLine=self.lineEditResult.text()
        if resultLine!="":
            sides=resultLine.split('=')
            self.clearAll()
            self.lineEditInput1.setText(str(sides[1]))
            self.changeFocus1()
        
    def clearAll(self):
        if help==1:
            self.showInfoDialog("Klávesa vymaže obsahy všech textových polí")
            return
        self.lineEditInput1.clear()
        self.lineEditInput2.clear()
        self.lineEditResult.clear()
        self.lineEditSign.clear()
        self.changeFocus1()
                
    def add(self):
        if help==1:
            self.showInfoDialog("Klávesa vypočítá součet dvou čísel")
            return
        self.lineEditSign.setText('+')
        self.changeFocus2()
        return
        
    def sub(self):
        if help==1:
            self.showInfoDialog("Klávesa vypočítá rozdíl dvou čísel")
            return
        self.lineEditSign.setText('-')
        self.changeFocus2()
        return
        
    def mul(self):
        if help==1:
            self.showInfoDialog("Klávesa vypočítá součin dvou čísel")
            return
        self.lineEditSign.setText('*')
        self.changeFocus2()
        return
        
    def div(self):
        if help==1:
            self.showInfoDialog("Klávesa vypočítá podíl dvou čísel")
            return
        self.lineEditSign.setText('/')
        self.changeFocus2()
        return
            
    def pow(self):
        if help==1:
            self.showInfoDialog("Klávesa umocní číslo (vlevo) na daný exponent (vpravo)")
            return
        self.lineEditSign.setText('^')
        self.changeFocus2()
        return
    
    def fact(self):
        if help==1:
            self.showInfoDialog("Klávesa vypočítá faktoriál daného čísla (vlevo)")
            return
        self.lineEditSign.setText('!')
        return
        
    def root(self):
        if help==1:
            self.showInfoDialog("Klávesa vypočítá n-tou mocninu (vpravo) daného čísla (vlevo)")
            return
        self.lineEditSign.setText('√')
        self.changeFocus2()
        return
        
    def ln(self):
        if help==1:
            self.showInfoDialog("Klávesa vypočítá přirozený logaritmus čísla (vlevo)")
            return
        self.lineEditSign.setText("ln")
        return
    
    def equals(self):
        if help==1:
            self.showInfoDialog("Klávesa zobrazí výsledek dané matematické operace")
            return
        sign = self.lineEditSign.text()
        a = self.lineEditInput1.text()
        b = self.lineEditInput2.text()
        a=self.returnFloat(a)
        #b=self.returnFloat(b)
        if a=="WRONG_VALUE":
            self.showErrorDialog("Input is empty, or in bad format")
            return
        try:
            if sign=='^':
                b=self.returnFloat(b)
                if b == "WRONG_VALUE":
                    self.showErrorDialog("Input is empty, or in bad format")
                    return
                result=MathLibrary.power(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='√':
                b=self.returnFloat(b)
                if b == "WRONG_VALUE":
                    self.showErrorDialog("Input is empty, or in bad format")
                    return
                result=MathLibrary.root(a,b)
                resultLine = "{0}{1}{2}={3}".format(b,sign,a,result)
            elif sign=='!':
                result=MathLibrary.fact(a)
                resultLine = "{0}{1}={2}".format(a,sign,result)
            elif sign=="ln":
                result=MathLibrary.ln(a)
                resultLine = "{0}({1})={2}".format(sign,a,result)
            elif sign=='+':
                b=self.returnFloat(b)
                if b == "WRONG_VALUE":
                    self.showErrorDialog("Input is empty, or in bad format")
                    return
                result=MathLibrary.add(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='-':
                b=self.returnFloat(b)
                if b == "WRONG_VALUE":
                    self.showErrorDialog("Input is empty, or in bad format")
                    return
                result=MathLibrary.subtract(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='*':
                b=self.returnFloat(b)
                if b == "WRONG_VALUE":
                    self.showErrorDialog("Input is empty, or in bad format")
                    return
                result=MathLibrary.multiply(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            elif sign=='/':
                b=self.returnFloat(b)
                if b == "WRONG_VALUE":
                    self.showErrorDialog("Input is empty, or in bad format")
                    return
                result=MathLibrary.divide(a, b)
                resultLine = "{0}{1}{2}={3}".format(a,sign,b,result)
            self.lineEditResult.setText(str(resultLine))
            self.changeFocus1()
        except ValueError as e:
            self.showErrorDialog(str(e))
    
        
    def returnFloat(self,a):
        if a=="":
            return "WRONG_VALUE"
        try:
            a = float(a)
            return a
        except ValueError:
            return "WRONG_VALUE"
        
    def showErrorDialog(self,input):
        QtWidgets.QMessageBox.critical(self,"Error",input)
        
    def showInfoDialog(self,input):
        QtWidgets.QMessageBox.information(self,"Nápověda",input)        
        

if __name__ == '__main__':                        
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())     