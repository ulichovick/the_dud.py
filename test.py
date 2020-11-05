import base64
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Cifrado import Cifrado
from usuarios import Usuario
from cuentas import cuenta

id_usuario = input("Ingrese id usu \n")

test = input("contraseña maestra \n")

#print(test.cifrar_contraseñas())
#print(test.cifrado_suave("hotmail","usuario","www.hotmail.com","contrasena"))
#print(test.descifrado_suave())
#se renombra el proyecto de pwwd_mngr o algo asi a fuck.exe
testt = []
test_var = cuenta(master_password=test,id_usuario=id_usuario).verificar_cuentas()
print(test_var)
for row in test_var:
    sal = row[4]
    cifrado = Cifrado(test)
    cifrado_pass = cifrado.verificar_cifrado(sal)
    testt.append(cifrado.descifrado_suave(row[0],row[1],row[2],row[3],cifrado_pass))
    print(cifrado.descifrado_suave(row[0],row[1],row[2],row[3],cifrado_pass))
print(testt)
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.execute("select nombre_cuenta,Login,URL,contraseña,sal from cuentas where ID_usuario =?",(id_usuario))
query = cursor.fetchone()
print(type(query))
print(query)
cifrado = Cifrado(test)
cifrado_pass = cifrado.verificar_cifrado(query[4])
print(cifrado.descifrado_suave(query[0],query[1],query[2],query[3],cifrado_pass))
conexion.close()
