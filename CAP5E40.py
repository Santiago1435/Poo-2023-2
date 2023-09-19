import tkinter as tk
import math
from tkinter import messagebox

class NumeroOperaciones:
    def __init__(self, valor):
        """
        Inicializa un objeto NumeroOperaciones con un valor.

        Args:
            valor (float): El valor del número.
        """
        self.valor = valor

    def getValor(self):
        """
        Obtiene el valor del número.

        Returns:
            float: El valor del número.
        """
        return self.valor

    def getSqrt(self):
        """
        Calcula y obtiene la raíz cuadrada del número.

        Returns:
            float: La raíz cuadrada del número.
        """
        return math.sqrt(self.valor)

    def getCuadrado(self):
        """
        Calcula y obtiene el cuadrado del número.

        Returns:
            float: El cuadrado del número.
        """
        return self.valor ** 2

    def getCubo(self):
        """
        Calcula y obtiene el cubo del número.

        Returns:
            float: El cubo del número.
        """
        return self.valor ** 3

def realizarOperacion():
    seleccionado = numeros_listbox.curselection()
    if seleccionado:
        numero_seleccionado = numeros_listbox.get(seleccionado[0])
        if numero_seleccionado >= 0:
            numero = NumeroOperaciones(numero_seleccionado)
            resultado = f'Número: {numero.getValor()} \nRaíz: {numero.getSqrt()} \nCuadrado: {numero.getCuadrado()} \nCubo: {numero.getCubo()}'
            messagebox.showinfo("Resultado", resultado)
        else:
            messagebox.showerror("Error", "Debe ser un número positivo")

def agregarNumero():
    numero = int(numero_entry.get())
    if numero >= 0:
        numeros_listbox.insert(tk.END, numero)
    else:
        messagebox.showerror("Error", "Debe ser un número positivo")

# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 40 Capitulo 5")
window.geometry("400x400")

numero_label = tk.Label(window, text="Número:")
numero_label.place(x=50, y=50)

numero_entry = tk.Entry(window)
numero_entry.place(x=150, y=50)

añadir_button = tk.Button(window, text="Añadir", command=agregarNumero)
añadir_button.place(x=190, y=100)

numeros_listbox = tk.Listbox(window, selectmode=tk.SINGLE)
numeros_listbox.place(x=150, y=150)

operacion_button = tk.Button(window, text="Realizar Operación", command=realizarOperacion)
operacion_button.place(x=160, y=350)

window.mainloop()
