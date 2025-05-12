"""
archivo: pila_hospital.py
Este módulo contiene la implementación de una pila de donantes de sangre.
"""

class Donante:
    """Clase Donante que representa un donante de sangre que seria el dato a ser guardado en el nodo"""
    def __init__(self, nombre, cedula, tipo_sangre, hora_registro):
        self.nombre = nombre
        self.cedula = cedula
        self.tipo_sangre = tipo_sangre
        self.hora_registro = hora_registro

    def __str__(self):
        return (f"{self.nombre} (C.I. {self.cedula}) - "
                f"Tipo: {self.tipo_sangre} - "
                f"Registrado: {self.hora_registro}")


class NodoDonante:
    """Clase NodoDonante que representa un nodo en la pila de donantes"""
    def __init__(self, donante):
        self.donante = donante
        self.siguiente = None


class PilaDonantes:
    """Clase PilaDonantes que representa una pila de donantes de sangre"""
    def __init__(self):
        self.tope = None

    def registrar_donante(self, nombre, cedula, tipo_sangre):
        """
        Registra un nuevo donante en la pila.
        :param nombre: nombre del donante
        :param cedula: numero de cedula del donante
        :param tipo_sangre: el tipo de sangre de el donante
        :return: un objeto Donante que representa al donante registrado
        """
        hora = self._obtener_hora_actual()
        nuevo_donante = Donante(nombre, cedula, tipo_sangre, hora)
        nuevo_nodo = NodoDonante(nuevo_donante)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        return nuevo_donante

    def revertir_ultimo(self):
        """
        Revertir el último donante registrado en la pila.
        :return: el último donante registrado o None si la pila está vacía
        """
        if self.tope is None:
            return None
        donante_revertido = self.tope.donante
        self.tope = self.tope.siguiente
        return donante_revertido

    def ver_actual(self):
        """
        Ver el donante en la parte superior de la pila sin eliminarlo.
        :return: el donante en la parte superior de la pila o None si la pila está vacía
        """
        if self.tope is None:
            return None
        return self.tope.donante

    def mostrar_donantes(self):
        """
        Mostrar todos los donantes registrados en la pila.
        :return: una lista de objetos Donante que representan a todos los donantes registrados
        """
        donantes = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            donantes.append(nodo_actual.donante)
            nodo_actual = nodo_actual.siguiente
        return donantes

    def _obtener_hora_actual(self):
        """
        Obtener la hora actual en formato HH:MM:SS.
        :return: la hora actual como una cadena en formato HH:MM:SS
        """
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")