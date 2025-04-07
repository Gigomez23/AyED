class Producto:
    """código, nombre, precio y
cantidad en stock."""
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def modificar_stock(self):
        cantidad = int(input("Introduce la nueva cantidad de stock: "))
        self.cantidad = cantidad
        print(f"Se ha modificado el stock del producto {self.nombre}. Nuevo stock: {self.cantidad}")
        
    def modificar_precio(self):
        precio_nuevo = float(input("Introduce el nuevo precio: "))
        self.precio = precio_nuevo
        print(f"Se ha modificado el precio del producto {self.nombre}. Nuevo precio: C${self.precio}")
        
    def modificar_nombre(self):
        nombre_nuevo = input("Introduce el nuevo nombre: ")
        self.nombre = nombre_nuevo
        print(f"Se ha modificado el nombre del producto {self.nombre}.")
        
    def modificar_codigo(self):
        codigo_nuevo = input("Introduce el nuevo codigo: ")
        self.codigo = codigo_nuevo
        print(f"Se ha modificado el codigo del producto {self.nombre}. Nuevo codigo: {self.codigo}")
    
    def mostrar_informacion(self):
        print(f"Codigo: {self.codigo}, Nombre: {self.nombre}, Precio: C${self.precio}, Stock: {self.cantidad}")