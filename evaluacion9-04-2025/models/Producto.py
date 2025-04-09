"""
Archivo: Producto.py
Descripcion: Este archivo contiene la clase Producto que se utiliza para
"""

class Producto:
    """Clase que representa un producto en el inventario."""
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        #nombre, categoria, precio, stock
        
    def agregar_stock(self, cantidad_agregar):
        """Funcion para agregar stock a un producto.

        Args:
            cantidad_agregar (int): cantidad a agregar a stock
        """
        self.stock += cantidad_agregar
        print(f"Se han agregado {cantidad_agregar} unidades al stock de {self.nombre}. Nuevo stock: {self.stock}")
        
    def retirar_stock(self, cantidad_retirar):
        """Funcion para retirar cierta cantidad de stock de un producto. 

        Args:
            cantidad_retirar (int): cantidad a retirar de stock
        """
        if self.stock < cantidad_retirar:
            print("No se puede retirar esa cantidad ya que no cuenta con suficiente unidades en el inventario actual. ")
            return
        else:
            self.stock -= cantidad_retirar
            print(f"Se han retirado {cantidad_retirar} unidades al stock de {self.nombre}. Nuevo stock: {self.stock}")
        
    def mostrar_info(self):
        """Funcion para mostrar la informacion de un producto en el inventario.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Categoria: {self.categoria}")
        print(f"Precio: C${self.precio}")
        print(f"Stock: {self.stock}")
        print(f"Valor total: C${self.precio * self.stock}")
            