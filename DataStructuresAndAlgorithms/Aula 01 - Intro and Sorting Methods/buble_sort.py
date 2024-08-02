import time
import numpy as np

def bubble_sort(arr):	
	n_trocas = 0
	n = len(arr)
	for i in range(n):
		# Flag para otimização: Se nenhum elemento for trocado, o vetor já está ordenado
		troca = False
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				# Troca os elementos
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				troca = True
				n_trocas += 1
				
		# Se não houve trocas, o vetor já está ordenado
		if not troca:
			break
	return arr, n_trocas
    
def insertion_sort(arr):
    num_trocas = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            num_trocas += 1
        arr[j + 1] = key
    return arr, num_trocas
    
#arr = [23,-2,30,-20]

for size in [10,100,1000,10000,20000]:
	
	#Sorteia 'size' elements 
	arr = np.random.randint(-9999, 9999, size)
	#print(arr)

	t1 = time.time() 
	arr,n_trocas = insertion_sort(arr)
	t2 = time.time()

	tt = t2 - t1
	#print(arr)
	print(f'Size= {size} || Tempo total: {tt:.10f} segs || Trocas {n_trocas}')
