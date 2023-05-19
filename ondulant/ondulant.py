from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def ondt(a):
    c=a+"non ondulant"
    L=len(a)
    i=0
    if int(a)<100:
        c="introduire un numero >=100"
    else:
        valid = False
        while valid == False:
            if a[i]==a[i+2]:
                i=i+1
            if i== L-2:
                c=a+"ondulant"
            if c==a+"ondulant" or a[i]!=a[i+2]:
                valid=True
    return c
def play():
    x=windows.l1.text()
    s=ondt(x)
    windows.l2.setText(str(s))




app=QApplication([])
windows = loadUi("ondulant.ui")
windows.show()
windows.b1.clicked.connect(play)
app.exec_()
