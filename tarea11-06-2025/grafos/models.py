import collections

class Grafo:
    def __init__(self, es_dirigido=False):
        self.grafo = {}
        self.es_dirigido = es_dirigido
        
    def agregar_vertice(self, vertice):
        """Si el vertice no esta en el diccionario, lo añade con un conjunto vacío de vecinos.

        Args:
            vertice: el vertice a agregar al grafo.
        """
        if vertice not in self.grafo:
            self.grafo[vertice] = set()
            print(f"Vértice '{vertice}' agregado al grafo.")
        else:
            print(f"El vértice '{vertice}' ya existe en el grafo.")
            
    def agregar_arista(self, u, v, peso=1):
        # asegurarse de que ambos vertices existen en el grafo
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        #añadir el/la arista
        self.grafo[u].add(v)
        print(f"Arista  {u} -> {v} agregada.")
        
        # Si no es dirigido, añadir la arista en la dirección opuesta también
        if not self.es_dirigido:
            self.grafo[v].add(u)
            print(f"Arista {v} -> {u} (bidireccional) agregada.")
            
    def obtener_vecinos(self, vertice):
        """Devuelve los vecinos del vértice dado.

        Args:
            vertice: el vértice del cual se quieren obtener los vecinos.

        Returns:
            Un conjunto de vecinos del vértice.
        """
        if vertice in self.grafo:
            return list(self.grafo[vertice]) #Convertir a lista para devolver
        return [] # Si el vértice no existe, no tiene vecinos.
    
    def existe_arista(self, u, v):
        # Verifica si ambos vértices existen y si 'v' esta en la lista de adyencia de 'u'
        return u in self.grafo and v in self.grafo[u]
    
    def bfs(self, inicio):
        visitados = set() #Conjunto para guardar los vértices ya visitados
        cola = collections.deque() # Cola para los vertices a visitar
        
        #Empezar el recorrido desde el vértice inicial
        cola.append(inicio)
        visitados.add(inicio)
        
        recorrido = [] # Lista para almacenar el orden de visita
        
        while cola:
            vertice_actual = cola.popleft() # Sacar el primer elemento de la cola
            recorrido.append(vertice_actual)
            print(f"Visitando: {vertice_actual}")
            
            # Añadir a la cola los vecinos no visitados
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return recorrido
    
    def dfs(self, inicio):
        visitados = set()
        recorrido = []
        
        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            recorrido.append(vertice)
            print(f"Visitando: {vertice}")
            
            for vecino in self.obtener_vecinos(vertice):
                if vecino not in visitados:
                    _dfs_recursivo(vecino)
        
        _dfs_recursivo(inicio)
        return recorrido
    
    def imprimir_grafo(self):
        """Imprime el grafo en formato de lista de adyacencia."""
        for vertice, vecinos in self.grafo.items():
            print(f"{vertice}: {', '.join(vecinos)}")
        print("-----------------------------------")
        
    def es_conexo(self):
        if not self.grafo:
            return True
        
        #tomar el primer vértice para iniciar el BFS/DFS
        primer_vertice = next(iter(self.grafo))
        
        # realizar un BFS desde el primer vértice
        recorrido_bfs = self.bfs(primer_vertice)
        
    def encontrar_camino(self, inicio, fin):
        """Encuentra un camino entre dos vértices usando DFS.

        Args:
            inicio: el vértice de inicio.
            fin: el vértice de destino.

        Returns:
            Una lista con el camino encontrado o None si no hay camino.
        """
        if inicio not in self.grafo or fin not in self.grafo:
            print(f"Error: '{inicio}' o '{fin}' no existen en el grafo. ")
            return []
        
        cola = collections.deque()
        visitados = set()
        padres = {}
        
        cola.append(inicio)
        vistados = set()
        padres = {}
        
        cola.append(inicio)
        visitados.add(inicio)
        padres[inicio] = None # El inicio no tiene padres
        
        while cola:
            vertice_actual = cola.popleft()
            
            if vertice_actual == fin:
                # Hemos llegado al destino, reconstruir el camino
                camino = []
                temp = fin
                while temp is not None:
                    camino.append(temp)
                    temp = padres[temp]
                return camino[::-1] # Invertir el camino para que vaya de inicio a fin
            
            for vecino in self.obtener_vecinos(vertice_actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = vertice_actual #Guardar el padre
                    cola.append(vecino)
        
        return [] # No se encontró un camino
    
            