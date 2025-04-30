"""
archivo: models.py

Este módulo contiene la implementación de una pila y funciones relacionadas.
"""

class Pila:
    """
    Clase que representa una pila con operaciones básicas.
    """
    def __init__(self, capacidad):
        """
        Inicializa una pila con una capacidad dada.
        Args:
            capacidad (int): Capacidad máxima de la pila.
        """
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.tope = -1
        
    def push(self, item):
        """
        Agrega un elemento a la cima de la pila.
        Args:
            item (int): Elemento a agregar a la pila.

        Raises:
            Exception: Si la pila está llena.
        """
        if self.tope < self.capacidad - 1:
            self.tope += 1
            self.items[self.tope] = item
            print(f"Elemento {item} agregado a la pila.")
        else:
            raise Exception("Pila llena")
        
    def pop(self):
        """
        Elimina y devuelve el elemento en la cima de la pila.
        Raises:
            Exception: Si la pila está vacía.

        Returns:
            int: Elemento eliminado de la pila.
        """
        if self.is_empty():
            raise Exception("Pila vacía")
        else:
            eliminado = self.items[self.tope]
            self.items[self.tope] = None
            self.tope -= 1
            print(f"Elemento {eliminado} eliminado de la pila.")
            return eliminado
    
    def is_empty(self):
        """
        Verifica si la pila está vacía.
        Returns:
            True si la pila está vacía, False en caso contrario.
        """
        return self.tope == -1
    
    def cima(self):
        """
        Devuelve el elemento en la cima de la pila sin eliminarlo.
        Raises:
            Exception: Si la pila está vacía.

        Returns:
            int: Elemento en la cima de la pila.
        """
        if not self.is_empty():
            return self.items[self.tope]
        else:
            raise Exception("Pila vacía")
    
    def imprimir(self):
        """
        Imprime el contenido de la pila desde el tope hasta la base.
        """
        if self.is_empty():
            print("Pila vacía")
        else:
            print("Contenido de la pila:")
            for i in range(self.tope, -1, -1):
                print(self.items[i])
                
    def __str__(self):
        if self.is_empty():
            return "Pila vacía"
        else:
            return "Contenido de la pila: " + ", ".join(str(self.items[i]) for i in range(self.tope, -1, -1))
        
        
    def organizar_pares_impares(self):
        """
        Organiza la pila separando los números pares de los impares.
        Raises:
            Exception: Si la pila está vacía.

        Returns:
            self: Pila organizada.
        """
        if self.is_empty():
            raise Exception("Pila vacía")
        
        pila_pares = Pila(self.capacidad)
        pila_impares = Pila(self.capacidad)
        
        while not self.is_empty():
            elemento = self.pop()
            if elemento % 2 == 0:
                pila_pares.push(elemento)
            else:
                pila_impares.push(elemento)
        
        while not pila_impares.is_empty():
            self.push(pila_impares.pop())
        
        while not pila_pares.is_empty():
            self.push(pila_pares.pop())
        print("Pila organizada: ", self)
        return self
    
    def ordenar_mayor_menor(self):
        """
        Organiza la pila de mayor a menor.
        Raises:
            Exception: Si la pila está vacía.

        Returns:
            self: Pila ordenada.
        """
        if self.is_empty():
            raise Exception("Pila vacía")
        
        pila_aux = Pila(self.capacidad)
        
        while not self.is_empty():
            elemento = self.pop()
            while not pila_aux.is_empty() and pila_aux.cima() > elemento:
                self.push(pila_aux.pop())
            pila_aux.push(elemento)
        
        while not pila_aux.is_empty():
            self.push(pila_aux.pop())
        print("Pila ordenada de mayor a menor: ", self)
        return self
    
def Convbinario(numero: int) -> str:
    """
    Convierte un número entero a su representación binaria usando una pila.

    Args:
        numero (int): Número entero positivo a convertir.

    Returns:
        str: Representación binaria del número.
    """
    if numero == 0:
        return "0"

    pila = []

    # Proceso de conversión
    while numero > 0:
        residuo = numero % 2
        pila.append(str(residuo))  # Guardamos como cadena
        numero //= 2

    # Extraemos los bits de la pila (de arriba hacia abajo)
    binario = ""
    while pila:
        binario += pila.pop()

    return binario

    
    