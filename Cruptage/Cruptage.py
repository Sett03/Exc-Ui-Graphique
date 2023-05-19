from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
def b1_click():
    T=array([str]*100)
    for j in range (26):
        T[j]= chr(65+j)
    T[26]=" "
    ch1=""
    ch=windows.l1.text()
    for i in range(0,len(ch),2):
        if ch[i] ==" ":
            x1=26
        else:
            x1=ord(ch[i])-65
        if ch[i+1] ==" ":
            x2=26
        else:
            x2=ord(ch[i+1])-65
        y1=((11*x1)+(3*x2))%27
        y2=((7*x1)+(4*x2))%27
        ch1=ch1+str(T[y1])+str(T[y2])
    windows.RES.setText(ch1)
        





app = QApplication([])
windows = loadUi ("Cruptage.ui")
windows.show()
windows.b1.clicked.connect ( b1_click )

app.exec_()