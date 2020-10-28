import os
import sqlite3
from Cifrado import Cifrado
class Usuario:
    def __init__ (self,nombre_usuario,password):
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.conexion = sqlite3.connect("usuarios.db")
        self.key,self.salt = Cifrado(self.password).cifrar_contraseñas()
    def crear_usuario(self):
        """
        acá se realiza el registro del usuario a la base de datos local
        casos de error pendientes a verificar
        """
        try:
            self.query = self.conexion.execute("insert into usuarios(nombre_usuario,contraseña,sal) values (?,?,?)",(self.nombre_usuario,self.key,self.salt))
            self.conexion.commit()
            self.resultado = "¡usuario creado con éxito!"
            return self.resultado
        except Exception as err:
            self.resultado = err
            return self.resultado
        finally:
            self.conexion.close()
    def funcname(self, parameter_list):
        """
        verifica si el usuario está registrado en la base de datos
        en caso que encuentre el usuario abrirá la sesión
        en caso contrario lanzara error y permanecera en la pantalla de inicio de sesión.
        """
        pass