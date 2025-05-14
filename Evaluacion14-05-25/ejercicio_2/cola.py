class Documento:
    """
    Representa un documento para imprimir.
    """
    def __init__(self, nombre: str, usuario: str, num_paginas: int):
        self.nombre = nombre
        self.usuario = usuario
        self.num_paginas = num_paginas

    def __str__(self):
        return f"Documento: {self.nombre}, Usuario: {self.usuario}, Páginas: {self.num_paginas}"


class ColaImpresion:
    """
    Simula una cola de impresión donde se agregan documentos y se procesan en orden FIFO.
    """
    def __init__(self):
        self.cola = []

    def agregar_documento(self, documento: Documento):
        """
        Agrega un documento a la cola de impresión.
        """
        self.cola.append(documento)
        print(f"Documento agregado a la cola: {documento}")

    def procesar_siguiente(self):
        """
        Procesa (imprime) el siguiente documento en la cola.
        Retorna el documento procesado o None si la cola está vacía.
        """
        if self.cola:
            documento_actual = self.cola.pop(0)
            print(f"Imprimiendo documento: {documento_actual}")
            return documento_actual
        else:
            print("No hay documentos en la cola para imprimir.")
            return None

    def documento_actual(self):
        """
        Muestra el documento que se está imprimiendo actualmente (el primero en la cola).
        """
        if self.cola:
            return self.cola[0]
        else:
            return None


''' En esta simulación, la cola de impresión funciona como una estructura FIFO (First In, First Out),
lo que significa que los documentos se imprimen en el orden en que fueron agregados.
Esto evita que varios usuarios impriman al mismo tiempo o que un documento se imprima antes que otro
que llegó primero, previniendo el desorden y conflictos en el uso de la impresora.
'''