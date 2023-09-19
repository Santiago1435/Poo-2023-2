import math
import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat


# Clase para cálculos relacionados con un círculo
class Circulo:
    def __init__(self, radio):
        """
        Inicializa un objeto Circulo con un radio.

        Args:
            radio (float): El radio del círculo.
        """
        self.radio = radio

    def calcular_area(self):
        """
        Calcula el área del círculo.

        Returns:
            float: El área del círculo.
        """
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        """
        Calcula el perímetro del círculo.

        Returns:
            float: El perímetro del círculo.
        """
        return 2 * math.pi * self.radio


# Clase para cálculos relacionados con un rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        """
        Inicializa un objeto Rectangulo con una base y una altura.

        Args:
            base (float): La base del rectángulo.
            altura (float): La altura del rectángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Calcula el área del rectángulo.

        Returns:
            float: El área del rectángulo.
        """
        return self.base * self.altura

    def calcular_perimetro(self):
        """
        Calcula el perímetro del rectángulo.

        Returns:
            float: El perímetro del rectángulo.
        """
        return 2 * self.base + 2 * self.altura


# Clase para cálculos relacionados con un cuadrado
class Cuadrado:
    def __init__(self, lado):
        """
        Inicializa un objeto Cuadrado con un lado.

        Args:
            lado (float): El lado del cuadrado.
        """
        self.lado = lado

    def calcular_area(self):
        """
        Calcula el área del cuadrado.

        Returns:
            float: El área del cuadrado.
        """
        return self.lado ** 2

    def calcular_perimetro(self):
        """
        Calcula el perímetro del cuadrado.

        Returns:
            float: El perímetro del cuadrado.
        """
        return 4 * self.lado


# Clase para cálculos relacionados con un triángulo rectángulo
class TrianguloRectangulo:
    def __init__(self, base, altura):
        """
        Inicializa un objeto TrianguloRectangulo con una base y una altura.

        Args:
            base (float): La base del triángulo.
            altura (float): La altura del triángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Calcula el área del triángulo.

        Returns:
            float: El área del triángulo.
        """
        return 0.5 * self.base * self.altura

    def calcular_perimetro(self):
        """
        Calcula el perímetro del triángulo rectángulo.

        Returns:
            float: El perímetro del triángulo rectángulo.
        """
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        return self.base + self.altura + hipotenusa

    def calcular_hipotenusa(self):
        """
        Calcula la longitud de la hipotenusa del triángulo rectángulo.

        Returns:
            float: La longitud de la hipotenusa.
        """
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def determinar_tipo(self):
        """
        Determina el tipo de triángulo (equilátero, isósceles o escaleno).

        Returns:
            str: El tipo de triángulo.
        """
        hipotenusa = math.sqrt(self.base ** 2 + self.altura ** 2)
        if self.base == self.altura and hipotenusa == self.base:
            return "Equilátero"
        elif self.base != self.altura and hipotenusa != self.base:
            return "Escaleno"
        else:
            return "Isósceles"


# Clase para cálculos relacionados con un rombo
class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor):
        """
        Inicializa un objeto Rombo con las diagonales mayor y menor.

        Args:
            diagonal_mayor (float): La longitud de la diagonal mayor.
            diagonal_menor (float): La longitud de la diagonal menor.
        """
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        """
        Calcula el área del rombo.

        Returns:
            float: El área del rombo.
        """
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        """
        Calcula el perímetro del rombo.

        Returns:
            float: El perímetro del rombo.
        """
        return self.diagonal_mayor * 2 + self.diagonal_menor * 2


# Clase para cálculos relacionados con un trapecio
class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        """
        Inicializa un objeto Trapecio con las bases mayor y menor, la altura y los lados.

        Args:
            base_mayor (float): La longitud de la base mayor.
            base_menor (float): La longitud de la base menor.
            altura (float): La altura del trapecio.
            lado1 (float): La longitud del lado 1.
            lado2 (float): La longitud del lado 2.
        """
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        """
        Calcula el área del trapecio.

        Returns:
            float: El área del trapecio.
        """
        return (self.base_mayor + self.base_menor) * self.altura / 2

    def calcular_perimetro(self):
        """
        Calcula el perímetro del trapecio.

        Returns:
            float: El perímetro del trapecio.
        """
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2


def crearFigura():
    figura_seleccionada = menu_var.get()

    if figura_seleccionada == 'Círculo':
        radio = askfloat("Ingresar Dato", "Ingrese el radio del círculo:")
        if radio is not None:
            figura = Circulo(radio=radio)

    if figura_seleccionada == 'Rectángulo':
        base = askfloat("Ingresar Dato", "Ingrese la base del rectángulo:")
        altura = askfloat("Ingresar Dato", "Ingrese la altura del rectángulo:")
        if base is not None and altura is not None:
            figura = Rectangulo(altura=altura, base=base)

    if figura_seleccionada == 'Cuadrado':
        lado = askfloat("Ingresar Dato", "Ingrese el lado del cuadrado:")
        if lado is not None:
            figura = Cuadrado(lado=lado)

    if figura_seleccionada == 'Triángulo Rectángulo':
        base = askfloat("Ingresar Dato", "Ingrese la base del Triángulo:")
        altura = askfloat("Ingresar Dato", "Ingrese la altura del Triángulo:")
        if base is not None and altura is not None:
            figura = TrianguloRectangulo(altura=altura, base=base)

    if figura_seleccionada == 'Rombo':
        diagonalM = askfloat("Ingresar Dato", "Ingrese la diagonal mayor del rombo:")
        diagonalm = askfloat("Ingresar Dato", "Ingrese la diagonal menor del rombo:")
        if diagonalM is not None and diagonalm is not None:
            figura = Rombo(diagonal_mayor=diagonalM, diagonal_menor=diagonalm)

    if figura_seleccionada == 'Trapecio':
        baseM = askfloat("Ingresar Dato", "Ingrese la base mayor del trapecio:")
        basem = askfloat("Ingresar Dato", "Ingrese la base menor del trapecio:")
        altura = askfloat("Ingresar Dato", "Ingrese la altura del trapecio:")
        lado1 = askfloat("Ingresar Dato", "Ingrese el lado 1 del trapecio:")
        lado2 = askfloat("Ingresar Dato", "Ingrese el lado 2 del trapecio:")
        if (baseM is not None and basem is not None and altura is not None and
                lado1 is not None and lado2 is not None):
            figura = Trapecio(base_mayor=baseM, base_menor=basem, altura=altura, lado1=lado1, lado2=lado2)

    if 'figura' in locals():
        resultado = f'Área: {float(figura.calcular_area())} \nPerímetro: {float(figura.calcular_perimetro())}'
        messagebox.showinfo("Área y Perímetro", resultado)


# Configuración general de la ventana ejecutable
window = tk.Tk()
window.title("Figuras Geométricas")
window.geometry("300x200")

menu_var = tk.StringVar(window)
menu_var.set("Círculo")  # Opción por defecto

menu = tk.OptionMenu(window, menu_var, "Círculo", "Cuadrado", "Rectángulo", "Triángulo Rectángulo", "Rombo", "Trapecio")
menu.pack(pady=20)

# Botón para crear la figura
calcular_button = tk.Button(window, text="Crear", command=crearFigura)
calcular_button.pack()

window.mainloop()
