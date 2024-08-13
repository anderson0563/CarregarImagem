import matplotlib.pyplot as plt
import numpy as np
import math 

def reta(a, b):
    plt.axis('equal')
    plt.plot([a[0],b[0]], [a[1],b[1]])
    rotulos(a,b)

def retaX(a,b):
    plt.axis('equal')
    plt.plot([-a[0],-b[0]], [a[1],b[1]])
    alinha=[-a[0], a[1]]
    blinha=[-b[0], b[1]]
    rotulos(alinha, blinha)

def rotulos(a, b):
    label = f"({a[0]}, {a[1]})"
    plt.annotate(label, a)
    label = f"({b[0]}, {b[1]})"
    plt.annotate(label, b)

def translacao(a, T):
    mat = [round(a[0]+T[0], 1), round(a[1]+T[1],1)]
    return mat
    
c=[5, 1]
b=[4,4]
a=[1,2]
plt.style.use('seaborn-whitegrid')

T=[2,2]
plt.axes()
reta(c,b)
reta(b,a)
reta(c,a)
at=translacao(a,T)
bt=translacao(b,T)
ct=translacao(c,T)
reta(ct,bt)
reta(bt,at)
reta(ct,at)

plt.axhline(color='black')
plt.axvline(color='black')
plt.xlabel('x', color='black')
plt.ylabel('y', color='black')
plt.title('Translação')
plt.show()