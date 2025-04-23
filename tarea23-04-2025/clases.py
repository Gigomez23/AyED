class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

# Insertar un nuevo valor al final de la lista
    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
        
    def contar(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def sumar(self):
        actual = self.cabeza
        suma = 0
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma
    
    def imprimir_primer_valor(self):
        if self.cabeza:
            print(f"El primer valor de la lista es: {self.cabeza.valor}")
        else:
            print("La lista está vacía")
            
            
    