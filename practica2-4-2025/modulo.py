"""Archivo que contiene las clases que vamos a estar utilizando."""

class Alumno:
    """
    Clase Alumno que representa a un estudiante.
    Atributos:
        nombre (str): Nombre del alumno.
        edad (int): Edad del alumno.
    Métodos:
        saludar(): Imprime un saludo con el nombre y la edad del alumno.
        mostrar_informacion(): Imprime la información del alumno.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        

class Perro:
    """
    Clase Perro que representa a un canino.
    Atributos:
        nombre (str): Nombre del perro.
        raza (int): Edad del perro.
        altura (float): altura del perro.
    Metodos: 
        __str__(): Devuelve una representación en cadena del perro.
        imprimir_datos(seleccion): Imprime los datos del perro según la opción seleccionada.
    """
    def __init__(self, nombre, raza, altura):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Altura: {self.altura}"
        
    def imprimir_datos(self, seleccion):
        match seleccion:
            case 1:
                print(f"Nombre: {self.nombre}")
            case 2:
                print(f"Raza: {self.raza}")
            case 3:
                print(f"Altura: {self.altura}")
            case _:
                print("Opción no válida")
        