import base64
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Cifrado import Cifrado
from usuarios import Usuario

nombre_usuario = input("Ingrese nom usu \n")

#test = Cifrado(pwwd)
#print(test.cifrar_contraseñas())
#print(test.cifrado_suave("hotmail","usuario","www.hotmail.com","contrasena"))
#print(test.descifrado_suave())

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.execute("select nombre_usuario,contraseña,sal from usuarios where nombre_usuario =?",(nombre_usuario,))
query = cursor.fetchone()
print(type(query[2]))
sal = query[2]
print(sal)
conexion.close()


conexion = sqlite3.connect("usuarios.db")
cursor = Usuario(nombre_usuario,"test")
query = cursor.verificar_usuario()
print(query)
conexion.close()
