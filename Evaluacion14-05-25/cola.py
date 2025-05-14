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
        print(f"Paciente '{dato}' agregado")

    def eliminar(self):
        """Atiende al siguiente paciente (elimina el nodo del frente)."""
        if self.frente is None:
            print("No hay pacientes para atender.")
            return None
        eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        print(f"Paciente '{eliminado}' atendido ")
        return eliminado

    def imprimir(self):
        """Muestra la lista actual de pacientes en espera."""
        if self.frente is None:
            print("No hay pacientes en espera.")
        else:
            print("Pacientes en espera:")
            actual = self.frente
            while actual is not None:
                print(f"- {actual.dato}")
                actual = actual.siguiente
