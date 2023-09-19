import tkinter as tk
from tkinter import messagebox

class ListaNumerosOperaciones:
    def __init__(self, lista):
        """
        Inicializa un objeto ListaNumerosOperaciones con una lista de números.

        Args:
            lista (list): La lista de números.
        """
        self.lista = lista

    def getValorMayor(self):
        """
        Obtiene el valor mayor de la lista de números.

        Returns:
            int: El valor mayor de la lista.
        """
        if self.lista:
            return max(self.lista)
        else:
            return None

def realizarOperacion():
    seleccionados = numeros_listbox.curselection()
    numeros_seleccionados = [int(numeros_listbox.get(i)) for i in seleccionados]

    if numeros_seleccionados:
        lista = ListaNumerosOperaciones(numeros_seleccionados)
        valor_mayor = lista.getValorMayor()

        if valor_mayor is not None:
            resultado = f'Número mayor: {valor_mayor}'
            messagebox.showinfo("Resultado", resultado)
        else:
            messagebox.showinfo("Resultado", "La lista está vacía")

        numeros_listbox.delete(0, tk.END)

def agregarNumero():
    numero = int(numero_entry.get())
    if numero >= 0:
        numeros_listbox.insert(tk.END, numero)
    else:
        messagebox.showerror("Error", "No se pueden agregar valores negativos")

# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 41 Capitulo 5")
window.geometry("400x400")

numero_label = tk.Label(window, text="Número:")
numero_label.place(x=50, y=50)

numero_entry = tk.Entry(window)
numero_entry.place(x=150, y=50)

añadir_button = tk.Button(window, text="Añadir", command=agregarNumero)
añadir_button.place(x=190, y=100)

numeros_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
numeros_listbox.place(x=150, y=150)

operacion_button = tk.Button(window, text="Realizar Operación", command=realizarOperacion)
operacion_button.place(x=160, y=350)

window.mainloop()
