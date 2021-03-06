# texto = " metodologia REST en servidores: GET / POST (Alta) / PUT (Modificar) / DELETE (Eliminar) "

# apuntes_servidor_web = open("apuntes_servidor_web.txt", "a")
# apuntes_servidor_web.close()

from flask import Flask, request
# 127.0.0.1 --- localhost
# :5000 --- puerto de conexion IP

app = Flask(__name__)

@app.route('/') # Le indicamos a la app que la ruta '/' es atendida por este funcion siguiente. Al definir la ruta tambien se define el metodo http (GET)
def raiz_sitio():
    return 'Hola'

@app.route('/')
def json_sitio():
    return {
        'campo1':'valor1',
        'campo2':'valor2'
    }
    
@app.route('/', methods=['POST', 'PUT']) 
def peticion_post():
    return 'desde un post'

@app.route('/search')
def busqueda_google():
    print(request.args)
    print(request.remote_addr)
    return 'buscando...'

@app.route('/productos/<codigo>/<familia>')
def leer_producto(codigo, familia):
    print('Piden el producto  ', codigo, familia)
    return 'producto' + codigo

@app.route('/productos', methods=['POST'])
def alta_producto():
    print(request.form)

    if not "apellido" in request.form:
        return "falta apellido"

    for key in request.form:
        print(key, '=', request.form[key])

    return 'se ingresa'


if __name__ == '__main__':      # para evitar que ejecutemos un modulo equivocado si tenemos muchas cosas
    app.run(port=8080) # le indicamos en qué puerto queremos que se ejecute



