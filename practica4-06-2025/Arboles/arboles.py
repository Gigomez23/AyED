"""
archivo: arboles.py
Este módulo define la clase ArbolBin que representa un árbol binario.
"""

class Nodo:
    """Clase que representa un nodo en el árbol binario.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        
class ArbolBin:
    """Clase que representa un árbol binario.
    Esta clase permite insertar nodos, buscar valores y realizar recorridos en el árbol.
    Los recorridos implementados son en orden, preorden y postorden.
    """
    def __init__(self):
        """Inicializa el árbol binario con la raíz en None.
        """
        self.raiz = None
        
    def insertar(self, valor):
        """Inserta un nuevo nodo con el valor dado en el árbol binario.

        Args:
            valor: Valor del nodo a insertar.
        """
        self.raiz = self.insertarrecursivo(self.raiz, valor)
    
    def insertarrecursivo(self, nodo, valor):
        """Inserta un nuevo nodo de forma recursiva en el árbol binario.

        Args:
            nodo: Nodo actual en el que se está insertando.
            valor: Valor del nodo a insertar.

        Returns:
            nodo: Nodo actualizado con el nuevo valor insertado.
        """
        if nodo is None:
            return Nodo(valor)
        
        if valor < nodo.valor:
            nodo.izquierda = self.insertarrecursivo(nodo.izquierda, valor)
        else:
            nodo.derecha = self.insertarrecursivo(nodo.derecha, valor)
        
        return nodo
    
    def buscar(self, valor):
        return self.buscarrecursivo(self.raiz, valor)
    
    def buscarrecursivo(self, nodo, valor):
        """Busca un valor en el árbol binario de forma recursiva.

        Args:
            nodo: Nodo actual en el que se está buscando.
            valor: Valor a buscar en el árbol.

        Returns:
            bool: True si el valor se encuentra en el árbol, False en caso contrario.
        """
        if nodo is None:
            return False
        
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self.buscarrecursivo(nodo.izquierda, valor)
        else:
            return self.buscarrecursivo(nodo.derecha, valor)
        
    def recorrido_inorden(self, nodo):
        """Recorrido en orden del árbol binario. Izquierda, raíz, derecha.

        Args:
            nodo: Nodo actual en el que se está realizando el recorrido.
        """
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.recorrido_inorden(nodo.derecha)
            
    def recorrido_preorden(self, nodo):
        """Recorrido preorden del árbol binario. Raíz, izquierda, derecha.

        Args:
            nodo: Nodo actual en el que se está realizando el recorrido.
        """
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.recorrido_preorden(nodo.izquierda)
            self.recorrido_preorden(nodo.derecha)
            
    def recorrido_postorden(self, nodo):
        """Recorrido postorden del árbol binario. Izquierda, derecha, raíz.

        Args:
            nodo: Nodo actual en el que se está realizando el recorrido.
        """
        # recorrido post orden: izquierda, derecha, raiz
        if nodo is not None:
            self.recorrido_postorden(nodo.izquierda)
            self.recorrido_postorden(nodo.derecha)
            print(nodo.valor, end=' ')