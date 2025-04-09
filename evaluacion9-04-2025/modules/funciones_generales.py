"""Archivo que contiene funciones y variables generales para el programa."""
import os

opciones = "1. Agregar producto\n2. Agregar cantidad de producto\n3. Retirar cantidad de producto\n4. Mostrar informacion de un producto\n5. Mostrar productos\n6. Salir"


def clear_screen():
    """Funcion para limpiar la pantalla."""
    os.system('cls' if os.name == 'nt' else 'clear')

def limpiar():
    """Funcion para limpiar la pantalla despues de interaccion de usuario"""
    input("Presione Enter para continuar...")
    clear_screen()