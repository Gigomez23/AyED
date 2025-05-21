class Pila:
    #almacenar los elementos de la pila
    def __init__(self):
        self.items = []
    #comprobar si la pila esta vacía
    def esta_vacia(self):
        return len(self.items) == 0
    #Agregar un elemento al tope (final) de la pila.
    def apilar(self, item):
        self.items.append(item)
    #Remover y devolver el elemento que está en el tope de la pila.
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    #Devolver la cantidad de elementos que hay en la pila actualmente.
    def tamano(self):
        return len(self.items)
