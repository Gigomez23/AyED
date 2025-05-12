class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        if self.tope is None:
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def cima(self):
        if self.tope is None:
            return None
        return self.tope.dato

    def imprimir(self):
        if self.tope is None:
            print("La pila está vacía")
            return
        else:
            print("Contenido de la pila:")
            nodo_actual = self.tope
            while nodo_actual is not None:
                print(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente

class PilaDocumentos(Pila):
    def __init__(self):
        super().__init__()

    def agregar_documento(self, documento):
        """Agrega un nuevo documento a la pila de revisión"""
        self.push(documento)

    def revisar_ultimo_documento(self):
        """Revisa y remueve el último documento agregado (el que está en el tope)"""
        return self.pop()

    def ver_ultimo_pendiente(self):
        """Muestra el último documento pendiente por revisar (sin removerlo)"""
        return self.cima()

    def mostrar_pendientes(self):
        """Muestra todos los documentos pendientes de revisión"""
        if self.tope is None:
            print("No hay documentos pendientes de revisión")
            return

        print("\nDocumentos pendientes de revisión (el último agregado aparece primero):")
        nodo_actual = self.tope
        posicion = 1
        while nodo_actual is not None:
            print(f"{posicion}. {nodo_actual.dato}")
            nodo_actual = nodo_actual.siguiente
            posicion += 1

    def documentos_pendientes(self):
        """Devuelve True si hay documentos pendientes, False si no"""
        return self.tope is not None