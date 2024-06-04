def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivô = arr[-1]
    menores = []
    maiores = []
    
    # Adiciona os elementos menores que o pivô
    for x in arr[:-1]:
        if x <= pivô:
            menores.append(x)
    
    # Adiciona os elementos maiores que o pivô
    for x in arr[:-1]:
        if x > pivô:
            maiores.append(x)
    
    # Chama recursivamente o Quick Sort nas sublistas menores e maiores
    menores_ordenados = quick_sort(menores)
    maiores_ordenados = quick_sort(maiores)
    
    # Concatena as sublistas menores e maiores com o pivô
    menores_ordenados.append(pivô)
    menores_ordenados.extend(maiores_ordenados)
    
    return menores_ordenados


def selection_sort(vet, i=0):
	# Caso base: se 'i' é igual ao tamanho da lista menos um, a lista está ordenada
	if i == len(vet) - 1:
		return vet

	# Encontrar o índice do menor elemento na sublista a partir de 'i'
	min_index = i
	for j in range(i + 1, len(vet)):
		if vet[j] < vet[min_index]:
			min_index = j     

	temp = vet[i]
	vet[i] = vet[min_index]
	vet[min_index] = temp

	# Chamar recursivamente a função 'ordena' para o próximo índice
	return selection_sort(vet, i + 1)

def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + soma_digitos(n // 10)
        

def print_rec(N):	
	
	print(N)
	
	if N != 0:		
		print_rec(N-1)
	
def soma(N):
	
	if N == 0:
		return 0
	
	s = N + soma(N-1)
	
	return s
	
def fat(N):
	
	if N == 1:
		return 1
		
	s = N*fat(N-1)
	
	return s
	
def fibo(N):
	
	if N == 0:
		return 0
	elif N == 1:
		return 1
		
	s = fibo(N-1) + fibo(N-2)
	
	return s
	
def soma_vet(vet):
	
	if len(vet) == 1:
		return vet[0]
	
	s = vet[0] + soma_vet(vet[1:])	
	return s	
