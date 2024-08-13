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

def escalaMeio(a):
    mat = [round(0.5*a[0], 1), round(0.5*a[1],1)]
    return mat

def escalaDobro(a):
    mat = [round(2*a[0], 1), round(2*a[1],1)]
    return mat

    
c=[-5, 1]
b=[-4,4]
a=[-2,2]
plt.style.use('seaborn-whitegrid')

plt.axes()
reta(c,b)
reta(b,a)
reta(c,a)
ameio=escalaMeio(a)
bmeio=escalaMeio(b)
cmeio=escalaMeio(c)
reta(cmeio,bmeio)
reta(bmeio,ameio)
reta(cmeio,ameio)
adobro=escalaDobro(a)
bdobro=escalaDobro(b)
cdobro=escalaDobro(c)
reta(cdobro,bdobro)
reta(bdobro,adobro)
reta(cdobro,adobro)

plt.axhline(color='black')
plt.axvline(color='black')
plt.xlabel('x', color='black')
plt.ylabel('y', color='black')
plt.title('Mudança de Escala')
plt.show()