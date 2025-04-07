from Models.Inventario import Inventario
from modulos.funciones_generales import *
from Models.Cliente import ClienteRegular, ClienteVIP

def gestionador_de_clientes(inventario: Inventario, lista_clientes):
    activo_clientes = True
    while activo_clientes:
        clear_screen()
        print("Gestionar Clientes")
        print("1. Agregar Cliente")
        print("2. Ver Clientes")
        print("3. Salir")
        seleccion_clientes = int(input("Selecciona una opción: "))
        match seleccion_clientes:
            case 1:
                id_cliente = f"00{len(lista_clientes) + 1}"
                nombre = input("Nombre del cliente: ")
                tipo_cliente = input("Tipo de cliente (Regular o VIP): ")
                contacto_cliente = input("Contacto del cliente: ")
                if tipo_cliente.lower() == "regular":
                    cliente = ClienteRegular(id_cliente, nombre, contacto_cliente)
                    lista_clientes.append(cliente)
                elif tipo_cliente.lower() == "vip":
                    cliente = ClienteVIP(id_cliente, nombre, contacto_cliente)
                    lista_clientes.append(cliente)
            case 2: 
                clear_screen()
                for cliente in lista_clientes:
                    print(f"ID: {cliente.id_cliente}, Nombre: {cliente.nombre}, Contacto: {cliente.contacto}")
                limpiar()
            case 3: 
                print("Saliendo...")
                activo_clientes = False
                limpiar()
            case _:
                print("Opción no válida.")
                limpiar()