"""Pedido que contenga información sobre el cliente, la lista
de productos solicitados y el total de la venta."""

class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = []
        self.cantidades = []
        self.total_venta = 0
        
    def mostrar_informacion(self):
        print(f"Pedido: {self.id_pedido}")
        print(f"Cliente: {self.cliente.nombre}, Tipo de cliente: {self.cliente.tipo_cliente}")
        print("Productos solicitados:")
        for producto in self.productos:
            print(f"Producto: {producto.nombre}, Precio: C${producto.precio}")
        if self.cliente.tipo_cliente == "VIP":
            print("Descuento aplicado: 15%")
        else:
            print("Descuento aplicado: 0%")
        print("Total de la venta: C$ ", self.total_venta)
    
        
    def agregar_productos(self, producto, cantidad):
        self.productos.append(producto)
        self.cantidades.append(cantidad)
        self.total_venta = self.total_venta + (producto.precio * cantidad)
    
    def calcular_descuentos(self):
        self.total_venta = self.total_venta - (self.total_venta * self.cliente.descuento)
    
    def total_venta(self):
        self.total_venta = 0
        for i in range(len(self.productos)):
            self.total_venta += self.productos[i].precio * self.cantidades[i]
        if self.cliente.tipo_cliente == "VIP":
            self.total_venta *= 0.85
    
    def mostrar_productos(self):
        print('Productos en el pedido:')
        for i in self.productos:
            print(f"Producto: {self.productos[i].producto.nombre}, Precio C$ {self.productos[i].producto.precio}, Cantidad: {self.cantidades[i]}")
        print(f"Total de la venta: C$ {self.total_venta}")
    