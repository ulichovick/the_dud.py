import base64
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Cifrado import Cifrado

#pwwd = input("Ingrese la contraseña \n")

#test = Cifrado(pwwd)
#print(test.cifrar_contraseñas())
#print(test.cifrado_suave("hotmail","usuario","www.hotmail.com","contrasena"))
#print(test.descifrado_suave())

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.execute("select * from usuarios")
for query in cursor:
    print(query)
conexion.close()