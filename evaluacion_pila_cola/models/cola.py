class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Dato almacenado en el nodo
        self.siguiente = None  # Referencia al siguiente nodo

class Cola:
    def __init__(self):
        self.frente = None  # Nodo al frente de la cola
        self.final = None   # Nodo al final de la cola

    def insertar(self, dato):
        """Agrega un nuevo elemento al final de la cola."""
        nuevo = Nodo(dato)
        if self.final is None:  # La cola está vacía
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo


    def eliminar(self):
        """Elimina el primer elemento agregado."""
        if self.frente is None:
            print("No hay datos.")
            return None
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return eliminado

    def imprimir(self):
        """Funciȯn para imprimir los datos de la pila"""
        if self.frente:
            print("Contenido de la cola: ")
            nodo_actual = self.frente
            while nodo_actual is not None:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente
        else:
            print("La cola está vacía")

    def mostrar_valores(self):
        """Muestra la lista actual de elementos en espera."""
        lista = []
        if self.frente is None:
            return ["Cola vacía"]
        else:
            actual = self.frente
            while actual is not None:
                lista.append(actual.dato)
                actual = actual.siguiente
            return lista