
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
El método de Distribution of Initial Runs es un algoritmo de ordenamiento externo que divide los datos en ejecuciones iniciales (initial runs), 
ordena estas ejecuciones y luego las fusiona para obtener una lista completamente ordenada.
Las initial runs son sublistas de tamaño fijo que se generan a partir de la lista de datos original.
Cada initial run se ordena individualmente utilizando un algoritmo de ordenamiento interno, como 'sort()' en Python.
Una vez generadas y ordenadas las initial runs, se fusionan utilizando un enfoque de fusión basado en heap (heap-based merging).
Se utiliza un heap mínimo para mantener el orden de fusión de los elementos de todas las initial runs.
Se inicializa un heap mínimo con el primer elemento de cada initial run.
En cada iteración, se extrae el elemento más pequeño del heap y se agrega a la lista final ordenada.
Se inserta en el heap el siguiente elemento del initial run de donde provino el elemento extraído, si existe.

Proceso:
1) Generación de Initial Runs: Divide la lista de datos en bloques de tamaño fijo y genera initial runs.
2) Ordenación de Initial Runs: Ordena cada initial run individualmente.
3) Fusión de Initial Runs: Utiliza un heap mínimo para fusionar las initial runs ordenadas en una lista final ordenada.

Caracteristicas:
* Complejidad: Distribution of Initial Runs es útil cuando se deben ordenar grandes volúmenes de datos en sistemas con limitaciones de memoria principal, 
    ya que permite procesar los datos en bloques y fusionarlos eficientemente para obtener una lista completamente ordenada.
* Espacio: Distribution of Initial Runs utiliza espacio adicional para mantener el heap de tamaño 'k' y las initial runs.
* Estabilidad: El algoritmo es estable, ya que preserva el orden relativo de los elementos con valores iguales.
"""

import heapq

def initial_runs_sort(data, block_size):

    n = len(data)
    runs = []
    
    # Generar ejecuciones iniciales
    for i in range(0, n, block_size):
        run = data[i:i + block_size]
        run.sort()
        runs.append(run)
    
    # Fusionar ejecuciones iniciales
    sorted_data = merge_runs(runs)
    
    return sorted_data

def merge_runs(runs):

    min_heap = []
    
    # Inicializar el heap min con el primer elemento de cada ejecución
    for i, run in enumerate(runs):
        if run:  # Asegurarse de que la ejecución no esté vacía
            heapq.heappush(min_heap, (run[0], i, 0))  # (valor, índice de ejecución, índice de elemento)
    
    merged_list = []
    
    while min_heap:
        # Obtener el elemento más pequeño del heap min
        val, run_idx, element_idx = heapq.heappop(min_heap)
        
        # Agregar el elemento a la lista fusionada
        merged_list.append(val)
        
        # Mover al siguiente elemento en la ejecución correspondiente
        if element_idx + 1 < len(runs[run_idx]):
            next_tuple = (runs[run_idx][element_idx + 1], run_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6, 7, 19, 4, 2, 10, 3, 14]
    block_size = 4  # Tamaño del bloque para las ejecuciones iniciales
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = initial_runs_sort(ejemplo_lista, block_size)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
