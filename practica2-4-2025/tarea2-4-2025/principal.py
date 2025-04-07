from modulos.gestion_inventario import gestionador_inventario
from modulos.gestion_pedidos import crear_pedidos
from modulos.gestion_clientes import gestionador_de_clientes
from Models.Inventario import Inventario
from Models.Producto import Producto
from modulos.funciones_generales import *

def main():
    activo = True
    inventario = Inventario()
    lista_pedidos = []
    lista_clientes = []
    while activo:
        clear_screen()
        print("Menu Principal")
        print("1. Gestionar Inventario")
        print("2. Gestionar Clientes")
        print("2. Crear Pedido")
        print("3. Salir")
        seleccion = int(input("Selecciona una opción: "))
        match seleccion:
            case 1:
                gestionador_inventario(inventario)
            case 2: 
                gestionador_de_clientes(inventario, lista_clientes)
            case 3:
                crear_pedidos(inventario, lista_pedidos, lista_clientes)
            case 3: 
                print("Saliendo...")
                activo = False
            case _:
                print("Opción no válida.")



if __name__ == "__main__":
    main()

"""Ejercicio #6 Facturación y reportes de ventas
Crear una clase Factura que simule el proceso de facturación de una venta. Los
estudiantes deberán encapsular los datos internos de la factura (como los
detalles de los productos, cantidades, precios y descuentos) y proveer métodos
para calcular el total de la venta, generar reportes simples y validar la integridad
de la información. Este ejercicio enfatiza la importancia de ocultar la
implementación interna y de diseñar interfaces claras y seguras para la gestión
de transacciones comerciales"""