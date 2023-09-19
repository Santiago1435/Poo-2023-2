import tkinter as tk
from tkinter import messagebox

class Trabajador:
    def __init__(self, nombre, horas, valor):
        """
        Inicializa un objeto Trabajador con nombre, horas trabajadas y valor de la hora.

        Args:
            nombre (str): El nombre del trabajador.
            horas (int): La cantidad de horas trabajadas al mes.
            valor (float): El valor de la hora trabajada.
        """
        self.nombre = nombre
        self.horas = horas
        self.valor = valor

    def getNombre(self):
        """
        Obtiene el nombre del trabajador.

        Returns:
            str: El nombre del trabajador.
        """
        return self.nombre

    def getHoras(self):
        """
        Obtiene la cantidad de horas trabajadas al mes.

        Returns:
            int: La cantidad de horas trabajadas.
        """
        return self.horas

    def getValor(self):
        """
        Obtiene el valor de la hora trabajada.

        Returns:
            float: El valor de la hora trabajada.
        """
        return self.valor

    def calcSalario(self):
        """
        Calcula el salario mensual del trabajador.

        Returns:
            float: El salario mensual calculado.
        """
        return self.horas * self.valor

def verificar():
    """
    Función para verificar el salario del trabajador y mostrar un mensaje de resultado en una ventana emergente.
    """
    trabajador = Trabajador(nombre=nombre_entry.get(), horas=int(horas_entry.get()), valor=float(valor_entry.get()))

    if trabajador.calcSalario() > 450000:
        string = f'Nombre: {trabajador.getNombre()} \nSalario Mensual: {trabajador.calcSalario()}'
    else:
        string = f'Nombre: {trabajador.getNombre()}'

    messagebox.showinfo("Resultado", string)

# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 22 Capitulo 4")
window.geometry("400x200")

nombre_label = tk.Label(window, text="Nombres:", anchor="e")
nombre_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

nombre_entry = tk.Entry(window)
nombre_entry.grid(row=0, column=1, padx=10, pady=10)

horas_label = tk.Label(window, text="Horas Trabajadas al Mes:", anchor="e")
horas_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

horas_entry = tk.Entry(window)
horas_entry.grid(row=2, column=1, padx=10, pady=10)

valor_label = tk.Label(window, text="Valor Hora Trabajada:", anchor="e")
valor_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

valor_entry = tk.Entry(window)
valor_entry.grid(row=3, column=1, padx=10, pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=verificar)
calcular_button.grid(row=8, columnspan=2, padx=10, pady=10)

window.mainloop()
