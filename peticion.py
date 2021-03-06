import requests, json

resp = requests.get('http://127.0.0.1:8080/')
if resp.status_code == 200: 
    print(resp.content) # .content: contenido respuesta (bytes), si es .text lo interpreta como texto, 

if resp.status_code == 200:
    o = resp.json()
    o2 = json.loads(resp.text)
    print(o.campo1) # Obtenemos una representacion en python del objeto JSON que viajó
    print(o2)