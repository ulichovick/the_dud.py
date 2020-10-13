import base64
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

pwwd = input("Ingrese la contraseña \n")
pwwd = str.encode(pwwd)
salt = str.encode("test")

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = base64.urlsafe_b64encode(kdf.derive(pwwd))
f=Fernet(key)
eleccion = int(input("¿Que desea realizar? 1=encriptar 2=desencriptar \n"))
if eleccion == 1:
    archi1=open("datos.txt","w") 
    archi1.write("Primer línea.\n") 
    archi1.write("Segunda línea.\n") 
    archi1.write("Tercer línea.\n")  
    archi1.close() 
    with open('datos.txt', 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)
    with open ('datos.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print("archivo encriptado")
else:
    with open('datos.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open('datos.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    print("archivo desencriptado")