import tkinter as tk
from tkinter import messagebox
import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        """
        Inicializa un objeto EcuacionCuadratica con coeficientes a, b y c.

        Args:
            a (float): Coeficiente a de la ecuación cuadrática.
            b (float): Coeficiente b de la ecuación cuadrática.
            c (float): Coeficiente c de la ecuación cuadrática.
        """
        self.a = a
        self.b = b
        self.c = c

    def encontrarRaices(self):
        """
        Encuentra las raíces de la ecuación cuadrática.

        Returns:
            tuple: Una tupla con las raíces de la ecuación. Si no hay raíces reales, devuelve (None, None).
        """
        discriminante = self.b**2 - 4 * self.a * self.c
        if discriminante < 0:
            return (None, None)
        raiz1 = (-1 * self.b + math.sqrt(discriminante)) / (2 * self.a)
        raiz2 = (-1 * self.b - math.sqrt(discriminante)) / (2 * self.a)
        return (raiz1, raiz2)

def calcularEcuacion():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        ecuacion = EcuacionCuadratica(a, b, c)
        raiz1, raiz2 = ecuacion.encontrarRaices()

        if raiz1 is not None and raiz2 is not None:
            resultado = f'Raíz 1: {raiz1}\nRaíz 2: {raiz2}'
        else:
            resultado = 'No hay raíces reales'

        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Ingresa coeficientes válidos (números reales)")

# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 22 Capitulo 4")

a_label = tk.Label(window, text="Coeficiente A:", anchor="e")
a_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

a_entry = tk.Entry(window)
a_entry.grid(row=0, column=1, padx=10, pady=10)

b_label = tk.Label(window, text="Coeficiente B:", anchor="e")
b_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

b_entry = tk.Entry(window)
b_entry.grid(row=1, column=1, padx=10, pady=10)

c_label = tk.Label(window, text="Coeficiente C:", anchor="e")
c_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

c_entry = tk.Entry(window)
c_entry.grid(row=2, column=1, padx=10, pady=10)

# Crear botón para calcular
calcular_button = tk.Button(window, text="Calcular", command=calcularEcuacion)
calcular_button.grid(row=8, columnspan=2, padx=10, pady=10)

window.mainloop()
