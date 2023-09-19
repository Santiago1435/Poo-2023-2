import tkinter as tk
from tkinter import messagebox
import math


class Triangulo:
    def __init__(self, lado):
        """
        Inicializa un objeto Triángulo con un lado dado.
        """
        self.lado = lado

    def getPerimetro(self):
        """
        Calcula y devuelve el perímetro del triángulo equilátero.
        """
        return self.lado * 3

    def getAltura(self):
        """
        Calcula y devuelve la altura del triángulo equilátero.
        """
        return math.sqrt(self.lado ** 2 - (self.lado / 2) ** 2)

    def getArea(self):
        """
        Calcula y devuelve el área del triángulo equilátero.
        """
        return math.sqrt(3) * (1 / 4) * self.lado ** 2


def calcularMedidas():
    """
    Calcula las medidas de un triángulo equilátero y muestra el resultado en una ventana de mensaje.
    """
    try:
        lado = float(lado_entry.get())
        if lado <= 0:
            raise ValueError("El lado debe ser un número positivo.")

        triangulo = Triangulo(lado)

        resultado = f'Perímetro: {triangulo.getPerimetro():.2f} \nAltura: {triangulo.getAltura():.2f} \nÁrea: {triangulo.getArea():.2f} \n'

        messagebox.showinfo("Resultado", resultado)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Calculadora de Triángulo Equilátero")
window.geometry("300x180")  # Tamaño de la ventana

# Crear un marco para centrar los elementos
frame = tk.Frame(window)
frame.pack(expand=True, fill="both")

lado_label = tk.Label(frame, text="Lado:", anchor="e")
lado_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="w")

lado_entry = tk.Entry(frame)
lado_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Crear botón para calcular y centrarlo
calcular_button = tk.Button(frame, text="Calcular", command=calcularMedidas)
calcular_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Centrar el marco en la ventana
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

window.mainloop()
