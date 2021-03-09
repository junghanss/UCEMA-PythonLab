import matplotlib.pyplot as plt
from random import choice

#Definimos la funcion para cada transformacion con p como una lista con 2 valores (x e y)
def trans_1(p):
    x=p[0]
    y=p[1]
    x1= 0.5*x
    y1= 0.5*y
    return x1,y1

def trans_2(p):
    x=p[0]
    y=p[1]
    x1= 0.5*x + 0.5
    y1= 0.5*y + 0.5
    return x1,y1

def trans_3(p):
    x=p[0]
    y=p[1]
    x1= 0.5*x + 1
    y1= 0.5*y
    return x1,y1
#Las funciones devolveran los valores de x1,y1 que son correspondientemente operados

transformations = [trans_1,trans_2,trans_3] #Una lista para que choice elija desde ella
a1=[0] #Listas para mantener un track de los puntos a y b (ahora 0,0)
b1=[0]
a,b=0,0

for i in range(10000): #Elegimos la cantidad de puntos de 10 a 1000000
    trans=choice(transformations) #Elige random la funcion de transformacion
    a,b = trans((a,b)) #los valores a b cambiaran
    a1.append(a)        # las listas seran graficadas
    b1.append(b)

plt.rc('figure',figsize=(16,16))
plt.plot(a1,b1,'o')
#plt.xlim("Eje horizontal")
#plt.ylim("Eje vertical")
#plt.title("Sierpinski Triangle")
plt.show()
plt.savefig('my_triangle_test.png')
