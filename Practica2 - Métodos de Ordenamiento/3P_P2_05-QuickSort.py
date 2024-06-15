
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
QuickSort es un algoritmo de ordenamiento eficiente y de uso general. Es un algoritmo que se caracteriza por la frase: "divide y vencerás".
Se selecciona un elemento de la lista como pivote. El pivote puede ser cualquier elemento, aunque comúnmente se elige el primer, último o un elemento al azar. 
y este se usa para dividir la lista en sublistas.
Los elementos de la lista se reorganizan de modo que todos los elementos menores o iguales al pivote queden a su izquierda y todos los elementos mayores queden a su derecha.
Esto da lugar a dos sublistas: una de elementos menores o iguales al pivote y otra de elementos mayores.
Las sublistas ordenadas se combinan con el pivote para formar la lista ordenada final.

Proceso:
1) Seleccionar Pivote: Elegir un pivote de la lista.
2) Dividir la Lista: Reorganizar la lista en dos sublistas en función del pivote.
3) Ordenar Recursivamente: Aplicar QuickSort recursivamente a las sublistas.
4) Combinar: Combinar las sublistas ordenadas con el pivote.

Caracteristicas:
* Complejidad: QuickSort es un algoritmo eficiente y versátil, ampliamente utilizado debido a su rendimiento en promedio de O(nlogn). 
  Esto lo vuelve particularmente útil para grandes conjuntos de datos.
* Espacio: QuickSort no es in-place en esta implementación (debido a la creación de sublistas). Sin embargo, hay versiones in-place.
* No Estable: QuickSort no es un algoritmo estable, lo que significa que puede cambiar el orden relativo de los elementos con valores iguales.
* Eficiencia: Es muy eficiente y se usa ampliamente en la práctica debido a su complejidad promedio de O(nlogn).
"""

def quicksort(arr):

    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(arr) <= 1:
        return arr
    else:
        # Elegir un pivote (aquí elegimos el pivote como el primer elemento)
        pivot = arr[0]
        
        # Dividir la lista en sublistas: menores, iguales y mayores al pivote
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        
        # Ordenar recursivamente las sublistas y combinarlas con el pivote
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [10, 7, 8, 9, 1, 5]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = quicksort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
