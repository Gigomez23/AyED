""""Diversas funciones en archivo especifoco para funciones. Para demostrar la modularidad"""""
import os
import platform

clear = None
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')
    
def clear_function():
    input("Presione cualquier tecla para borrar y continuar....")
    clear()

def suma(a, b):
    """Suma dos números"""
    return a + b

def resta(a, b):
    """Resta dos números"""
    return a - b

def multiplicacion(a, b):
    """Multiplica dos números"""
    return a * b

def division(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(a, b):
    """Eleva un número a la potencia de otro"""
    return a ** b