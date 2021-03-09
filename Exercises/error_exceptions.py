# Errores /= Excepciones

def dos():
    x, y = 1, 0
    z = x/y
    return z

def uno():
    return dos()

try:            # Ejecucion de prueba
    z=uno()
except:         # Si es así, entonces que haga lo siguiente:
    print("Hubo un error")

try:
    z= uno()
    # abrir()
except ArithmeticError:     # Jerarquía de errores (ejemplo: ZeroDivisionError es heredado de Arithmetic, pero se printeará el Aritmethic por ser primero)
    print('error aritmetico')
# except ZeroDivisionError:       
#     print("Hubo otro error, por cero no podemos dividir")
except FileExistsError:
    print('El archivo ya existe')
except:
    print("No sé qué pasó")

print("Final feliz")

class MiError(Exception):
    pass # No agregamos nada más de codigo a la linea
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    

def leer_entero_positivo():
    n = int(input("Ingrese un integro: "))
    if n<0:
        raise MiError("Ingresaste mal el dato, boludo.", 12345) # Levantar error
    return n

try:
    numero = leer_entero_positivo()
except MiError as e:
    print("Está mal ingresado.")
    print(e.param1)
    print(e.param2)



