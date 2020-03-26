import os,sys
from PyQt5 import QtWidgets,uic,QtGui,QtCore

def print():
    v=str(call.lineEdit.text())
    v2=str(call.lineEdit_2.text())


    cmd = ("head -n " + v2 + " " + v)
    result_code = os.system(cmd + ' > output.txt') 			   #cmd hold the shell command
    if os.path.exists('output.txt'):
        fp = open('output.txt', "r")
        output = fp.read()
        fp.close()
        os.remove('output.txt')

    call.textEdit.setText(output)

app = QtWidgets.QApplication(sys.argv)
call = uic.loadUi("micro.ui")

call.pushButton_2.clicked.connect(QtCore.QCoreApplication.instance().quit) #for exit button
call.pushButton.clicked.connect(print)					   #for submiting the shell command and display the output


call.show()
app.exec()


#FOSS MICRO PROJECT 2020 - S4 CSE A FISAT
#GROUP MEMEBERS :
#JEEVAMOL ROLL_NO: 61
#JENAT JOSE ROLL_NO: 62
#JIBIN GEORGE ROLL_NO: 63
