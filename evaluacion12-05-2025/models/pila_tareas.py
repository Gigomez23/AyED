class Tarea:
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
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None


class PilaTareas:
    def __init__(self):
        self.tope = None

    def agregar_tarea(self, estudiante, grado, materia):
        fecha = self._obtener_fecha_actual()
        nueva_tarea = Tarea(estudiante, grado, materia, fecha)
        nuevo_nodo = NodoTarea(nueva_tarea)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        return nueva_tarea

    def revisar_tarea(self):
        if self.tope is None:
            return None
        tarea_revisada = self.tope.tarea
        self.tope = self.tope.siguiente
        return tarea_revisada

    def ver_proxima(self):
        if self.tope is None:
            return None
        return self.tope.tarea

    def mostrar_tareas(self):
        tareas = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            tareas.append(nodo_actual.tarea)
            nodo_actual = nodo_actual.siguiente
        return tareas

    def _obtener_fecha_actual(self):
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M")