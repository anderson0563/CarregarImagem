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


def rotacao180(a):
    mat = [round(-1*a[0] + 0*a[1],1), round(0*a[0] - 1*a[1],1)]
    return mat
    
c=[-5, 1]
b=[-4,4]
a=[-2,2]
plt.style.use('seaborn-whitegrid')

plt.axes()
reta(c,b)
reta(b,a)
reta(c,a)
alinha=rotacao180(a)
blinha=rotacao180(b)
clinha=rotacao180(c)
reta(clinha,blinha)
reta(blinha,alinha)
reta(clinha,alinha)

plt.axhline(color='black')
plt.axvline(color='black')
plt.xlabel('x', color='black')
plt.ylabel('y', color='black')
plt.title('Rotação 180o')
plt.show()