import sympy as sym
from sympy.functions.elementary.complexes import principal_branch
import matplotlib.pyplot as plt

# Aralık değerlerimiz
xa=0.5
xb=4

x = sym.Symbol("x")
fx = (x-1)**2*(x-2)*(x-3) # Function

def turev(fx):
    df = sym.diff(fx)
    return df

def df(x):
    df=(x - 3)*(x - 2)*(2*x - 2) + (x - 3)*(x - 1)**2 + (x - 2)*(x - 1)**2
    return df

def Yarılama():
    global xa,xb
    xk = xa + (xb - xa) / 2
    if df(xk)*df(xa)>0:
        xa = xk
    else: 
        xb = xk
    return xk,xa,xb

dfa=df(xa)    
dfb=df(xb)

noktalar = []

if dfa*dfb>0 :
    print("Bu noktalar arasında yerel minimum/maksimum noktası yoktur !")
else:
    while True:
        xk,xa,xb = Yarılama()
        noktalar.append(xk)
        if df(xk)==0 or (xb-xa)<10**(-10):
            break
print(noktalar)
a = len(noktalar)
plt.plot(xk,range(0,a))
plt.show()
print("The best value of x : ",xk)