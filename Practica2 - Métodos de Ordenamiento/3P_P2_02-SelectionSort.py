
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
Selection Sort es un algoritmo de ordenamiento que divide la lista en dos partes: 
una sublista ordenada que se construye de izquierda a derecha en la lista y una sublista no ordenada que contiene los elementos restantes por ordenar. 
El algoritmo selecciona de manera iterativa el menor (o mayor, dependiendo del orden deseado) elemento de la sublista no ordenada 
y lo intercambia con el primer elemento no ordenado de la lista, moviendo así el límite entre las sublistas ordenada y no ordenada.

Proceso:
1) Inicialización: Considerar toda la lista como no ordenada.
2) Búsqueda del menor: Encontrar el menor elemento en la sublista no ordenada.
3) Intercambio: Intercambiar el menor elemento encontrado con el primer elemento no ordenado.
4) Avance del límite: Mover el límite entre las sublistas ordenada y no ordenada.
5) Repetición: Repetir los pasos 2-4 hasta que toda la lista esté ordenada.

Caracteristicas:
('O' = Operación del proceso y 'n' = Número de elementos dentro de la lista)
* Complejidad Temporal: El algoritmo se vuelve menos eficiente mientras mas grande se vuelva la lista.
* Espacio: Es un algoritmo in-place, lo que significa que no requiere espacio adicional significativo aparte de la lista que se está ordenando.
* Estabilidad: No es un algoritmo estable, lo que significa que puede cambiar el orden relativo de los elementos con valores iguales.
* Eficiencia: Aunque simple y fácil de entender, no es el más eficiente para listas grandes debido a su complejidad cuadrática.
"""

def selection_sort(arr):

    n = len(arr)  # Longitud de la lista
    
    # Iterar sobre cada elemento de la lista
    for i in range(n):
        # Suponer que el primer elemento no ordenado es el menor
        min_idx = i
        
        # Encontrar el menor elemento en la sublista no ordenada
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambiar el menor elemento encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [64, 25, 12, 22, 11]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = selection_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
