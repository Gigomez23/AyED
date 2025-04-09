"""Crea un programa que permita registrar productos, actualizar stock, mostrar reportes 
y buscar productos por nombre, aplicando los fundamentos de programación en Python y organizando el código en módulos.
Organizar el código utilizando funciones y clases, y separar las partes del 
programa en módulos (es decir, en archivos .py diferentes).
Autores: Gabriel Gomez, Gabriel Lacayo
"""
from modules.funciones_generales import *
from modules.funciones_menu import *


def main():
    """Funcion principal del programa."""
    activo = True
    inventario = []
    while activo:
        clear_screen()
        print("Bienvenido al programa de gestion de inventario.")
        print(opciones)
        opcion = input("Digite la seleccion de accion: ")
        match opcion:
            case "1":
                agregar_producto(inventario)
            case "2":
                agregar_stock_producto(inventario)
            case "3":
                retirar_producto(inventario)
            case "4":
                mostrar_informacion_del_producto(inventario)
            case "5":
                clear_screen()
                print("Productos en el inventario:")
                mostrar_productos(inventario)
                limpiar()
            case "6":
                activo = False
            case _:
                print("Opcion no valida.")
        


if __name__ == "__main__":
    """Punto de partida del programa"""
    main()