
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

class UnionFind:
    def __init__(self, n):
        # Inicialización de la estructura Union-Find con n nodos
        self.parent = list(range(n))  # Inicialmente cada nodo es su propio padre
        self.rank = [1] * n  # Inicialmente cada conjunto tiene rango 1
    
    def find(self, u):
        # Función para encontrar el representante del conjunto de u (con compresión de camino)
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compresión de camino
        return self.parent[u]
    
    def union(self, u, v):
        # Función para unir los conjuntos de u y v
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union por rango
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True  # Se realizó la unión
        return False  # No se realizó la unión porque u y v ya estaban en el mismo conjunto

def kruskal(graph, n, min_cost=True):
    # Función principal de Kruskal para encontrar el MST o árbol de máximo coste
    if min_cost:
        graph.sort()  # Ordenar las aristas por peso (ascendente)
    else:
        graph.sort(reverse=True)  # Ordenar las aristas por peso (descendente)
    
    uf = UnionFind(n)  # Inicializar la estructura Union-Find con n nodos
    mst = []  # Lista para almacenar las aristas del MST
    total_cost = 0  # Costo total del MST
    
    for weight, u, v in graph:
        if uf.union(u, v):
            # Si unir u y v no forma un ciclo, se añade la arista al MST
            mst.append((weight, u, v))
            total_cost += weight
            
            # Imprimir el paso actual para mostrar qué arista se añadió al MST
            print(f"Agregada arista: ({u}, {v}) con peso {weight}. Costo total: {total_cost}\n")
            print(f"MST parcial:", mst, "\n")
        else:
            # Si unir u y v forma un ciclo, se ignora esa arista
            print(f"Ignorada arista: ({u}, {v}) con peso {weight}. Costo total: {total_cost}\n")
            print(f"MST actual:", mst, "\n")
    
    return mst, total_cost

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de grafo: (peso, nodo1, nodo2)
    graph = [
        (1, 0, 1),
        (2, 0, 2),
        (4, 1, 2),
        (3, 1, 3),
        (5, 2, 3),
        (6, 3, 4)
    ]
    
    num_nodos = 5  # Suponiendo que los nodos están etiquetados del 0 al 4
    
    print("Encontrando el Árbol de Mínimo Coste usando el algoritmo de Kruskal:\n")
    mst, costo_minimo = kruskal(graph, num_nodos, min_cost=True)
    print("\nÁrbol de Mínimo Coste:", mst)
    print("Costo total mínimo:", costo_minimo)
