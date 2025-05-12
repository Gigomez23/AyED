"""
archivo: pilas_pan.py
Este módulo contiene la implementación de una pila de panes.
"""

class Pan:
    """
    Clase que representa un pan.
    Atributos:
        tipo (str): Tipo de pan.
        hora_horneado (str): Hora de horneado del pan en formato HH:MM:SS.
    """
    def __init__(self, tipo, hora_horneado):
        self.tipo = tipo
        self.hora_horneado = hora_horneado

    def __str__(self):
        return f"{self.tipo} (Horneado: {self.hora_horneado})"


class NodoPan:
    """
    Clase que representa un nodo en la pila de panes.
    Atributos:
        pan (Pan): Pan que contiene el nodo.
        siguiente (NodoPan): Referencia al siguiente nodo en la pila.
    """
    def __init__(self, pan):
        self.pan = pan
        self.siguiente = None


class PilaPanes:
    """
    Clase que representa una pila de panes.
    Atributos:
        tope (NodoPan): Referencia al nodo en la parte superior de la pila.
    """
    def __init__(self):
        self.tope = None

    def agregar_pan(self, tipo):
        """
        Agrega un nuevo pan a la pila.
        Args:
            tipo (str): string de pan a agregar.

        Returns:
            str: el pan agregado
        """
        hora_actual = self._obtener_hora_actual()
        nuevo_pan = Pan(tipo, hora_actual)
        nuevo_nodo = NodoPan(nuevo_pan)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        return nuevo_pan

    def vender_pan(self):
        """
        Vende el pan en la parte superior de la pila y lo elimina.
        Returns:
            str: el pan vendido o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        pan_vendido = self.tope.pan
        self.tope = self.tope.siguiente
        return pan_vendido

    def ver_proximo(self):
        """
        Devuelve el pan en la parte superior de la pila sin eliminarlo.

        Returns:
            str: el pan en la parte superior o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        return self.tope.pan

    def mostrar_panes(self):
        """
        Muestra todos los panes en la pila.
        Returns:
            array: lista de panes en la pila.
        """
        panes = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            panes.append(nodo_actual.pan)
            nodo_actual = nodo_actual.siguiente
        return panes

    def _obtener_hora_actual(self):
        """
        Obtiene la hora actual en formato HH:MM:SS.
        Returns:
            str: la hora actual en formato HH:MM:SS.
        """
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")