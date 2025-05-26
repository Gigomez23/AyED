import heapq

class Elemento:
    """
    Clase que representa un elemento en la cola de prioridad.
    Cada elemento tiene un nombre y una prioridad (número entero).
    Menor número indica mayor prioridad.
    """

    def __init__(self, nombre: str, prioridad: int):
        """
        Inicializa un nuevo elemento con nombre y prioridad.

        Args:
            nombre (str): Nombre del elemento
            prioridad (int): Prioridad del elemento (menor número = mayor prioridad)
        """
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, otro):
        """Compara si este elemento tiene mayor prioridad que otro."""
        return self.prioridad < otro.prioridad

    def __eq__(self, otro):
        """Compara si dos elementos tienen la misma prioridad."""
        return self.prioridad == otro.prioridad

    def __str__(self):
        """Representación en string del elemento."""
        return f"{self.nombre} (Prioridad: {self.prioridad})"


class ColaPrioridad:
    """
    Implementación de una cola de prioridad usando un min-heap.
    Los elementos se desencolan según su prioridad (menor número primero).
    """

    def __init__(self):
        """Inicializa una cola de prioridad vacía."""
        self._cola = []
        self._indice = 0  # Para manejar empates en prioridad

    def encolar(self, elemento: Elemento):
        """
        Añade un nuevo elemento a la cola de prioridad.

        Args:
            elemento (Elemento): Elemento a añadir a la cola
        """
        # Usamos el índice para mantener el orden de llegada cuando hay empates
        heapq.heappush(self._cola, (elemento.prioridad, self._indice, elemento))
        self._indice += 1

    def desencolar(self) -> Elemento:
        """
        Remueve y devuelve el elemento con mayor prioridad (menor número).

        Returns:
            Elemento: El elemento con mayor prioridad

        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            raise IndexError("La cola de prioridad está vacía")
        return heapq.heappop(self._cola)[2]  # [2] es el elemento

    def esta_vacia(self) -> bool:
        """Verifica si la cola está vacía."""
        return len(self._cola) == 0

    def __len__(self) -> int:
        """Devuelve el número de elementos en la cola."""
        return len(self._cola)

    def __str__(self) -> str:
        """Representación en string de la cola de prioridad."""
        elementos_ordenados = sorted([(prioridad, idx, elemento) for prioridad, idx, elemento in self._cola])
        return "Cola de Prioridad:\n" + "\n".join([str(elemento) for _, _, elemento in elementos_ordenados])

