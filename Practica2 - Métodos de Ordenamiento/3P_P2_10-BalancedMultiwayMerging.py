
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
Balanced Multiway Merging es un algoritmo que se utiliza para fusionar eficientemente múltiples listas ordenadas en una sola lista ordenada. 
Utiliza una estructura de datos de heap (o montículo) mínimo para mantener el orden en el que se deben fusionar los elementos de las listas. 
Utiliza un heap (montículo) mínimo para mantener los elementos de las listas en el orden de fusión.
Cada elemento en el heap es una tupla que contiene el valor del elemento, el índice de la lista de origen y el índice del elemento dentro de esa lista.
Inicialmente, se inserta en el heap el primer elemento de cada lista.
En cada iteración, se extrae el elemento más pequeño del heap (el menor elemento entre todos los elementos actuales de las listas) y se agrega a la lista fusionada.
Se inserta en el heap el siguiente elemento de la lista de donde provino el elemento extraído.

Proceso:
1) Inicialización del Heap: Inicia el heap con el primer elemento de cada lista junto con su índice.
2) Fusión Iterativa: Extrae y fusiona el elemento más pequeño del heap hasta que todas las listas se hayan fusionado en una sola lista ordenada.
3) Finalización: La lista resultante contiene todos los elementos ordenados de las listas originales.

Caracteristicas:
* Complejidad: Balanced Multiway Merging es particularmente útil cuando se deben fusionar muchas listas ordenadas, 
    como en la fusión de archivos grandes o en aplicaciones de bases de datos.
* Espacio: Balanced Multiway Merging utiliza espacio adicional para mantener el heap de tamaño 'k' y la lista final.
* Estabilidad: El algoritmo es estable, ya que preserva el orden relativo de los elementos con valores iguales.
"""

import heapq

def balanced_multiway_merge(lists):

    # Usamos un heap min para mantener el orden en el que vamos a fusionar los elementos
    min_heap = []
    
    # Inicializamos el heap min con el primer elemento de cada lista junto con el índice de la lista
    for i, lst in enumerate(lists):
        if lst:  # Aseguramos que la lista no esté vacía
            heapq.heappush(min_heap, (lst[0], i, 0))  # (valor, índice de lista, índice de elemento)
    
    merged_list = []
    
    while min_heap:
        # Obtenemos el menor elemento del heap min
        val, list_idx, element_idx = heapq.heappop(min_heap)
        
        # Agregamos el elemento a la lista fusionada
        merged_list.append(val)
        
        # Movemos al siguiente elemento en la lista correspondiente
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list


if __name__ == "__main__":
    # Definimos varias listas ordenadas de ejemplo
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6, 8, 10]
    lista3 = [0, 9, 11]
    
    # Mostramos las listas antes de la fusión
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista 3:", lista3)
    
    # Llamamos a la función de fusión
    listas_fusionadas = balanced_multiway_merge([lista1, lista2, lista3])
    
    # Mostramos la lista fusionada después del proceso
    print("Listas fusionadas:", listas_fusionadas)
