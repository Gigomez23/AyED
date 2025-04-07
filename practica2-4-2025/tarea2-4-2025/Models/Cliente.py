"""Crear una clase Cliente con atributos básicos (por ejemplo, ID, nombre y
contacto)"""

"""Se podrá incluir el uso de herencia
para diferenciar entre tipos de clientes (por ejemplo, cliente regular y cliente VIP)
y aplicar descuentos especiales"""

class Cliente:
    def __init__(self, id_cliente, nombre, contacto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contacto = contacto
        
    def __str__(self):
        return f"Cliente(ID: {self.id_cliente}, Nombre: {self.nombre}, Contacto: {self.contacto})"
    

class ClienteRegular(Cliente):
    def __init__(self, id_cliente, nombre, contacto):
        super().__init__(id_cliente, nombre, contacto)
        self.descuento = 0
        self.tipo_cliente = "Regular"
        

class ClienteVIP(Cliente):
    def __init__(self, id_cliente, nombre, contacto):
        super().__init__(id_cliente, nombre, contacto)
        self.descuento = 0.15 
        self.tipo_cliente = "VIP"
    