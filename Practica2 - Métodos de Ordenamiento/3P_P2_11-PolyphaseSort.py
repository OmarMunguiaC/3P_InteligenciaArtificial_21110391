
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
El Polyphase Sort es un algoritmo de ordenamiento externo diseñado para ordenar grandes cantidades de datos cuando estos no caben en memoria principal. 
Utiliza un enfoque de fusión basado en fases para dividir y ordenar las secuencias de datos en múltiples fases hasta que todos los datos estén ordenados.
Consiste en varias partes: Las 'Fases' representan las iteraciones de ordenamiento. Los 'Bloques' son las secuencias de datos que se ordenan en cada fase
Utiliza un 'heap mínimo' para mantener los elementos de los bloques en el orden de fusión.
Cada elemento en el heap es una tupla que contiene el valor del elemento, el índice del bloque de origen y el índice del elemento dentro de ese bloque
Inicialmente, se inserta en el heap el primer elemento de cada bloque.
En cada iteración, se extrae el elemento más pequeño del heap (el menor elemento entre todos los elementos actuales de los bloques) y se agrega a la lista fusionada.
Se inserta en el heap el siguiente elemento del bloque de donde provino el elemento extraído.

Proceso: 
1) Inicialización del Heap: Inicia el heap con el primer elemento de cada bloque junto con su índice.
2) Fusión Iterativa: Extrae y fusiona el elemento más pequeño del heap hasta que todos los bloques se hayan fusionado en una sola lista ordenada.
3) Finalización: La lista resultante contiene todos los elementos ordenados de los bloques originales.

Caracteristicas:
* Complejidad: es útil cuando se deben ordenar grandes volúmenes de datos de manera eficiente y cuando estos datos no caben en la memoria principal. 
    Ofrece una forma escalable de ordenar datos utilizando un enfoque de ordenamiento externo basado en fases.
* Espacio: Polyphase Sort utiliza espacio adicional para mantener el heap de tamaño 'k' y la lista final.
* Estabilidad: El algoritmo es estable, ya que preserva el orden relativo de los elementos con valores iguales.
"""

import heapq

def polyphase_sort(blocks):

    # Inicializar el heap min para manejar la fusión de los bloques
    min_heap = []
    
    # Inicializar el heap min con el primer elemento de cada bloque junto con el índice del bloque
    for i, block in enumerate(blocks):
        if block:  # Asegurarse de que el bloque no esté vacío
            heapq.heappush(min_heap, (block[0], i, 0))  # (valor, índice de bloque, índice de elemento)
    
    merged_list = []
    
    while min_heap:
        # Obtener el elemento más pequeño del heap min
        val, block_idx, element_idx = heapq.heappop(min_heap)
        
        # Agregar el elemento a la lista fusionada
        merged_list.append(val)
        
        # Mover al siguiente elemento en el bloque correspondiente
        if element_idx + 1 < len(blocks[block_idx]):
            next_tuple = (blocks[block_idx][element_idx + 1], block_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list


if __name__ == "__main__":
    # Definimos varios bloques de elementos desordenados
    bloque1 = [1, 5, 8, 10]
    bloque2 = [2, 4, 6, 7]
    bloque3 = [3, 9, 11]
    
    # Mostramos los bloques antes de la ordenación
    print("Bloque 1:", bloque1)
    print("Bloque 2:", bloque2)
    print("Bloque 3:", bloque3)
    
    # Llamamos a la función de ordenamiento
    bloques_ordenados = polyphase_sort([bloque1, bloque2, bloque3])
    
    # Mostramos los bloques ordenados después del proceso
    print("Bloques ordenados:", bloques_ordenados)
