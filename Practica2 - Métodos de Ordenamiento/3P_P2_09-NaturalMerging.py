
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
Natural Merging es una variante del algoritmo MergeSort que explota el hecho de que las listas de entrada suelen contener secuencias de elementos ya ordenados. 
En lugar de dividir la lista en sublistas de tamaños iguales, Natural Merging identifica y utiliza estas secuencias ordenadas (runs) para hacer la fusión más eficiente.
Un run es una sublista de elementos que ya están ordenados. Natural Merging comienza identificando estos runs en la lista de entrada.
Después de identificar los runs, se fusionan iterativamente hasta que toda la lista esté ordenada.

Proceso:
1) Identificación de Runs: Encuentra las sublistas ordenadas en la lista de entrada.
2) Iteración y Fusión: Fusiona iterativamente los runs identificados hasta que toda la lista esté ordenada.
3) Fusión Final: Fusiona los runs ordenados para formar la lista ordenada final.

Caracteristicas:
* Complejidad: Natural Merging es un algoritmo eficiente y estable, especialmente útil cuando la lista de entrada ya contiene secuencias ordenadas largas. 
    Explota estas secuencias para reducir el número de operaciones de fusión necesarias, haciendo el proceso de ordenamiento más eficiente.
* Espacio: Natural Merging utiliza espacio adicional para las listas temporales durante la fusión, similar a otros métodos de MergeSort.
* Estabilidad: Natural Merging es estable, lo que significa que no cambia el orden relativo de los elementos con valores iguales.
"""

def merge(arr, left, mid, right):

    # Crear arrays temporales para los subarrays
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Inicializar índices para fusionar los subarrays
    i = 0
    j = 0
    k = left

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

def natural_merge_sort(arr):

    # Función para encontrar sublistas ordenadas
    def find_runs(arr):
        runs = []
        n = len(arr)
        new_run = [0]
        
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                runs.append((new_run[0], i - 1))
                new_run = [i]
        
        runs.append((new_run[0], n - 1))
        return runs
    
    # Ejecutar el algoritmo de ordenamiento
    if len(arr) <= 1:
        return arr
    
    runs = find_runs(arr)
    
    while len(runs) > 1:
        new_runs = []
        
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                left, mid = runs[i]
                _, right = runs[i + 1]
                merge(arr, left, mid, right)
                new_runs.append((left, right))
            else:
                new_runs.append(runs[i])
        
        runs = new_runs
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6, 7, 19, 4, 2, 10, 3, 14]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = natural_merge_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
