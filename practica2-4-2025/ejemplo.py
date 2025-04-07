"""Ejemplificando clases en python"""
from modulo import *

if __name__ == "__main__":
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    
    alumno=Alumno(nombre, edad)
    alumno.mostrar_informacion()
    alumno.saludar()
    
    firu = Perro("Firu", "Labrador", 0.5)
    print(firu.nombre)
    print(firu.raza)
    print(firu.altura)
    
    firu.imprimir_datos(1)
    firu.imprimir_datos(2)
    firu.imprimir_datos(3)
    
    print(firu)