class Nodo:
    """
    Clase que representa un Nodo
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    """
    Clase que representa una pila para almacenar datos
    """
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        if self.tope is None:
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def cima(self):
        if self.tope is None:
            return None
        return self.tope.dato

    def imprimir(self):
        if self.tope is None:
            print("La pila está vacía")
            return
        else:
            print("Contenido de la pila:")
            nodo_actual = self.tope
            while nodo_actual is not None:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente