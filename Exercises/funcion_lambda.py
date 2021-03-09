f1 = lambda x : 2*x+3
print(f1(2))

f2 = lambda x,y : x**y
print(f2(2,6))

def ejemplo1(n):
    return lambda x: x*n

print(ejemplo1(5))  # Hasta ahi solo tengo almacenada una lambda de 10 sin definir x todavia
f3 = ejemplo1(10)   # Almaceno mi variable lambda en f3
print(f3(3))        # Defino el parametro X y me devuelve la operacion

