import numpy as np
import time
import random
import bisect #nao pode ser usada no trabalho

# Definir a seed para garantir reproducibilidade
#random.seed(42)
#np.random.seed(42)

def linear_search(arr, element):
    for i, num in enumerate(arr):
        if num == element:
            return i
    return -1

def insert_sort():

	return vet

size = 1000000  # Tamanho do vetor

#Sorteia 'size' elements 
arr = np.random.randint(-99999999, 99999999, size)

# Ordenar o vetor
sorted_arr = sorted(arr) #deverá ser implementa no trabalho


# Para garantir que o valor vai existir, seleciona um número aleatório presente no vetor 
target_element = np.random.choice(arr)
target_element = sorted_arr[300000]

# Medir o tempo para encontrar o elemento no vetor desordenado (busca linear)
start_time = time.time()
index_linear_unsorted = linear_search(arr, target_element)
end_time = time.time()
linear_unsorted_search_time = end_time - start_time

# Medir o tempo para encontrar o elemento no vetor ordenado (busca linear)
start_time = time.time()
index_linear_sorted = linear_search(sorted_arr, target_element)
end_time = time.time()
linear_sorted_search_time = end_time - start_time


# Medir o tempo para encontrar o elemento no vetor ordenado (busca binária)
start_time = time.time()
index_binary = bisect.bisect(sorted_arr, target_element) #ESSA FUNCAO DEVERÁ SER IMPLEMENTADA NO TRABALHO
end_time = time.time()
binary_search_time = end_time - start_time

# Resultados
print(f"Tam Array {len(arr)} - Min: {sorted_arr[0]} - Max: {sorted_arr[-1]}")
print(f"Elemento: {target_element}")
print(f"Índice do elemento (busca linear - unsorted): {index_linear_unsorted}")
print(f"Tempo para encontrar no vetor desordenado (busca linear): {linear_unsorted_search_time:.10f} segundos\n\n")

print(f"Índice do elemento (busca linear - sorted): {index_linear_sorted}")
print(f"Tempo para encontrar no vetor ordenado (busca linear): {linear_sorted_search_time:.10f} segundos\n\n")

print(f"Índice do elemento (busca binária): {index_binary-1}") #Ajustando o index de 1 ... N, para 0 ... N-1
print(f"Tempo para encontrar no vetor ordenado (busca binária): {binary_search_time:.10f} segundos")
