"""
models.py

Este archivo contiene las clases y sus respectivos metodos y atributos para el editor de texto.

Clases:
    Nodo: Representa un nodo en la lista doblemente enlazada, que contiene una acción y referencias a los nodos anterior y siguiente.
    Accion: Representa una acción realizada en el editor de texto, como insertar, borrar, copiar o pegar texto.
    EditorTexto: Implementa las funcionalidades del editor de texto, incluyendo la gestión del historial de acciones y el portapapeles.

"""

class Nodo:
    """
    Clase que representa un nodo en una lista doblemente enlazada.
    
    Atributos:
        accion: La acción asociada a este nodo.
        anterior: Referencia al nodo anterior en la lista.
        siguiente: Referencia al nodo siguiente en la lista.
    """
    
    def __init__(self, accion, anterior=None, siguiente=None):
        self.accion = accion
        self.anterior = anterior
        self.siguiente = siguiente


class Accion:
    """
    Clase que representa una acción realizada en el editor de texto.
    
    Atributos:
        tipo: Tipo de acción (insertar, borrar, copiar, pegar).
        texto_afectado: Texto que fue afectado por la acción.
        posicion: Posición en el texto donde ocurrió la acción.
        texto_clipboard: Texto copiado al portapapeles (si aplica).
    """
    
    def __init__(self, tipo, texto_afectado, posicion, texto_clipboard=""):
        """funcion que inicializa la clase Accion

        Args:
            tipo (string): tipo de accion
            texto_afectado (string): el texto afectado por la accion
            posicion (int): posicion donde se realizo la accion
            texto_clipboard (str, optional): En caso de copiar aqui se guarda el texto. En caso de que no se utilize su valor default es "".
        """
        self.tipo = tipo    # Guarda el tipo de acción (insertar, borrar, copiar, pegar)
        self.texto_afectado = texto_afectado  # Guarda el texto que fue afectado en la acción
        self.posicion = posicion  # Guarda la posición en el texto donde ocurrió la acción
        self.texto_clipboard = texto_clipboard  # Y este guarda el texto copiado en el portapapeles

    def __str__(self):
        """Aqui se define como se muestra la accion como texto

        * Si la accion es copiar, muestra que el texto fue guardado en portapapeles
        * Si la accion es copiar, pegar o borrar, se muestra el texto afectado y su posicion

        Returns:
            string: descripcion de la accion y su texto afectado
        """
        if self.tipo == 'copiar':
            return f"{self.tipo} '{self.texto_afectado}' (guardado en portapapeles)"
        return f"{self.tipo} '{self.texto_afectado}' en posición {self.posicion}"


