import tkinter as tk
from tkinter import messagebox

class Comparacion:
    def __init__(self, a, b):
        """
        Inicializa un objeto Comparacion con dos números dados (a y b).
        """
        self.a = a
        self.b = b

    def comparar(self):
        if self.a > self.b:
            return 1
        elif self.a == self.b:
            return 2
        else:
            return 3

def calcular():
    nuevaComparacion = Comparacion(float(a_entry.get()), float(b_entry.get()))

    resultado = nuevaComparacion.comparar()
    if resultado == 1:
        string = f'{float(a_entry.get())} es mayor que {float(b_entry.get())}'
    elif resultado == 2:
        string = f'{float(a_entry.get())} es igual a {float(b_entry.get())}'
    else:
        string = f'{float(a_entry.get())} es menor que {float(b_entry.get())}'

    messagebox.showinfo("Resultado", string)

# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 7 Capitulo 4")
window.geometry("300x180")  # Tamaño de la ventana

# Crear un marco para centrar los elementos
frame = tk.Frame(window)
frame.pack(expand=True, fill="both")

a_label = tk.Label(frame, text="Número A:")
a_label.grid(row=0, column=0, padx=(10, 0), pady=10, sticky="e")

a_entry = tk.Entry(frame)
a_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

b_label = tk.Label(frame, text="Número B:")
b_label.grid(row=1, column=0, padx=(10, 0), pady=10, sticky="e")

b_entry = tk.Entry(frame)
b_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Crear botón para calcular y centrarlo
calcular_button = tk.Button(frame, text="Calcular", command=calcular)
calcular_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Centrar el marco en la ventana
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

window.mainloop()
