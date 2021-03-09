# ORM: Object Relational Mapping: mapea objetos a bases de datos relacionales
# Base de datos relacional: Tablas (Access, SQL Server, MySQL, Oracle, Maria DB, etc...)
# SQL: lenguaje de programacion de base de datos
# ejemplo: insert into productos (descripcion, precio, peso, proveedor) values ('mouse', 350, 120, 'gralf')
# si cambiarias de SQL Server a MySQL tendrias un re quilombo manualmente, para eso se usa ORM

from sqlalchemy.ext.declarative import declarative_base # declarative base construye una clase base
from sqlalchemy import Column, String, Float, Integer # para especificar que algo es una columna 
from sqlalchemy import create_engine # motor de base de datos
from sqlalchemy.orm import sessionmaker # para crear/abrir/cerrar sesiones


Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos' #el nombre de la tabla donde se van a guardar estos objetos
    id = Column(Integer, primary_key=True) #primary_key es la columna que identifica de forma univoca el objeto
    descripcion = Column(String)
    precio = Column(Float)
    peso = Column(Float)
    proveedor = Column(Integer)

    def __str__(self):
        return self.descripcion # Para que no devuelva el espacio en memoria, sino el objeto

engine = create_engine('sqlite:///mibase.sqlite') # Connection String; usaremos sqlite como base de datos, es la mas parecida a Access que existe y es open source, mibase seria la direccion donde guardamos

Base.metadata.create_all(engine) # Crear el modelo en la base de datos, en este caso la tabla

Session = sessionmaker() # creamos un objeto para el manejo de sesiones
Session.configure(bind=engine) # vinculamos la sesion con el motor de base de datos

# Proceso p/ Grabar un producto
a = Producto()
a.id = '88'
a.descripcion = 'mouse'
a.precio = 350.45
a.peso = 120
a.proveedor = ''

s = Session()
s.add(a)
s.commit() # asienta los cambios en la base de datos, salva
print('Se grabó con id  ', a.id)

s = Session()
prds = s.query(Producto)  # query = consultar
for p in prds:
    print(p.id, p.descripcion, p.precio)

prds = s.query(Producto).filter(Producto.id==2)
