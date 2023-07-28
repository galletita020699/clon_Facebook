import sqlite3
from sqlite3 import Error

#Conexion de la base de datos
try:
   connection = sqlite3.connect("proyecto.db")
   print("Conexión exitosa")
except:
   print(Error)
   connection.close()

   def insertar(connection):
    #agregamos el cursor
    cursor = connection.cursor()
    cursor.execute('INSERT INTO segundo_parcial(nombre,apellido_paterno, apellido_materno,correo,fecha_nacimiento, contraseña) VALUES ("Monserrat","Cayetano","Hernández","monsecaye@hotmail.com","02 junio 1999", "monse23")')
    #Guarda los cambios en la base de datos
    connection.commit() 
   insertar(connection)
   