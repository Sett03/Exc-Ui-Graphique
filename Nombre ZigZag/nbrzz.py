from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def zigzag(n):
    m2=str(n)
    test=True
    i=1
    j=0
    valide=False
    while valide==False and j< len (m2)-1:
        if  int(m2[j])<int(m2[j+1]) or int(m2[j])>int(m2[j+1]):
            j=j+1
        else:
            valide=True
    if j==len(m2)-1:
        return True
    else:
        return False
    
def play():
    m=windows.l1.text()
    n=int(m)
    if not n>=100:
        windows.l2.setText("veillez verifier vos données n>=100")
    elif zigzag(n)==True:
        windows.l2.setText("ce nbr est ZIG ZAG")
    else:
        windows.l2.setText("veillez verifier vos donnée")

def effacer():
    windows.clear()


app = QApplication([])
windows = loadUi ("interzz.ui")
windows.show()
windows.b1.clicked.connect ( play )
#☻windows.b2.clicked.connect ( effacer )

app.exec_()