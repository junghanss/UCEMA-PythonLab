archivo = open('archivo1.txt', 'w')     
archivo.write('1 . Prueba 27-5 Clase\n')
archivo.write('2 . Salto de linea\n3. Salto de linea')
archivo.write('4 . Lorem Ipsum')
archivo.close() # Recordemos siempre cerrar el archivo para no generar quilombo

# w: crear / abrir para escribir (sobreescribe)
# t: texto (parametro default)
# b: binario
# x: crear nuevo archivo (no debe existir)
# a: agregar al final del programa

archivo2 = open('archivo1.txt', )
contenido = archivo2.read()
print(contenido, '\n')
archivo2.close()

archivo2=open('archivo1.txt')
for linea in archivo2:
    print(linea, end='')
archivo2.close()

archivo2=open('archivo1.txt')
lineas = archivo2.readlines() # Devuelve una lista con las lineas
print('\n',lineas)
archivo2.close()

# Comma Separated Value
a = open('GOOG.csv')
suma_total=0

for linea in a:
    campos = linea.split(',')
    cuit = campos[0]
    punto_venta = int(campos[1])
    numero = int(campos[2])
    total = float(campos[3])

    suma_total = suma_total + total

    print(cuit,punto_venta,numero,total)

print(suma_total)
a.close()
