
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

import heapq  # Importamos la biblioteca heapq para manejar la cola de prioridad

# Función que implementa el Algoritmo de Dijkstra
def dijkstra(graph, start):
    # Inicializamos la distancia de todos los nodos al infinito
    distances = {node: float('inf') for node in graph}
    # La distancia al nodo inicial es 0
    distances[start] = 0
    # Utilizamos una cola de prioridad para manejar los nodos a visitar
    priority_queue = [(0, start)]
    # Mantenemos un registro de los nodos visitados
    visited = set()
    # Registro de caminos
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        # Extraemos el nodo con la menor distancia acumulada
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue

        print(f"\nVisitando nodo {current_node} con distancia acumulada {current_distance}")
        
        # Marcamos el nodo como visitado
        visited.add(current_node)
        
        # Exploramos los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Solo consideramos este camino si es más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                previous_nodes[neighbor] = current_node
                print(f"Actualizando distancia del nodo {neighbor} a {distance}")
        
        # Imprimimos el estado actual del grafo con flechas
        print_graph_with_arrows(graph, previous_nodes, distances)
    
    return distances

def print_graph_with_arrows(graph, previous_nodes, distances):
    print("\nEstado del grafo:")
    for node in graph:
        for neighbor, weight in graph[node].items():
            direction = "->"
            if previous_nodes[neighbor] == node:
                direction = "=>"
            print(f"{node} {direction} {neighbor} (peso {weight})")
    print("Distancias actuales:", distances)
    print("Caminos anteriores:", previous_nodes)

# Definimos el grafo como un diccionario de diccionarios
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Nodo de inicio
start_node = 'A'

# Llamamos a la función y obtenemos las distancias
distances = dijkstra(graph, start_node)

# Imprimimos el resultado final
print("\nDistancias finales desde el nodo de inicio:")
for node, distance in distances.items():
    print(f"Distancia a {node}: {distance}")