class EditorTexto:
    """
    Aqui es donde se emplean las funciones del editor de texto básico con historial de acciones utilizando una lista doblemente enlazada.
    Permite realizar operaciones de insertar, copiar, pegar y borrar texto, manteniendo registro de cada acción
    para poder deshacer y rehacer cambios. También maneja un portapapeles interno para las operaciones de copiar y pegar.
    Además, ofrece funciones para visualizar el estado actual del texto y el historial completo de ediciones realizadas.
    
    Atributos:
        cabeza: Referencia al nodo más reciente (cabeza) de la lista de acciones.
        cola: Referencia al nodo más antiguo (cola) de la lista de acciones.
        actual: Referencia al nodo actual en la lista de acciones.
        texto: Texto actual del editor.
        portapapeles: Texto almacenado en el portapapeles.
        texto_actual: Texto afectado por la última acción realizada.
        
    Métodos:
        agegar_accion: Agrega una nueva acción al historial y aplica la acción al texto.
        deshacer: Deshace la última acción realizada.
        rehacer: Rehace la última acción deshecha.
        mostrar_estado: Muestra el estado actual del texto y el portapapeles, así como el historial de acciones.
        aplicar_accion: Aplica una acción al texto actual.
        revertir_accion: Revierte una acción aplicada al texto.
    """

    def __init__(self):
        """Inicializa el editor de texto con una lista doblemente enlazada para el historial de acciones.
        """
        self.cabeza = None
        self.cola = None
        self.actual = None
        self.texto = ""
        self.portapapeles = ""
        self.texto_actual = ""  # <--- (lo que me tarde corrigiendo esta vaina) nueva variable para el último texto afectado

    def agregar_accion(self, tipo, texto_afectado, posicion, texto_clipboard=""):
        """Agrega una nueva acción al historial y aplica la acción al texto.

        Args:
            tipo (string): tipo de accion
            texto_afectado (string): el texto afectado por la accion
            posicion (int): posicion donde se realizo la accion
            texto_clipboard (str, optional): En caso de copiar aqui se guarda el texto. En caso de que no se utilize su valor default es "".
        """
        nueva_accion = Accion(tipo, texto_afectado, posicion, texto_clipboard)
        nuevo_nodo = Nodo(nueva_accion, anterior=self.cabeza)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cabeza.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo

        self.actual = self.cabeza
        self._aplicar_accion(nueva_accion)

        # Actualizamos el texto_actual solo si la acción modifica el contenido
        if tipo in ['insertar', 'pegar']:
            self.texto_actual = texto_afectado

    def _aplicar_accion(self, accion):
        """Aplica la acción al texto actual. Dependiendo del tipo de acción, modifica el texto o el portapapeles.

        Args:
            accion (string): especifica la accion a aplicar
        """
        if accion.tipo == 'insertar':
            self.texto = self.texto[:accion.posicion] + accion.texto_afectado + self.texto[accion.posicion:]
        elif accion.tipo == 'borrar':
            self.texto = self.texto[:accion.posicion] + self.texto[accion.posicion + len(accion.texto_afectado):]
        elif accion.tipo == 'copiar':
            self.portapapeles = accion.texto_afectado
        elif accion.tipo == 'pegar':
            self.texto = self.texto[:accion.posicion] + self.portapapeles + self.texto[accion.posicion:]

    def deshacer(self):
        """Deshace la última acción realizada. Si no hay acciones para deshacer, retorna None.

        Returns:
            string: La acción deshecha o None si no hay acciones para deshacer.
        """
        if self.actual is None:
            return None

        accion = self.actual.accion
        self._revertir_accion(accion)
        self.actual = self.actual.anterior
        return accion

    def _revertir_accion(self, accion):
        """Funcion que revierte la acción aplicada al texto actual.

        Args:
            accion (string): especifica la accion a revertir
        """
        if accion.tipo == 'insertar':
            self.texto = self.texto[:accion.posicion] + self.texto[accion.posicion + len(accion.texto_afectado):]
        elif accion.tipo == 'borrar':
            self.texto = self.texto[:accion.posicion] + accion.texto_afectado + self.texto[accion.posicion:]
        elif accion.tipo == 'pegar':
            self.texto = self.texto[:accion.posicion] + self.texto[accion.posicion + len(self.portapapeles):]

    def rehacer(self):
        """Rehace la última acción deshecha. Si no hay acciones para rehacer, retorna None.

        Returns:
            string: La acción rehecha o None si no hay acciones para rehacer.
        """
        if self.actual is None or self.actual.siguiente is None:
            return None

        self.actual = self.actual.siguiente
        accion = self.actual.accion
        self._aplicar_accion(accion)

        if accion.tipo in ['insertar', 'pegar']:
            self.texto_actual = accion.texto_afectado

        return accion

    def mostrar_estado(self):
        """Muestra el estado actual del texto y el portapapeles, así como el historial de acciones.
        """
        print(f"\nTexto actual: '{self.texto_actual}'")  # se muestra SOLO el último afectado
        print(f"Clipboard: '{self.portapapeles}'")
        print("\nHistorial de acciones:")

        nodo = self.cola
        while nodo is not None:
            prefix = "-> " if nodo == self.actual else "   "
            print(f"{prefix}{nodo.accion}")
            nodo = nodo.siguiente