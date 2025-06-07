import math

def F(x):
    return x**3 + 6 * x**2 - 19*x -84
def Df(x):
    return 3 * x**2 + 12*x - 19
def Flounder(x):
    if ((x*1000) % 10 >=5):
        return (((x*100)-((x*100)%1))/100 + 0.01)
    else :
        return (((x*100)-((x*100)%1))/100)
x = -4 #Ini nilai X0
xt = -3 #Ini nilai x sebenarnya
i = 1
while x != xt:
    x = x - F(x) / Df(x)
    print("Iterasi ke -",i,":","\nTanpa pembulatan: ",x,"\nDengan pembulatan: ",Flounder(x),"\n")
    i += 1