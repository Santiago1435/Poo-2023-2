import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, codigoEmpleado):
        """
        Inicializa un objeto Empleado con nombre y código de empleado.
        """
        self.nombre = nombre
        self.codigoEmpleado = codigoEmpleado
        self.HorasTrabajadas = 0
        self.ValorHora = 0
        self.PorcentajeRetencion = 0

    def setHorasTrabajadas(self, horas):
        """
        Establece las horas trabajadas por el empleado.
        """
        self.HorasTrabajadas = horas

    def setValorHora(self, valor):
        """
        Establece el valor de la hora de trabajo del empleado.
        """
        self.ValorHora = valor

    def setPorcentajeRetencion(self, porcentaje):
        """
        Establece el porcentaje de retención en la fuente para el empleado.
        """
        self.PorcentajeRetencion = porcentaje

    def getNombres(self):
        """
        Obtiene el nombre del empleado.
        """
        return self.nombre

    def getCodigo(self):
        """
        Obtiene el código de empleado.
        """
        return self.codigoEmpleado

    def getSalarioBruto(self):
        """
        Calcula y devuelve el salario bruto del empleado.
        """
        return self.ValorHora * self.HorasTrabajadas

    def getSalarioNeto(self):
        """
        Calcula y devuelve el salario neto del empleado después de aplicar la retención.
        """
        return self.ValorHora * self.HorasTrabajadas * (1 - (self.PorcentajeRetencion / 100))

def calcular_salario():
    """
    Calcula el salario neto y bruto de un empleado y muestra el resultado en una ventana de mensaje.

    Obtiene los datos ingresados por el usuario desde las entradas de la interfaz gráfica, crea un objeto Empleado con esos datos,
    calcula el salario neto y bruto del empleado y muestra el resultado en una ventana de mensaje.

    Para ello, accede a las entradas por su índice en la lista 'entries', donde se encuentran los campos de entrada.
    """
    nuevo = Empleado(nombre=entries[0].get(), codigoEmpleado=entries[1].get())  # Acceder a las entradas por su índice en la lista
    nuevo.setHorasTrabajadas(horas=float(entries[2].get()))
    nuevo.setValorHora(valor=float(entries[3].get()))
    nuevo.setPorcentajeRetencion(porcentaje=float(entries[4].get()))
    resultado = f'Nombres: {nuevo.getNombres()} \n Código: {nuevo.getCodigo()} \n Salario neto: {nuevo.getSalarioNeto()} \n Salario Bruto: {nuevo.getSalarioBruto()}'
    messagebox.showinfo("Resultado", resultado)


# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Ejercicio 18 Capítulo 3")
window.geometry("400x250")

# Etiquetas y campos de entrada
labels = ["Nombres:", "Código:", "Horas Trabajadas al Mes:", "Valor Hora Trabajada:", "Porcentaje Retención en la Fuente:"]
entries = [tk.Entry(window) for _ in range(5)]

for i, label_text in enumerate(labels):
    label = tk.Label(window, text=label_text)
    label.grid(row=i, column=0, sticky="e")
    entries[i].grid(row=i, column=1, padx=10, pady=10)

# Botón para calcular el salario
calcular_button = tk.Button(window, text="Calcular", command=calcular_salario)
calcular_button.grid(row=5, columnspan=2, padx=10, pady=10)

window.mainloop()
