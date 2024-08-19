# Importar Bibliotecas
from tkinter import *
from tkinter import ttk,messagebox
from Modelo.Modelo_VG_Mensaje import *
from Controlador.Controlador_VG_Gestor import *
import tkinter as tk

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("APLICACION ESCRITORIO MVC ARQ SW")
        self.root.configure(background='lightblue')
        self.root.geometry("600x350")

        self.miId = tk.StringVar()
        self.miNombre = tk.StringVar()
        self.miCargo = tk.StringVar()
        self.miSalario = tk.StringVar()

        # Cargar imágenes
        self.imagen_buscar = tk.PhotoImage(file="Vista/imagenes/buscar.png")
        self.imagen_crear = tk.PhotoImage(file="Vista/imagenes/crear.png")
        self.imagen_mostrar = tk.PhotoImage(file="Vista/imagenes/mostrar.png")
        self.imagen_actualizar = tk.PhotoImage(file="Vista/imagenes/actualizar.png")
        self.imagen_eliminar = tk.PhotoImage(file="Vista/imagenes/eliminar.png")

        # Configurar la tabla
        self.cabecera = ["ID", "Nombre del Empleado", "Cargo", "Salario"]
        self.tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2'))
        self.tree.place(x=0, y=130)
        self.tree.column('#0', width=100)
        self.tree.heading('#0', text=self.cabecera[0], anchor=tk.CENTER)
        self.tree.heading('#1', text=self.cabecera[1], anchor=tk.CENTER)
        self.tree.heading('#2', text=self.cabecera[2], anchor=tk.CENTER)
        self.tree.column('#3', width=100)
        self.tree.heading('#3', text=self.cabecera[3], anchor=tk.CENTER)
        self.tree.bind("<Button-1>", self.seleccionarUsandoClick)

        self.mostrar()

        # Menú
        self.menubar = tk.Menu(self.root)
        self.menubasedat = tk.Menu(self.menubar, tearoff=0)
        self.menubasedat.add_command(label="Crear/Conectar Base de Datos", command=self.conexionBBDD)
        self.menubasedat.add_command(label="Eliminar Base de Datos", command=self.eliminarBBDD)
        self.menubasedat.add_command(label="Salir", command=self.salirAplicacion)
        self.menubar.add_cascade(label="Inicio", menu=self.menubasedat)

        self.ayudamenu = tk.Menu(self.menubar, tearoff=0)
        self.ayudamenu.add_command(label="Resetear Campos", command=self.limpiarCampos)
        self.ayudamenu.add_command(label="Acerca", command=Gestor.mensaje)
        self.menubar.add_cascade(label="Ayuda", menu=self.ayudamenu)

        self.root.config(menu=self.menubar)

        # Etiquetas y cajas de texto
        tk.Label(self.root, text="Nombre", background='lightblue').place(x=50, y=10)
        tk.Entry(self.root, textvariable=self.miNombre, width=50).place(x=100, y=10)

        tk.Label(self.root, text="Cargo", background='lightblue').place(x=50, y=40)
        tk.Entry(self.root, textvariable=self.miCargo).place(x=100, y=40)

        tk.Label(self.root, text="Salario", background='lightblue').place(x=280, y=40)
        tk.Entry(self.root, textvariable=self.miSalario, width=10).place(x=320, y=40)

        tk.Label(self.root, text="USD", background='lightblue').place(x=380, y=40)

        # Botones
        tk.Button(self.root, text="Buscar Registro", image=self.imagen_buscar, bg="orange", command=self.buscar).place(x=450, y=10)
        tk.Button(self.root, text="Crear Registro", image=self.imagen_crear, bg="green", command=self.crear).place(x=50, y=85)
        tk.Button(self.root, text="Actualizar Registro", image=self.imagen_actualizar, bg="orange", command=self.actualizar).place(x=180, y=85)
        tk.Button(self.root, text="Mostrar Lista", image=self.imagen_mostrar, bg="orange", command=self.mostrar).place(x=320, y=85)
        tk.Button(self.root, text="Eliminar Registro", image=self.imagen_eliminar, bg="red", command=self.borrar).place(x=450, y=85)

    def conexionBBDD(self):
        Gestor.conexionBBDD()

    def eliminarBBDD(self):
        Gestor.eliminarBBDD()
        self.limpiarMostrar()

    def limpiarCampos(self):
        self.miId.set("")
        self.miNombre.set("")
        self.miCargo.set("")
        self.miSalario.set("")

    def limpiarMostrar(self):
        self.limpiarCampos()
        self.mostrar()

    def mostrar(self):
        Gestor.mostrar(self.tree)

    def salirAplicacion(self):
        valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
        if valor == "yes":
            self.root.destroy()

    def crear(self):
        Gestor.crear(self.miNombre.get(), self.miCargo.get(), self.miSalario.get())
        self.limpiarMostrar()

    def actualizar(self):
        Gestor.actualizar(self.miNombre.get(), self.miCargo.get(), self.miSalario.get(), self.miId.get())
        self.limpiarMostrar()

    def borrar(self):
        Gestor.borrar(self.miId.get())
        self.limpiarMostrar()

    def buscar(self):
        Gestor.buscar(self.tree, self.miNombre.get())

    def seleccionarUsandoClick(self, event):
        item = self.tree.identify('item', event.x, event.y)
        self.miId.set(self.tree.item(item, "text"))
        self.miNombre.set(self.tree.item(item, "values")[0])
        self.miCargo.set(self.tree.item(item, "values")[1])
        self.miSalario.set(self.tree.item(item, "values")[2])

        
