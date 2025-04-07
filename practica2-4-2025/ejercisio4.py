import sys
import os

# Add the path of folder_a to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the desired module or function
# from file_a import your_function  # Replace 'your_function' with the actual function or class name

from Models.Inventario import Inventario
from Models.Producto import Producto

def ejercisio4():
    inventario = Inventario()
    while True:
        print("1. Agregar producto\n2. Mostrar inventario\n3. Modificar articulo\n4. Ver datos de producto\n5. Salir")
        seleccion = int(input("Selecciona una opción: "))
        match seleccion:
            case 1:
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                producto = Producto(codigo, nombre, precio, cantidad)
                inventario.agregar_inventario(producto)
            case 2:
                inventario.mostrar_inventario()
            case 3:
                inventario.modificar_articulo()
            case 4:
                inventario.ver_datos_de_producto()
            case 5:
                break
            case _:
                print("Opción no válida.")
                
if __name__ == "__main__":
    ejercisio4()