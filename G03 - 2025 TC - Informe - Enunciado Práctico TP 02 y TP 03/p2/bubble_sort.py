def bubble_sort(lista):
    n = len(lista)
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
numeros = [5, 3, 4, 8, 7, 5, 1, 2, 3]

ordenada = bubble_sort(numeros)
print("Lista ordenada:", ordenada)