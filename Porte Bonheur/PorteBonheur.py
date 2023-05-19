from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Play():
    N=windows.l.text()
    V=verifier(N)
    if V== True:
        windows.RES.setText(str(N)+"est porte bonheur")
    else:
        windows.RES.setText(str(N)+"n'est pas porte bonheur")

def verifier (X):
    ch= str(X)
    c=abs( int(ch[0])-int(ch[1]))
    verif = True
    i=0
    while (verif == True and (i <len(ch)-1)):
        if int(ch[i])<int(ch[i+1]):
            p = True
        else :
            p = False
        if not((abs(int(ch[i])- int (ch[i+1]))==c)and ((int(ch[i])<int(ch[i+1])) == p)):
            verif= False
        else:
            i=i+1
    return verif
def close():
    exit(app.exec_())

app=QApplication([])
windows = loadUi("interbb.ui")
windows.show()
windows.verif.clicked.connect(Play)

windows.close.clicked.connect(close)
app.exec_()