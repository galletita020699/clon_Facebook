import sqlite3
from sqlite3 import Error

#Conexion de la base de datos
try:
   connection = sqlite3.connect("proyecto.db")
   print("Conexión exitosa")
except:
   print(Error)
finally:
   connection.close()