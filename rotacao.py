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


def rotacao30(a):
    matrizRotacao = np.array(
        [
            [math.sqrt(3)/2, -1/2],
            [1/2, math.sqrt(3)/2] 
        ]    
    )

    mat = [round(math.sqrt(3)/2*a[0] - 1/2*a[1],1), round(1/2*a[0] + math.sqrt(3)/2*a[1],1)]
    return mat
    
c=[-5, 1]
b=[-4,4]
a=[-2,2]
plt.style.use('seaborn-whitegrid')

plt.axes()
reta(c,b)
reta(b,a)
reta(c,a)
alinha=rotacao30(a)
blinha=rotacao30(b)
clinha=rotacao30(c)
reta(clinha,blinha)
reta(blinha,alinha)
reta(clinha,alinha)

plt.axhline(color='black')
plt.axvline(color='black')
plt.xlabel('x', color='black')
plt.ylabel('y', color='black')
plt.title('Rotação 30o')
plt.show()