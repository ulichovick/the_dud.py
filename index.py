import sqlite3
from cryptography.fernet import Fernet

archi1=open("datos.txt","w") 
archi1.write("Primer línea.\n") 
archi1.write("Segunda línea.\n") 
archi1.write("Tercer línea.\n")  
archi1.close() 

key = Fernet.generate_key()
f = Fernet(key)

with open('datos.txt', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('datos.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

with open('datos.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('datos.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

print("Desea encriptar el archivo?")


