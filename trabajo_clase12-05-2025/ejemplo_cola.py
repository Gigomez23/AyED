import time

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente=self.final=nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
            # print(f"Elemento {dato} agregado a la cola.")

    def eliminar(self):
        if self.frente is None:
            print("La cola está vacía. No se puede eliminar ningún elemento.")
        dato_eliminado = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato_eliminado

    def Imprimir(self):
        if self.frente is None:
            print("La cola está vacía.")
            return
        else:
            print("Elementos en la cola:")
            actual = self.frente
            while actual is not None:
                time.sleep(0.5)
                print(actual.dato)
                actual = actual.siguiente
        print("Pom pom.")

    def ver_frente(self):
        if self.frente is None:
            return None
        return self.frente.dato

    def esta_vacia(self):
        return self.frente is None