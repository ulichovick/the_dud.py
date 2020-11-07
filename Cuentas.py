import sqlite3
from Cifrado import Cifrado


class cuenta:
    def __init__(
                self,
                id_usuario="",
                sitio="",
                url="",
                login="",
                password="",
                master_password=""):
        self.sitio = sitio
        self.id_usuario = id_usuario
        self.url = url
        self.login = login
        self.password = password
        self.master_password = master_password
        self.conexion = sqlite3.connect("usuarios.db")

    def crear_cuenta(self):
        """
        acá se realiza el registro de las cuentas a la base de datos local
        casos de error pendientes a verificar
        """
        self.key, self.sal = Cifrado(self.master_password).cifrar_contraseñas()
        # cambiar los return para que salgan en una lista
        self.sitio, self.login, self.url, self.password = Cifrado(self.master_password).cifrado_suave(
                                                                                                self.sitio,
                                                                                                self.login,
                                                                                                self.url,
                                                                                                self.password,
                                                                                                self.key)
        try:
            self.query = self.conexion.execute(
                                            """insert into cuentas(ID_usuario,Nombre_cuenta,Login,URL,contraseña,sal)
                                            values (?,?,?,?,?,?)""",
                                            (self.id_usuario,
                                            self.sitio,
                                            self.login,
                                            self.url,
                                            self.password,
                                            self.sal))
            self.conexion.commit()
            return "mensaje de exito"
        except Exception as err:
            self.resultado = err
            return self.resultado
        finally:
            self.conexion.close()

    def verificar_cuentas(self):
        """
        verifica las cuentas registradas bajo el id del usuario
        """
        try:
            self.query = self.conexion.execute(
                                            """select Nombre_cuenta,Login,URL,contraseña,sal from cuentas where ID_usuario = ?""",
                                            (self.id_usuario))
            self.query = self.query.fetchall()
            return (self.query)

        except Exception as err:
            self.resultado = err
            return self.resultado
        finally:
            self.conexion.close()
