from Models.Inventario import Inventario
from Models.Producto import Producto
from modulos.funciones_generales import *

def gestionador_inventario(inventario: Inventario):
    clear_screen()
    activo = True
    while activo:
        print("Gestion de Productos e Inventario")
        print("1. Agregar Producto")
        print("2. Mostrar Productos")
        print("3. Modificar Producto")
        print("4. Ver datos de Producto")
        print("5. Salir")
        seleccion = int(input("Selecciona una opción: "))
        match seleccion:
            case 1: 
                clear_screen()
                print("Agregar producto")
                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                producto = Producto(codigo, nombre, precio, cantidad)
                inventario.agregar_inventario(producto)
                print("Producto agregado.")
                limpiar()
            case 2:
                clear_screen()
                print("Mostrar productos")
                inventario.mostrar_inventario()
                limpiar()
            case 3:
                clear_screen()
                print("Modificar producto")
                inventario.modificar_articulo()
                limpiar()
            case 4:
                clear_screen()
                print("Ver datos de producto")
                inventario.ver_datos_de_producto()
                limpiar()
            case 5:
                clear_screen()
                print("Saliendo...")
                activo = False
            case _:
                clear_screen()
                print("Opción no válida.")
                limpiar()
