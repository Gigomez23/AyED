class Pan:
    def __init__(self, tipo, hora_horneado):
        self.tipo = tipo
        self.hora_horneado = hora_horneado

    def __str__(self):
        return f"{self.tipo} (Horneado: {self.hora_horneado})"


class NodoPan:
    def __init__(self, pan):
        self.pan = pan
        self.siguiente = None


class PilaPanes:
    def __init__(self):
        self.tope = None

    def agregar_pan(self, tipo):
        hora_actual = self._obtener_hora_actual()
        nuevo_pan = Pan(tipo, hora_actual)
        nuevo_nodo = NodoPan(nuevo_pan)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        return nuevo_pan

    def vender_pan(self):
        if self.tope is None:
            return None
        pan_vendido = self.tope.pan
        self.tope = self.tope.siguiente
        return pan_vendido

    def ver_proximo(self):
        if self.tope is None:
            return None
        return self.tope.pan

    def mostrar_panes(self):
        panes = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            panes.append(nodo_actual.pan)
            nodo_actual = nodo_actual.siguiente
        return panes

    def _obtener_hora_actual(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")