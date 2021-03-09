import pandas as pd 
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count     

# Listas para Factores de produccion (L, K) y Cantidades producidas (Qi)
L = [0.2]
K = [0]
Q_1 = [0]
Q_2 = [0]
Q_3 = [0]

def cobb_douglas_rd(K, L):      # Creamos funciones de produccion Cobb-Douglas que nos devolverán un nivel de produccion especifico segun el valor de los coeficientes alpha beta
    z = 1
    alpha = 0.40
    beta = 0.4
    return z * K**alpha * L**beta
def cobb_douglas(K, L):
    z = 1
    alpha = 0.333
    return z * K**alpha * L**(1-alpha)
def cobb_douglas_rc(K, L):
    z = 1
    alpha = 0.6
    beta = 0.6
    return z * K**alpha * L**beta

plt.style.use('seaborn')
index = count(start=1, step=1) # con la funcion count iremos empleando valores que se incrementan de a 1 
def animacion(i):   # Definimos la funcion que incrementará las listas de factores, que luego serán procesadas por las funciones de produccion y por último se graficaran continuamente
    K.append(next(index))
    L.append(next(index))
    Q_1.append(cobb_douglas_rd(L[i],K[i]))
    Q_2.append(cobb_douglas(L[i],K[i]))
    Q_3.append(cobb_douglas_rc(L[i],K[i]))
    plt.cla()
    plt.plot(Q_3, label="Rendimientos Crecientes")
    plt.plot(Q_2, label='Rendimientos Constantes')
    plt.plot(Q_1, label='Rendimientos Decrecientes')
    print(L, K)
    plt.title("Funciones de Produccion Cobb-Douglas", fontsize=16)
    plt.xlabel("Adhesion Factores: step 2 unidades")
    plt.ylabel("Produccion Total (Q)")
    plt.legend()
    
ani = FuncAnimation(plt.gcf(), animacion, interval=700) # Con una clase animamos la figura del grafico con un intervalo que define la velocidad
plt.tight_layout() 
plt.show()

def returns_to_scale(K, L, gamma):
    y1 = cobb_douglas(K, L)
    y2 = cobb_douglas(gamma*K, gamma*L)
    y_ratio = y2 / y1
    return y_ratio / gamma
def marginal_products(K, L, epsilon):
    mpl = (cobb_douglas(K, L + epsilon) - cobb_douglas(K, L)) / epsilon
    mpk = (cobb_douglas(K + epsilon, L) - cobb_douglas(K, L)) / epsilon
    return mpl, mpk

# print(cobb_douglas(5,10),
#     "Su rendimiento de escala es: ",returns_to_scale(1.5,0.9,5),
#     "Sus productos marginales son: ", marginal_products(1.5,0.9,0.5))