def parfait(N):
    S=0
    for i in range ( 1, N-1,1):
        if N%i==0:
            S=S+i
    if S==N:
        return True
    else:
        return False
def Sparfait(X):
    if parfait(X)==False:
        return False
    else :
        ch=str(X)
        i=0
        valid = False
        while valid == False and i<len(ch) :
            if not parfait(int(ch[i]))==True:
                i=i+1
            else :
                valid= True
        return valid
X=int (input("saisir X: "))
print(Sparfait(X))
#496