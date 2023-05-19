from PyQt5.QtWidgets import *
from PyQt5.uic import *

print(ord(" "))
def jeux(ch):
    if (ch.isdigit() and len(ch)==8 and ch[0]=="9" and ch[1] in ["9" ,"7", "5"]):
        x=int(ch)
        if x%2==0:
            msg="vous avez gagnez"
        else:
            msg="dsl vous avez perdu"
    else:
        msg = "verifier votre numero"
    return msg
    
def play():
    ch=f.l.text()
    r=jeux(ch)
    f.msg.setText(r)
def clear():
    f.l.clear()
def close():
    f.close()

app=QApplication([])
f=loadUi("tt.ui")
f.show()
f.b.clicked.connect(play)
f.bc.clicked.connect(clear)
f.bd.clicked.connect(close)


app.exec_()