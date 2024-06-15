
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
Straight Merging, o MergeSort Iterativo, es una variación del algoritmo MergeSort que utiliza un enfoque iterativo en lugar de recursivo. 
Este método también se basa en la técnica de dividir y vencer, pero realiza las fusiones de manera iterativa, 
mejorando el uso de la memoria en comparación con la versión recursiva.
El array se divide en subarrays más pequeños de manera iterativa.En cada iteración, se fusionan los subarrays ordenados hasta que todo el array está ordenado.
Se crean subarrays de tamaño creciente que se fusionan de forma iterativa.
Al igual que MergeSort recursivo, el MergeSort iterativo es estable, preservando el orden relativo de elementos iguales.

Proceso: 
1) Inicialización de Subarrays: Comienza con subarrays de tamaño 1.
2) Iteración y Fusión: En cada iteración, fusiona subarrays de tamaño creciente hasta que todo el array está ordenado.
3) Fusión Final: Fusiona los subarrays ordenados para formar la lista ordenada final.

Caracteristicas:
* Complejidad: Straight Merging es un algoritmo eficiente y estable, 
    adecuado para listas grandes y situaciones donde se prefiere una implementación iterativa sobre una recursiva para mejorar el uso de la memoria.
* Espacio: Straight Merging utiliza espacio adicional para las listas temporales durante la fusión, similar a MergeSort recursivo.
* Estabilidad: Straight Merging es estable, lo que significa que no cambia el orden relativo de los elementos con valores iguales.
"""

def merge(arr, l, m, r):

    n1 = m - l + 1
    n2 = r - m

    # Crear arrays temporales
    L = [0] * n1
    R = [0] * n2

    # Copiar los datos a los arrays temporales L[] y R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Fusionar los arrays temporales de nuevo en arr[l..r]
    i = 0     # Índice inicial del primer subarray
    j = 0     # Índice inicial del segundo subarray
    k = l     # Índice inicial del subarray fusionado

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L[], si hay alguno
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R[], si hay alguno
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_iterative(arr):

    current_size = 1
    
    # Iterar sobre los tamaños de subarrays 1, 2, 4, 8, ...
    while current_size < len(arr) - 1:
        left = 0
        # Iterar sobre los subarrays actuales
        while left < len(arr) - 1:
            mid = min((left + current_size - 1), (len(arr) - 1))
            right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr) - 1])
            
            # Fusionar los subarrays arr[left...mid] y arr[mid+1...right]
            merge(arr, left, mid, right)
            left = left + current_size * 2

        # Incrementar el tamaño de subarrays a fusionar
        current_size = 2 * current_size
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6, 7]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = merge_sort_iterative(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
