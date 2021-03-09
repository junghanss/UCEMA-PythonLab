def operar(v1,v2,fn):       # Funcion de orden superior, recibe como parametros los nros y una funcion, te devuelve la funcion operando
    return fn(v1,v2)

def sumar(x1,x2):
    return x1+x2
def restar(x1,x2):
    return x1-x2
def multiplicar(x1,x2):
    return x1*x2
def dividir(x1,x2):
    return x1/x2

resu1=operar(10,3,sumar)
print(resu1)
resu2=operar(10,3,restar)
print(resu2)
print(operar(30,10,multiplicar))
print(operar(10,2,dividir))

# Funcion MAP: aplica una función a cada uno de los elementos de una lista. Imagina que tienes una lista de enteros y quieres obtener una nueva lista con el cuadrado de cada uno de ellos.
enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print("El resultado con Map fue: ", cuadrados)

# Funcion FILTER: Imagina que quieres filtrar una lista de números para obtener solo los valores pares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x : x % 2 == 0, valores))
print("El resultado con Filter fue: ", pares)

# Funcion REDUCE: Para llevar a cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado.
from functools import reduce
suma = reduce(lambda x, y: x + y, valores)
print("El resultado con Reduce fue: ", suma) 