from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def Play():
    N=int(windows.l1.text())
    q=kpp(N)
    if (q!=0):
        windows.RES.setText(str(N)+" est "+str(q)+"kpp")
    else:
        windows.RES.setText(str(N)+" est non kpp")
def kpp(n):
    c=0
    d=2
    valid =False
    while valid ==False:
        if n%d==0:
            c=c+1
            n=n//d
        else:
            d=d+1
        if n==1:
            valid=True
    return c


#def effacer():
    #windows.l1.clear()
    
    
    
app=QApplication([])
windows = loadUi("kpp.ui")
windows.show()
windows.verif.clicked.connect(Play)

#windows.effacer.clicked.connect(effacer) ##j'ai utilisez la methode graphique pour le module effacer(en Qt Designer)
app.exec_()