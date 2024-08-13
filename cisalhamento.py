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

def cisalhamento(a, kx, ky):
    mat = [round(a[0]+kx*a[1], 1), round(ky*a[0] + a[1],1)]
    return mat
    
c=[5, 1]
b=[4,4]
a=[0,0]
plt.style.use('seaborn-whitegrid')

plt.axes()
reta(c,b)
reta(b,a)
reta(c,a)
acisa=cisalhamento(a,1,0)
bcisa=cisalhamento(b,1,0)
ccisa=cisalhamento(c,1,0)
reta(ccisa,bcisa)
reta(bcisa,acisa)
reta(ccisa,acisa)

plt.axhline(color='black')
plt.axvline(color='black')
plt.xlabel('x', color='black')
plt.ylabel('y', color='black')
plt.title('Cisalhamento')
plt.show()