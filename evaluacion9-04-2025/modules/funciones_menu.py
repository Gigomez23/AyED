"""
Archivo: funciones_menu.py
Descripcion: Este archivo contiene las funciones que se utilizan para
mostrar el menu y las opciones del programa.
"""
from models.Producto import Producto
from modules.funciones_generales import *

def mostrar_productos(inventario):
    """Funcion de menu para mostrar los productos en el inventario. 

    Args:
        inventario (array): lista que contiene los productos en el inventario
    """
    clear_screen()
    if not inventario:
        print("No hay productos en el inventario.")
    else:
        print("Productos en el inventario:")
        for producto in inventario:
            print({producto.nombre})
    print("")


def agregar_producto(inventario):
    """Funcion de menu para crear un producto nuevo. 

    Args:
        inventario (array): lista que contiene los productos en el inventario
    """
    clear_screen()
    print("Agregar producto nuevo al inventario")
    nombre_producto = input("Ingrese el nombre del producto: ")
    categoria_producto = input("Ingrese la categoria del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: C$"))
    stock_producto = int(input("Ingrese el stock del producto: "))
    if stock_producto < 0:
        print("No se puede agregar una cantidad negativa.")
        limpiar()
        return
    if stock_producto == 0:
        print("No se puede agregar una cantidad cero.")
        limpiar()
        return
    if precio_producto < 0:
        nuevo_producto = Producto(nombre_producto, categoria_producto, precio_producto, stock_producto)
        inventario.append(nuevo_producto)
        print(f"Producto {nombre_producto} agregado al inventario.")
        limpiar()
    

def agregar_stock_producto(inventario):
    """Funcion de menu para agregar stock a un producto. 

    Args:
        inventario (array): lista que contiene los productos en el inventario
    """
    clear_screen()
    mostrar_productos(inventario)
    nombre_producto = input("Ingrese el nombre del producto: ")
    for producto in inventario:
        if producto.nombre == nombre_producto:
            cantidad_agregar = int(input("Ingrese la cantidad a agregar: "))
            if cantidad_agregar < 0:
                print("No se puede agregar una cantidad negativa.")
                limpiar()
                return
            if cantidad_agregar == 0:
                print("No se puede agregar una cantidad cero.")
                limpiar()
                return
            if cantidad_agregar > 0:
                producto.agregar_stock(cantidad_agregar)
                limpiar()
            return
    print(f"Producto {nombre_producto} no encontrado en el inventario.")
    limpiar()


def retirar_producto(inventario):
    """Funcion de menu para retirar stock de un producto. 

    Args:
        inventario (array): lista que contiene los productos en el inventario
    """
    clear_screen()
    mostrar_productos(inventario)
    nombre_producto = input("Ingrese el nombre del producto: ")
    for producto in inventario:
        if producto.nombre == nombre_producto:
            cantidad_retirar = int(input("Ingrese la cantidad a retirar: "))
            if cantidad_retirar < 0:
                print("No se puede retirar una cantidad negativa.")
                limpiar()
                return
            if cantidad_retirar == 0:
                print("No se puede retirar una cantidad cero.")
                limpiar()
                return
            if cantidad_retirar > 0:
                producto.retirar_stock(cantidad_retirar)
                limpiar()
                return
            return
    print(f"Producto {nombre_producto} no encontrado en el inventario.")
    limpiar()



def mostrar_informacion_del_producto(inventario):
    """Funcion para mostrar informacion del producto. 

    Args:
        inventario (array): lista que contiene los productos en el inventario
    """
    clear_screen()
    mostrar_productos(inventario)
    nombre_producto = input("Ingrese el nombre del producto: ")
    for producto in inventario:
        if producto.nombre == nombre_producto:
            producto.mostrar_info()
            limpiar()
            return
    print(f"Producto {nombre_producto} no encontrado en el inventario.")
    limpiar()
    

    
    
