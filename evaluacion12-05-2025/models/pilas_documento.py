"""
archivo: pila_documento.py
Este módulo contiene la implementación de una pila de documentos.
"""

class Documento:
    """
    Clase Documento que representa un documento con su nombre, tipo, fecha y solicitante.
    Atributos:
        nombre (str): Nombre del documento.
        tipo (str): Tipo de documento.
        fecha (str): Fecha de creación o revisión del documento.
        solicitante (str): Nombre del solicitante del documento.
    """
    def __init__(self, nombre, tipo, fecha, solicitante):
        self.nombre = nombre
        self.tipo = tipo
        self.fecha = fecha
        self.solicitante = solicitante

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Sol: {self.solicitante} - {self.fecha}"


class PilaDocumentos:
    """
    Clase que representa una pila de documentos.
    Atributos:
        tope (Nodo): Referencia al nodo en la parte superior de la pila.
    """
    def __init__(self):
        self.tope = None

    def agregar_documento(self, documento):
        """
        Agrega un nuevo documento a la pila.    
        Args:
            documento (Documento): _Instancia_ de la clase Documento.
        """
        nuevo_nodo = Nodo(documento)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def revisar_ultimo_documento(self):
        """
        Revisa el documento en la parte superior de la pila y lo elimina.
        Returns:
            Documento: el documento eliminado o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        documento = self.tope.dato
        self.tope = self.tope.siguiente
        return documento

    def ver_ultimo_pendiente(self):
        """
        Devuelve el documento en la parte superior de la pila sin eliminarlo.
        Returns:
            array: el documento en la parte superior o None si la pila está vacía.
        """
        if self.tope is None:
            return None
        return self.tope.dato

    def mostrar_pendientes(self):
        """
        Muestra todos los documentos pendientes en la pila.
        Returns:
            array: lista de documentos pendientes.
        """
        documentos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            documentos.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return documentos

    def documentos_pendientes(self):
        """
        Verifica si hay documentos pendientes en la pila.
        Returns:
            tope: True si hay documentos pendientes, False en caso contrario.
        """
        return self.tope is not None


class Nodo:
    """
    Clase Nodo que representa un nodo en la pila de documentos.
    Atributos:
        dato (Documento): Documento almacenado en el nodo.
        siguiente (Nodo): Referencia al siguiente nodo en la pila.
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None