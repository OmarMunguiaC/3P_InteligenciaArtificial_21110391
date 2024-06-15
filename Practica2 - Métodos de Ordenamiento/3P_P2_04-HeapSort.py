
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
Heap Sort es un algoritmo de ordenamiento basado en un árbol binario llamado heap.
Un heap es un árbol binario completo donde cada nodo cumple la propiedad de heap. En un max heap, para cada nodo i,
el valor del nodo es mayor o igual que los valores de sus hijos. 
En un min-heap, el valor del nodo es menor o igual que los valores de sus hijos. Heap Sort generalmente usa un max-heap.
La operación heapify es fundamental para construir y mantener el heap. Dada una lista y un índice, 
heapify asegura que el subárbol con raíz en ese índice cumpla la propiedad de heap.

Proceso:
1) Construcción del Heap: Convertir la lista en un max heap.
2) Intercambio y Reducción del Heap: Intercambiar la raíz con el último elemento y reducir el tamaño del heap.
3) Heapify: Aplicar heapify para restaurar la propiedad de heap.
4) Repetición: Repetir el proceso hasta que el heap se reduzca a un solo elemento.

Caracteristicas:
('O' = Operación del proceso y 'n' = Número de elementos dentro de la lista)
* Complejidad: Heap Sort es un algoritmo eficiente y robusto que se utiliza cuando se necesita una complejidad temporal garantizada de O(nlogn).
* Espacio: Es un algoritmo in-place, lo que significa que no requiere espacio adicional significativo aparte de la lista que se está ordenando.
* No Estable: Heap Sort no es un algoritmo estable, lo que significa que puede cambiar el orden relativo de los elementos con valores iguales.
* Eficiencia: Es eficiente y tiene una complejidad de tiempo de O(nlogn), lo que lo hace adecuado para listas grandes.
"""

def heapify(arr, n, i):

    largest = i      # Inicializar el más grande como la raíz
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Si el hijo derecho es mayor que el más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
        # Recursivamente convertir el subárbol afectado en un heap
        heapify(arr, n, largest)

def heap_sort(arr):

    n = len(arr)

    # Construir un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mover la raíz actual al final
        heapify(arr, i, 0)  # Llamar a heapify en el heap reducido

    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6, 7]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = heap_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
