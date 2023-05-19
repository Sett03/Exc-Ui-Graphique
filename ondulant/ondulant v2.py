from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def ondulant(n):
    ch=str(n)
    if len(ch)< 3:
        mess="veullier introduire le nombre >=100"
    else :
        test=True
        i=0
        valide =False
        while valide == False :
            if ch [i]!=ch[i+2]:
                test=False
            else :
                i=i+1
            print(i)
            if test == False or i==len(ch)-2 :
                valide=True
        if test == True:
            mess=ch+"est ondulant"
        else :
            mess=ch+"non ondulant"
    return mess
def play():
    x=windows.l1.text()
    s=ondt(x)
    windows.l2.setText(str(s))




app=QApplication([])
windows = loadUi("ondulant.ui")
windows.show()
windows.b1.clicked.connect(play)
app.exec_()
