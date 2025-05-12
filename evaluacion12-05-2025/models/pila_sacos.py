"""
archivo: pila_sacos.py
Este módulo contiene la implementación de una pila de sacos.
"""

class Saco:
    """
    Clase que representa un saco de producto.
    Atributos:
        producto (str): Nombre del producto.
        peso (float): Peso del producto en kilogramos.
        hora_carga (str): Hora de carga del producto en formato HH:MM:SS.
    """
    def __init__(self, producto, peso, hora_carga):
        self.producto = producto
        self.peso = peso
        self.hora_carga = hora_carga

    def __str__(self):
        return f"{self.producto} ({self.peso} kg) - Cargado: {self.hora_carga}"


class NodoSaco:
    """
    Clase que representa un nodo en la pila de sacos.
    Atributos:
        saco (Saco): Saco que contiene el nodo.
        siguiente (NodoSaco): Referencia al siguiente nodo en la pila.
    """
    def __init__(self, saco):
        self.saco = saco
        self.siguiente = None


class PilaSacos:
    """
    Clase que representa una pila de sacos.
    Atributos:
        tope (NodoSaco): Referencia al nodo en la parte superior de la pila.
    """
    def __init__(self):
        """
        Inicializa una nueva pila de sacos.
        """
        self.tope = None

    def apilar_saco(self, producto, peso):
        """
        Agrega un nuevo saco a la pila.
        Args:
            producto (str): _nombre_ del producto.
            peso (str): peso del producto en kilogramos.

        Returns:
            Saco: el saco
        """
        hora = self._obtener_hora_actual()
        nuevo_saco = Saco(producto, peso, hora)
        nuevo_nodo = NodoSaco(nuevo_saco)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        return nuevo_saco

    def desapilar_saco(self):
        """
        Elimina el saco en la parte superior de la pila y lo devuelve.
        Returns:
            _Saco: el saco eliminado o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        saco_descargado = self.tope.saco
        self.tope = self.tope.siguiente
        return saco_descargado

    def ver_tope(self):
        """
        Devuelve el saco en la parte superior de la pila sin eliminarlo.
        Returns:
            NodoSaco: el saco en la parte superior de la pila o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        return self.tope.saco

    def mostrar_sacos(self):
        """
        Muestra todos los sacos en la pila.
        Returns:
            array: una lista de sacos en la pila.
        """
        sacos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            sacos.append(nodo_actual.saco)
            nodo_actual = nodo_actual.siguiente
        return sacos

    def _obtener_hora_actual(self):
        """
        Obtiene la hora actual en formato HH:MM:SS.
        Returns:
            str: la hora actual en formato HH:MM:SS.
        """
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")