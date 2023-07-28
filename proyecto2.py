from tkinter import *	
import os
from sqlite3 import Error

db_name="proyecto.db"
def ventana_inicio():
    global principal
    color="sky blue"
    principal=Tk()
    principal.geometry("500x450")
    principal.config(bg="purple")
    principal.title("Proyecto_Segundo_Parcial")
    imagenL=PhotoImage(file="facebook2.png")
    lblImagen=Label(principal,image=imagenL).place(x=100, y=100)
    Label(text="BIENVENIDO A META VERSO ", bg="Green", width="300", height="2", font=("Cooper Black", 18)).pack()
    Label(text="Escoja su opción",bg="purple", width="150", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()
    Button(text="Iniciar Sesion", height="2", width="30", bg=color, command=login).pack() 
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=color, command=registro).pack()
    Label(text="").pack()
    principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global venregistro
    venregistro = Toplevel(principal)
    venregistro.geometry("300x400")
    venregistro.config(bg="blue")
    venregistro.title("Registro")
    
    global nombre_usuario   #variables globales
    global entrada_nombre
    global apellidopaterno
    global entrada_apellidopaterno
    global apellidomaterno
    global entrada_apellidomaterno
    global correo
    global entrada_correo
    global fechanacimiento
    global entrada_fechanacimiento
    global clave
    global entrada_clave
    nombre_usuario = StringVar() 
    apellidopaterno = StringVar() 
    apellidomaterno = StringVar() 
    correo = StringVar() 
    fechanacimiento = StringVar() 
    clave = StringVar()
 
    Label(venregistro, text="Introduce tus datos", bg="yellow").pack()
    Label(venregistro, text="").pack()
    
    etiqueta_nombre = Label(venregistro, text="Nombre: ", bg="gray").pack()
    entrada_nombre = Entry(venregistro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    
    etiqueta_apellidopaterno = Label(venregistro, text="Apellido Paterno", bg="gray").pack()
    entrada_apellidopaterno = Entry(venregistro, textvariable=apellidopaterno)
    entrada_apellidopaterno.pack()
    
    etiqueta_apellidomaterno = Label(venregistro, text="Apellido Materno:", bg="gray").pack()
    entrada_apellidomaterno = Entry(venregistro, textvariable=apellidomaterno) 
    entrada_apellidomaterno.pack()
    
    etiqueta_correo = Label(venregistro, text="Correo Electronico:", bg="gray").pack()
    entrada_correo = Entry(venregistro, textvariable=correo) 
    entrada_correo.pack()
    
    etiqueta_fechanacimiento = Label(venregistro, text="Fecha de Nacimiento:", bg="gray").pack()
    entrada_fechanacimiento = Entry(venregistro, textvariable=fechanacimiento) 
    entrada_fechanacimiento.pack()
    
    etiqueta_clave = Label(venregistro, text="Contraseña * ", bg="gray").pack()
    entrada_clave = Entry(venregistro, textvariable=clave, show='*') 
    entrada_clave.pack()
    
    Label(venregistro, text="").pack()
    Button(venregistro, text="Registrarse", width=10, height=1, bg="purple", command = registro_usuario).pack() #BOTÓN "Registrarse"

#ventana login

def login():
    global venlogin   #variable global
    global verusuario
    global verifica_clave
    global entrada_usuario
    global entrada_clave

    verusuario = StringVar()
    verifica_clave = StringVar()
 
 
    venlogin = Toplevel(principal)
    venlogin.title("login")
    venlogin.config(bg="black")
    venlogin.geometry("300x300")
    Label(venlogin, text="Introduce tus Datos:", bg="blue").pack()
    Label(venlogin, text="").pack()
 
 
    Label(venlogin, text="Nombre:", bg="red").pack()
    entrada_usuario = Entry(venlogin, textvariable=verusuario)
    entrada_usuario.pack()
    Label(venlogin, text="").pack()
    Label(venlogin, text="Contraseña: * ", bg="red").pack()
    entrada_clave = Entry(venlogin, textvariable=verifica_clave, show= '*')
    entrada_clave.pack()
    Label(venlogin, text="").pack()
    Button(venlogin, text="Inicio Sesion", bg="gray", width=10, height=1, command = verifica_login).pack()

#VENTANA login

def verifica_login():
    usuario_1 = verusuario.get()
    clave1 = verifica_clave.get()
    entrada_usuario.delete(0, END) 
    entrada_clave.delete(0, END) 
    lista_archivos = os.listdir() #lista de archivos.
    if usuario_1 in lista_archivos:
        archivo = open(usuario_1, "r") #Archivo modo lectura
        verifica = archivo.read().splitlines() 
       
        if clave1 in verifica:
            exito_login() 
       
        else:
            no_clave() 
    
    else:
        no_usuario() 


# Ventana
 
def exito_login():
    global vexito
    vexito = Toplevel(venlogin)
    vexito.title("Exito")
    vexito.geometry("100x100")
    Label(vexito, text="Finalizado con exito").pack()
    Button(vexito, text="OK", command=borrar_login).pack()
 
#Ventana.
 
def no_clave():
    global claveven
    claveven = Toplevel(venlogin)
    claveven.title("ERROR")
    claveven.geometry("100x100")
    Label(claveven, text="Contraseña incorrecta ").pack()
    Button(claveven, text="OK", command=borrar_no_clave).pack() 
 
#Ventana
 
def no_usuario():
    global usuarioven
    usuarioven = Toplevel(venlogin)  #ventana que hereda con venlogin
    usuarioven.title("ERROR")
    usuarioven.geometry("100x100")
    Label(usuarioven, text="Usuario no encontrado").pack()
    Button(usuarioven, text="OK", command=borrar_no_usuario).pack() 

#Cerrar ventanas

def borrar_login():
    vexito.destroy() #cerramos la ventana
 
 
def borrar_no_clave():
    claveven.destroy()#cerramos la ventana
 
 
def borrar_no_usuario():
    usuarioven.destroy()#cerramos la ventana

#REGISTRO USUARIO
 
def registro_usuario():
 
    monse = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(monse, "w") #archivo modo lectura
    file.write(monse + "\n")
    file.write(clave_info)
    file.close()
    
    query = 'INSERT INTO segundo_parcial(nombre, apellido_paterno,apellido_materno,correo, fecha_nacimiento,contraseña) VALUES(null,null,null,null,null,null)'
    entrada_nombre. verusuario = StringVar()
    entrada_apellidopaterno. verusuario = StringVar()
    entrada_apellidomaterno. verusuario = StringVar()
    entrada_correo. verusuario = StringVar()
    entrada_fechanacimiento. verusuario = StringVar()
    verifica_clave = StringVar()

    entrada_clave.delete(0, END)
    entrada_nombre.delete(0, END)
    entrada_apellidopaterno.delete(0, END)
    entrada_apellidomaterno.delete(0, END)
    entrada_correo.delete(0, END)
    entrada_fechanacimiento.delete(0, END)
 
 
    Label(venregistro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
def run_query(self, query, parameter = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
            conn.close()
        return result
    
def get_proyecto(self):
    query = 'SELECT * FROM segundo_parcial ORDER BY name DESC'
        #db_rows = self.run_query(query)
        #print(db_rows)

        #for row in db_rows:
            #print (row)
            #self.tree.insert('',0,text=row[1], values=row[2])
 
ventana_inicio()  #EJECUCIÓN 