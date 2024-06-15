
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
El método de ordenamiento por Intercambio o Bubble Sort es un algoritmo de ordenamiento sencillo pero ineficiente para listas grandes. 
Funciona repetidamente intercambiando los elementos adyacentes si están en el orden incorrecto.

Proceso:
1) Inicialización: Comenzar desde el primer elemento de la lista.
2) Comparación: Comparar cada par de elementos adyacentes.
3) Intercambio: Intercambiar los elementos si están en el orden incorrecto.
4) Burbujeo: Empujar el mayor elemento al final de la lista en cada iteración.
5) Optimización: Utilizar una bandera 'swapped' para verificar si se han realizado intercambios y terminar el algoritmo antes si la lista ya está ordenada.

Caracteristicas:
('O' = Operación del proceso y 'n' = Número de elementos dentro de la lista)
* Complejidad: Este método es muy simple, sin embargo, puede reducir su eficiencia dependiendo del numero de intercambios que requiera la lista.
* Espacio: Es un algoritmo in-place, lo que significa que no requiere espacio adicional significativo aparte de la lista que se está ordenando.
* Estabilidad: Es un algoritmo estable, lo que significa que no cambia el orden relativo de los elementos con valores iguales.
* Simplicidad: Es fácil de entender e implementar, lo que lo hace útil para contextos educativos y para listas pequeñas.
"""

def bubble_sort(arr):
    n = len(arr)  # Longitud de la lista
    
    # Iterar sobre cada elemento de la lista
    for i in range(n):
        # La bandera 'swapped' se usa para optimización, para terminar el algoritmo si la lista ya está ordenada
        swapped = False
        
        # Iterar sobre la lista desde el primer elemento hasta el último elemento no ordenado
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Si no se realizó ningún intercambio, la lista ya está ordenada
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [64, 34, 25, 12, 22, 11, 90]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = bubble_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
