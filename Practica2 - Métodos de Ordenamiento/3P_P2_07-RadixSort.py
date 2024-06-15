
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
RadixSort es un algoritmo de ordenamiento que ordena números procesando sus dígitos individualmente, 
comenzando desde el dígito menos significativo hasta el más significativo. 
Utiliza un subalgoritmo de ordenamiento estable, como Counting Sort, para ordenar los números basándose en cada dígito.
Se procesa cada dígito de los números en la lista, comenzando desde el dígito menos significativo (unidad) hasta el más significativo.
Counting Sort se usa para ordenar los números basándose en el dígito actual. Es crucial que el subalgoritmo sea estable para que RadixSort funcione correctamente.
Un algoritmo de ordenamiento es estable si preserva el orden relativo de los elementos con valores iguales. RadixSort depende de esta propiedad para funcionar correctamente.

Proceso: 
1) Determinación del Máximo: Encuentra el número máximo para determinar el número de dígitos.
2) Ordenación por Dígitos: Usa Counting Sort para ordenar la lista basándose en cada dígito, comenzando por el menos significativo.
3) Repetir para Cada Dígito: Repite el proceso para cada dígito significativo hasta que todos los dígitos hayan sido procesados.

Caracteristicas:
* Complejidad: RadixSort es un algoritmo eficiente para ordenar grandes conjuntos de números, especialmente cuando los números tienen un rango limitado. 
        La utilización de Counting Sort para cada dígito permite que RadixSort tenga una complejidad lineal en muchos casos prácticos, 
        haciéndolo muy eficiente para ciertos tipos de datos.
* Espacio: RadixSort no es in-place, ya que requiere espacio adicional para las listas temporales usadas durante el Counting Sort.
* Estabilidad: RadixSort es un algoritmo estable si el subalgoritmo de ordenamiento utilizado es estable (Counting Sort lo es).
"""

def counting_sort_for_radix(arr, exp):

    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Contar las ocurrencias de cada dígito en exp
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Cambiar count[i] para que contenga la posición actual de este dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el array de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copiar los elementos ordenados de output a arr
    for i in range(n):
        arr[i] = output[i]
    
    return arr

def radix_sort(arr):

    # Encontrar el número máximo para conocer el número de dígitos
    max_val = max(arr)
    
    # Aplicar Counting Sort a cada dígito (exp será 1, 10, 100, ...)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr


if __name__ == "__main__":
    # Definimos una lista de ejemplo
    ejemplo_lista = [170, 45, 75, 90, 802, 24, 2, 66]
    
    # Mostramos la lista antes del ordenamiento
    print("Lista antes del ordenamiento:", ejemplo_lista)
    
    # Llamamos a la función de ordenamiento
    lista_ordenada = radix_sort(ejemplo_lista)
    
    # Mostramos la lista después del ordenamiento
    print("Lista después del ordenamiento:", lista_ordenada)
