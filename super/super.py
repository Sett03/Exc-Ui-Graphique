from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import array
def cnd1(a):
    c=0
    i=0
    ch=str(a)
    L=len(ch)
    valid =False
    while valid ==False:
        
        if int(ch[i])%2 == 0:
            c=c+1
        i=i+1
        if i == L-1:
            valid = True
    if c==L-1:
        return True
    else :
        return False
def div(a):
    d=0
    for i in range (2,a):
        if a%i==0:
            d=d+1
    return d
def cnd2(a):
    d=div(a)
    t=array([int]*d)
    j=0
    for i in range(2,a):
        if a%i==0:
            t[j]=i
            j=j+1
    x=0
    for i in range(d):
        if t[i]%2==0:
            x=x+1
    if x==d:
        return True
    else:
        return False



def super(a):
    c=""
    if a==0:
        c="saisir un numero >0"
    else:
        if cnd1(a)and cnd2(a) == True:
            c="super-pair-plus"
        else:
            c="non super pair plus"
    
    
    
    return c
def play():
    x=windows.l1.text()
    s=super(int(x))
    windows.l2.setText(s)




app=QApplication([])
windows = loadUi("super.ui")
windows.show()
windows.b1.clicked.connect(play)
app.exec_()

