
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

import heapq

def prim(graph, start_node):

    # Lista de aristas en el MST
    mst = []

    # Conjunto de nodos visitados
    visited = set()

    # Cola de prioridad (min-heap) para seleccionar la arista con el menor peso
    min_heap = [(0, start_node, None)]  # (peso, nodo_actual, nodo_previo)

    while min_heap:
        # Extraemos la arista con el menor peso
        weight, current_node, previous_node = heapq.heappop(min_heap)

        if current_node not in visited:
            # Añadimos el nodo actual al conjunto de visitados
            visited.add(current_node)

            # Si previous_node no es None, agregamos la arista al MST
            if previous_node is not None:
                mst.append((previous_node, current_node, weight))
                print(f"Arista añadida al MST: {previous_node} --({weight})--> {current_node}")

            # Recorremos las aristas adyacentes del nodo actual
            for neighbor, edge_weight in graph[current_node]:
                if neighbor not in visited:
                    # Añadimos la arista a la cola de prioridad
                    heapq.heappush(min_heap, (edge_weight, neighbor, current_node))
                    print(f"Arista considerada: {current_node} --({edge_weight})--> {neighbor}")

            # Mostrar el estado actual del grafo con flechas
            print_graph_state(graph, visited, mst)

    return mst

def print_graph_state(graph, visited, mst):
    """
    Función para imprimir el estado actual del grafo de forma gráfica.
    :param graph: Grafo representado como un diccionario.
    :param visited: Conjunto de nodos visitados.
    :param mst: Lista de aristas que componen el MST.
    """
    print("\nEstado actual del grafo:")
    for node in graph:
        if node in visited:
            print(f"{node} ->", end=' ')
            for neighbor, weight in graph[node]:
                if neighbor in visited:
                    if (node, neighbor, weight) in mst or (neighbor, node, weight) in mst:
                        print(f"{neighbor}({weight}, MST)", end='  ')
                    else:
                        print(f"{neighbor}({weight})", end='  ')
            print()
        else:
            print(f"{node} ->", end=' ')
            for neighbor, weight in graph[node]:
                print(f"{neighbor}({weight})", end='  ')
            print()

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el grafo como un diccionario
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    # Nodo inicial
    start_node = 'A'

    print(f"Ejecutando el algoritmo de Prim desde el nodo {start_node}\n")
    mst = prim(graph, start_node)

    print("\nÁrbol de Expansión Mínimo (MST) resultante:")
    for edge in mst:
        print(f"{edge[0]} --({edge[2]})--> {edge[1]}")
