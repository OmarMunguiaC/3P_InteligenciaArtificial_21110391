
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
MergeSort es un algoritmo eficiente y estable, especialmente adecuado para grandes conjuntos de datos y cuando la estabilidad del algoritmo es importante.
La idea central es dividir la lista de elementos en sublistas más pequeñas hasta que cada sublista tenga un solo elemento 
y luego combinar estas sublistas de manera ordenada para formar la lista ordenada final.

Proceso:
1) División: Recursivamente divide la lista en sublistas hasta que cada sublista tenga un solo elemento.
2) Ordenar y Fusionar: Compara los elementos de las sublistas y fusiónalos en una nueva lista ordenada.
3) Combinar: Repite el proceso de fusión hasta que todas las sublistas estén fusionadas en una lista ordenada.

Caracteristicas:
* Estabilidad: MergeSort es un algoritmo estable, lo que significa que no cambia el orden relativo de los elementos con valores iguales. 
               Esto es importante cuando se necesita mantener el orden original de elementos con claves iguales.
* Complejidad: MergeSort tiene una complejidad temporal de O(nlogn) en el peor, mejor y promedio de los casos. 
               Esto se debe a que cada división de la lista toma O(logn) y cada fusión toma O(n).
* Espacio Adicional: MergeSort no es in-place, lo que significa que requiere espacio adicional para las listas temporales usadas durante la fusión. 
                     La cantidad de espacio adicional es proporcional al tamaño de la lista original.
* Divide y Vencerás: La técnica de "divide y vencerás" permite que MergeSort sea fácil de paralelizar, ya que cada mitad de la lista se puede ordenar de manera independiente.
"""

def merge_sort(arr):

    if len(arr) > 1:
        # Encontrar el punto medio de la lista
        mid = len(arr) // 2
        
        # Dividir la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Llamar recursivamente a merge_sort en cada mitad
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Inicializar los índices para la sublista izquierda, derecha y lista principal
        i = j = k = 0
        
        # Copiar los datos a las listas temporales left_half y right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Verificar si quedan elementos en la lista izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Verificar si quedan elementos en la lista derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [38, 27, 43, 3, 9, 82, 10]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = merge_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
