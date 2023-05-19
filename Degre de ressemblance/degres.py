from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def verif(ch):
    i=0
    valid = True
    while valid == True and i<len(ch):
        if not 65<=ord(ch[i])<=97:
            valid ==False
        else :
            i=i+1
    return valid
        

def ds(X,Y):
    i=0
    k=0
    
    while ((i<len(X)and i<len(Y))):
        
        if X[i]==Y[i]:
            k=k+1
        i=i+1
    c= (k/(i))*100
    return c
        
    
    
    
def close_click():
    windows.close()
def calc_click():
    X=windows.l1.text()
    Y=windows.l2.text()
    if not verif(X)==True:
        windows.RES.setText("le 1er nombre est vide")
    elif verif(Y)==False:
        windows.RES.setText("le 2eme nombre est vide")
    else:
        R=ds(X,Y)
        windows.RES.setText("le degre de ressemblance est "+str(R))


app = QApplication([])
windows = loadUi ("C:/Users/pc/Desktop/Graf/Degre de ressemblance/interdr.ui")
windows.show()
windows.EXIT.clicked.connect ( close_click )
windows.calc.clicked.connect ( calc_click )

app.exec_()