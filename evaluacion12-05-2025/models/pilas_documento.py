class Documento:
    def __init__(self, nombre, tipo, fecha, solicitante):
        self.nombre = nombre
        self.tipo = tipo
        self.fecha = fecha
        self.solicitante = solicitante

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Sol: {self.solicitante} - {self.fecha}"


class PilaDocumentos:
    def __init__(self):
        self.tope = None

    def agregar_documento(self, documento):
        nuevo_nodo = Nodo(documento)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def revisar_ultimo_documento(self):
        if self.tope is None:
            return None
        documento = self.tope.dato
        self.tope = self.tope.siguiente
        return documento

    def ver_ultimo_pendiente(self):
        if self.tope is None:
            return None
        return self.tope.dato

    def mostrar_pendientes(self):
        documentos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            documentos.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return documentos

    def documentos_pendientes(self):
        return self.tope is not None


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None