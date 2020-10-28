import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from usuarios import Usuario

class Aplicacion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Password manager")
        self.ventana1.geometry("300x300")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        #login de usuario
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="Iniciar Sesión")
        self.label1=ttk.Label(self.pagina1,text="Usuario:")
        self.label1.grid(column=0,row=0)
        self.usuario_login=tk.StringVar()
        self.entrada_usuario=ttk.Entry(self.pagina1,width=25,textvariable=self.usuario_login)
        self.entrada_usuario.grid(column=1,row=0)
        self.label2=ttk.Label(self.pagina1,text="Contraseña:")
        self.label2.grid(column=0,row=1)
        self.passwd_login=tk.StringVar()
        self.entrada_passwd=ttk.Entry(self.pagina1,width=25,textvariable=self.passwd_login)
        self.entrada_passwd.grid(column=1,row=1)
        self.boton1=ttk.Button(self.pagina1, text="Cancelar", command=self.ventana1.destroy)
        self.boton1.grid(column=0,row=2)
        self.boton2=ttk.Button(self.pagina1, text="Aceptar",command=self.verifica_usuario)
        self.boton2.grid(column=1,row=2)

        #registra usuario
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="Añadir Usuario")
        self.label1=ttk.Label(self.pagina2,text="Usuario:")
        self.label1.grid(column=0,row=0)
        self.usuario=tk.StringVar()
        self.entrada_usuario=ttk.Entry(self.pagina2,width=25,textvariable=self.usuario)
        self.entrada_usuario.grid(column=1,row=0)
        self.label2=ttk.Label(self.pagina2,text="Contraseña:")
        self.label2.grid(column=0,row=1)
        self.passwd=tk.StringVar()
        self.entrada_passwd=ttk.Entry(self.pagina2,width=25,textvariable=self.passwd)
        self.entrada_passwd.grid(column=1,row=1)
        self.label3=ttk.Label(self.pagina2,text="Confirmar Contraseña:")
        self.label3.grid(column=0,row=2)
        self.confirma_passwd=tk.StringVar()
        self.entrada_confirma_passwd=ttk.Entry(self.pagina2,width=25,textvariable=self.confirma_passwd)
        self.entrada_confirma_passwd.grid(column=1,row=2)
        self.boton1=ttk.Button(self.pagina2, text="Cancelar", command=self.ventana1.destroy)
        self.boton1.grid(column=0,row=3)
        self.boton2=ttk.Button(self.pagina2, text="Aceptar", command=self.verifica_contra)
        self.boton2.grid(column=1,row=3)

        self.cuaderno1.grid(column=0, row=0)
        self.ventana1.mainloop()

    def verifica_contra(self):
        self.passwd = str(self.passwd.get())
        self.confirma_passwd = str(self.confirma_passwd.get())
        self.usuario = str(self.usuario.get())
        if self.passwd == self.confirma_passwd:
            self.resultado = Usuario(self.usuario,self.passwd)
            self.mensaje_exito = messagebox.showinfo(title="resultado", message=self.resultado.crear_usuario())
        else:
            self.mensaje_exito = messagebox.showwarning(title="resultado", message="¡las contraseñas no coinciden!")
    def verifica_usuario(self):
        self.passwd = str(self.passwd_login.get())
        self.usuario = str(self.usuario_login.get())
        self.resultado = Usuario(self.usuario,self.passwd)
        self.mensaje = messagebox.showinfo(title="resultado", message=self.resultado.verificar_usuario())
app1=Aplicacion()