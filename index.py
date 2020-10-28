import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from usuarios import Usuario
usu = input("Ingrese el nombre de usuario: \n")
pwwd = input("Ingrese la contraseña: \n")
pwwd_conf = input("Ingrese la contraseña de nuevo: \n")
while pwwd != pwwd_conf:
    print("las contraseñas no coinciden")
    pwwd = input("Ingrese la contraseña: \n")
    pwwd_conf = input("Ingrese la contraseña de nuevo: \n")

test = Usuario(usu,pwwd)
test.crear_usuario()
print("todo ok: ")

