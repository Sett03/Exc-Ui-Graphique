from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def pgcd(a,b):
    while a!=b:
        d=abs(b-a)
        b=a
        a=d
    return a
def play():
    x=windows.l1.text()
    y=windows.l2.text()
    s=pgcd(int(x),int(y))
    windows.l3.setText(str(s))




app=QApplication([])
windows = loadUi("PGCD.ui")
windows.show()
windows.b1.clicked.connect(play)
app.exec_()