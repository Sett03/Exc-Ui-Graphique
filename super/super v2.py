from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
def cnd(a):
    test1=False
    c=0
    ch=str(a)
    for i in range (len(ch)):
        if int (ch[i])%2==0:
            c=c+1
    test1=c=len(ch)
    i=1
    test2= True
    valid= False
    while valid == False:
        i=i+1
        if(a%i==0):
            if not (i%2==0):
                test2= False
        if test2 == False or i==a:
            valid = True
    test3=(test1 and test2)
    return test3



def super(a):
    c=""
    if a==0:
        c="saisir un numero >0"
    else:
        if cnd(a) == True:
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


