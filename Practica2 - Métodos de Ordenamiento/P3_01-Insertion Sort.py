
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
Insertion Sort es un algoritmo de ordenamiento que construye la lista ordenada de elementos uno a uno, 
insertando cada nuevo elemento en su posición correcta dentro de la lista ya ordenada. 
este proceso se repite hasta que todos los elementos están ordenados.
Insertion Sort es intuitivo y eficiente para ciertos tipos de listas, 
especialmente cuando se espera que la lista esté parcialmente ordenada o cuando se trabaja con un pequeño conjunto de datos.

Este método se puede separar en los siguientes pasos:
1) Inicialización: Comenzar con la sublista ordenada conteniendo el primer elemento.
2) Iteración: Para cada elemento en la sublista desordenada, considerar el elemento como "key".
3) Comparación: Comparar el "key" con los elementos de la sublista ordenada de derecha a izquierda.
4) Desplazamiento: Desplazar los elementos mayores que el "key" una posición hacia la derecha.
5) Inserción: Insertar el "key" en su posición correcta.
6) Repetición: Repetir los pasos del 2 al 5 hasta que toda la lista esté ordenada.

Caracteristicas:
* Adaptabilidad: Es muy eficiente para listas pequeñas y para listas que ya están mayormente ordenadas, con una complejidad de tiempo de
O(n) en el mejor caso (cuando la lista ya está ordenada).
* Estabilidad: Es un algoritmo estable, lo que significa que no cambia el orden relativo de los elementos con valores iguales.
* Simple implementación: Es fácil de implementar y entender.
* Complejidad: En el peor caso y en el caso promedio, la complejidad temporal es O(n^2), donde n es el número de elementos en la lista.
* Espacio: No requiere espacio adicional significativo, ya que ordena la lista en su lugar.
"""

def insertion_sort(arr):

    # Iterar sobre cada elemento de la lista comenzando desde el segundo elemento
    for i in range(1, len(arr)):
        key = arr[i] # Elemento actual a insertar en la parte ordenada
        j = i - 1 # Índice del último elemento de la parte ordenada

        # Mover elementos de la parte ordenada que son mayores que la 'key'
        # una posición hacia la derecha para hacer espacio para la 'key'
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar la 'key' en la posición correcta
        arr[j + 1] = key
    
    return arr

if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [12, 11, 13, 5, 6]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = insertion_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
