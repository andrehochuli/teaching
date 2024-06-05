## Lista de Exercícios - Recusividae

1. Implemente uma função recursiva que imprime todos os números de \( N \) até 0.
   
   ```python
   def print_rec(N):
       print(N)
       if N != 0:        
          print_rec(N-1)
   ```
   
       

2. Implemente uma função recursiva que imprime todos os números de 0 até N.
   
   ```python
   def print_rec(N):
       
       if N != 0:        
          print_rec(N-1)
       
       print(N)
   ```

3. Desenvolva uma função recursiva que retorna a soma de todos os números inteiros de \( N \) até 0.
   
   ```python
   def soma(N):
   	
   	if N == 0:
   		return 0
   	
   	s = N + soma(N-1)
   	
   	return s
   ```

4. Crie uma função recursiva que calcula a soma dos dígitos de um número inteiro. (4871 = 20)
   
   ```python
   def soma_digitos(n):
       if n == 0:
           return 0
       else:
           return n % 10 + soma_digitos(n // 10)
   ```

5. Implemente uma função recursiva que retorna a soma dos elementos de um vetor de inteiros.
   
   ```python
   def soma_vet(vet):
   	
   	if len(vet) == 1:
   		return vet[0]
   	
   	s = vet[0] + soma_vet(vet[1:])	
   	return s
   ```

6. Escreva uma função recursiva para calcular o fatorial de ( N ).
   
   ```python
   def fat(N):
   	
   	if N == 1:
   		return 1
   		
   	s = N*fat(N-1)
   	
   	return s
   ```

7.  Desenvolva uma função recursiva para calcular o \( n \)-ésimo termo da sequência de Fibonacci.
   
   ```python
   def fibo(N):
   	
   	if N == 0:
   		return 0
   	elif N == 1:
   		return 1
   		
   	s = fibo(N-1) + fibo(N-2)
   	
   	return s
   ```

8. Implemente o algoritmo Selection Sort para ordenar um vetor de inteiros.

```python
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
```
