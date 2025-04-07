from Models.Inventario import Inventario
from Models.Producto import Producto
from Models.Cliente import Cliente, ClienteRegular, ClienteVIP
from Models.Pedido import Pedido
from modulos.funciones_generales import *

def crear_pedidos(inventario: Inventario, pedidos, clientes):
    clear_screen()
    activo = True
    id = f"00{len(pedidos) + 1}"
    id_cliente = f"00{len(clientes) + 1}"
    cliente = None
    pedido = None
    print("Crear pedido")
    print("Agregue el cliente")
    print("1. Crear cliente\n2. Seleccionar cliente existente\n")
    seleccion = int(input("Selecciona una opción: "))
    if seleccion == 1:
        nombre = input("Nombre del cliente: ")
        tipo_cliente = input("Tipo de cliente (Regular o VIP): ")
        contacto_cliente = input("Contacto del cliente: ")
        if tipo_cliente.lower() == "regular":
            cliente = ClienteRegular(id_cliente, nombre, contacto_cliente)
            clientes.append(cliente)
        elif tipo_cliente.lower() == "vip":
            cliente = ClienteVIP(id_cliente, nombre, contacto_cliente)
            clientes.append(cliente)
        else:
            print("Tipo de cliente no válido.")
            return
    elif seleccion == 2:
        print("Clientes existentes:")
        for i, c in enumerate(clientes):
            print(f"{i + 1}. {c.nombre}")
        seleccion_cliente = int(input("Selecciona el cliente: "))
        cliente = clientes[seleccion_cliente - 1]
    else:
        print("Opción no válida.")
        return
    pedido = Pedido(id, cliente)
    pedidos.append(pedido)
    clear_screen()
    while activo:
        print("Agregue Productos al Pedido.")
        for i, p in enumerate(inventario.articulos):
            print(f"{i + 1}. {p.nombre} - C$ {p.precio} ({p.cantidad} disponibles)")
        seleccion_producto = int(input("Selecciona el producto: "))
        cantidad_producto = int(input("Cantidad del producto: "))
        producto = inventario.articulos[seleccion_producto - 1]
        if cantidad_producto > producto.cantidad:
            print("No hay suficiente cantidad del producto.")
            return
        pedido.agregar_productos(producto, cantidad_producto)
        producto.cantidad -= cantidad_producto
        print(f"Producto {producto.nombre} agregado al pedido.")
        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != "s":
            break
    pedido.calcular_descuentos()
    pedido.mostrar_informacion()
    
    
    
    
                        
                        
    
    