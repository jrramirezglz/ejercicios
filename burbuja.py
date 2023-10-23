def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # Elegir el pivote, en este caso, el elemento
    # del medio
    left = [x for x in arr if x < pivot]  # Elementos menores que el pivote
    middle = [x for x in arr if x == pivot]  # Elementos iguales al pivote
    right = [x for x in arr if x > pivot]  # Elementos mayores que el pivote

    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
numeros = [3, 6, 8, 10, 1, 2, 1]
numeros_ordenados = quicksort(numeros)
print(numeros_ordenados)

numeros2 = [31, 62, 83, 104, 15, 26, 17, 31, 62, 83, 104, 15, 26, 17]
numeros3 =sorted(numeros2)
print(numeros3)

numeros6 = [314, 625, 836, 1047, 158, 269, 170, 314, 625, 836, 1047, 158, 269, 170]
numeros4 = set(numeros6)
print(numeros4)
lista_new = list(numeros4)
print(lista_new)
lista_new.reverse()
print(lista_new)
