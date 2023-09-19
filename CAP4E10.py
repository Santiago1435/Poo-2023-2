import tkinter as tk
from tkinter import messagebox

class Estudiante:
    def __init__(self, numero, nombre):
        """
        Inicializa un objeto Estudiante con un número de inscripción y un nombre.
        """
        self.numeroIns = numero
        self.nombre = nombre

    def getNumero(self):
        return self.numeroIns

    def getNombre(self):
        return self.nombre

    def setPatrimonio(self, valor):
        self.patrimonio = valor

    def setEstrato(self, estrato):
        self.estrato = estrato

    def getMatricula(self):
        if self.patrimonio > 2000000 and self.estrato > 3:
            return 50000 + (self.patrimonio * 0.03)

def calcular_matricula():
    estudiante = Estudiante(numero=numero_inscripcion_entry.get(), nombre=nombre_entry.get())
    estudiante.setEstrato(estrato=int(estrato_entry.get()))
    estudiante.setPatrimonio(valor=float(patrimonio_entry.get()))

    valor = estudiante.getMatricula()

    string = f'Número Inscripción: {estudiante.getNumero()} \nNombres: {estudiante.getNombre()} \nMatrícula: {valor:.2f}'

    messagebox.showinfo("Resultado", string)

# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 10 Capitulo 4")
window.geometry("400x250")

# Crear un marco para centrar los elementos
frame = tk.Frame(window)
frame.pack(expand=True, fill="both")

numero_inscripcion_label = tk.Label(frame, text="Número Inscripción:", anchor="e")
numero_inscripcion_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

numero_inscripcion_entry = tk.Entry(frame)
numero_inscripcion_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

nombre_label = tk.Label(frame, text="Nombres:", anchor="e")
nombre_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

nombre_entry = tk.Entry(frame)
nombre_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

patrimonio_label = tk.Label(frame, text="Patrimonio:", anchor="e")
patrimonio_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

patrimonio_entry = tk.Entry(frame)
patrimonio_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

estrato_label = tk.Label(frame, text="Estrato:", anchor="e")
estrato_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

estrato_entry = tk.Entry(frame)
estrato_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Crear botón para calcular y centrarlo
calcular_button = tk.Button(frame, text="Calcular", command=calcular_matricula)
calcular_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Centrar el marco en la ventana
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

window.mainloop()
