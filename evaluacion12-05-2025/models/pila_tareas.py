"""
archivo: pila_tareas.py
Este módulo contiene la implementación de una pila de trabajos a entregar.
"""

class Tarea:
    """
    Clase que representa una tarea a entregar.
    Atributos:
        estudiante (str): Nombre del estudiante.
        grado (int): Grado del estudiante.
        materia (str): Materia de la tarea.
        fecha_entrega (str): Fecha de entrega de la tarea.
    """
    def __init__(self, estudiante, grado, materia, fecha_entrega):
        self.estudiante = estudiante
        self.grado = grado
        self.materia = materia
        self.fecha_entrega = fecha_entrega

    def __str__(self):
        return (f"{self.estudiante} ({self.grado}°) - "
                f"{self.materia} - "
                f"Entregado: {self.fecha_entrega}")


class NodoTarea:
    """
    Clase que representa un nodo en la pila de tareas.  
    Atributos:
        tarea (Tarea): Tarea que contiene el nodo.
        siguiente (NodoTarea): Referencia al siguiente nodo en la pila.
    """
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None


class PilaTareas:
    """
    Clase que representa una pila de tareas.
    Atributos:
        tope (NodoTarea): Referencia al nodo en la parte superior de la pila.
    """
    def __init__(self):
        self.tope = None

    def agregar_tarea(self, estudiante, grado, materia):
        """
        Agrega una nueva tarea a la pila.

        Args:
            estudiante (str): _nombre_ del estudiante.
            grado (str): _grado_ del estudiante.
            materia (str): _materia_ de la tarea.

        Returns:
            Tarea: la tarea
        """
        fecha = self._obtener_fecha_actual()
        nueva_tarea = Tarea(estudiante, grado, materia, fecha)
        nuevo_nodo = NodoTarea(nueva_tarea)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        return nueva_tarea

    def revisar_tarea(self):
        """
        Revisa la tarea en la parte superior de la pila y la elimina.

        Returns:
            Tarea: tarea eliminada o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        tarea_revisada = self.tope.tarea
        self.tope = self.tope.siguiente
        return tarea_revisada

    def ver_proxima(self):
        """
        Ver la tarea en la parte superior de la pila sin eliminarla.
        Returns:
            Nodo: tarea en la parte superior de la pila o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        return self.tope.tarea

    def mostrar_tareas(self):
        """
        Muestra todas las tareas en la pila.
        Returns:
            array: lista de tareas en la pila.
        """
        tareas = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            tareas.append(nodo_actual.tarea)
            nodo_actual = nodo_actual.siguiente
        return tareas

    def _obtener_fecha_actual(self):
        """
        Obtiene la fecha y hora actual en formato "dd/mm/yyyy hh:mm".
        Returns:
            str: fecha y hora actual.
        """
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M")