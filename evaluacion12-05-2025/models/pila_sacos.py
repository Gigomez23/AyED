class Saco:
    def __init__(self, producto, peso, hora_carga):
        self.producto = producto
        self.peso = peso
        self.hora_carga = hora_carga

    def __str__(self):
        return f"{self.producto} ({self.peso} kg) - Cargado: {self.hora_carga}"


class NodoSaco:
    def __init__(self, saco):
        self.saco = saco
        self.siguiente = None


class PilaSacos:
    def __init__(self):
        self.tope = None

    def apilar_saco(self, producto, peso):
        hora = self._obtener_hora_actual()
        nuevo_saco = Saco(producto, peso, hora)
        nuevo_nodo = NodoSaco(nuevo_saco)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        return nuevo_saco

    def desapilar_saco(self):
        if self.tope is None:
            return None
        saco_descargado = self.tope.saco
        self.tope = self.tope.siguiente
        return saco_descargado

    def ver_tope(self):
        if self.tope is None:
            return None
        return self.tope.saco

    def mostrar_sacos(self):
        sacos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            sacos.append(nodo_actual.saco)
            nodo_actual = nodo_actual.siguiente
        return sacos

    def _obtener_hora_actual(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")