# JSON: JavaScript Object Notation
import json 

s = '{ "nombre":"Juan", "apellido":"Junghanss" }'

o = json.loads(s)   # Si tenemos un string, nos lo convierte en dict
# print(o) # type=dict
print(o['nombre'])

d = {
    'nombre':'Juan',
    'apellido':'Junghanss'
}
dx = json.dumps(d)
print('En JSON es: ' + dx)

class Persona():
    nombre=''
    edad=0
    altura=0
p =Persona()
p.nombre='Juan'
p.edad=21
p.altura=175

px = json.dumps(p.__dict__) # Convertimos en un dict el objeto, junto con sus atributos. Sino, json.dumps crashea
print("En JSON es:  ", px)
