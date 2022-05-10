#Imprimir de forma ordenada (Selection Sort Algorithm)
		
import random
vet = []

for i in range(0,10):
    vet.append(random.randint(1000,30000))

tam = len(vet)


print(vet)
for i in range(0,tam):

    #Indice do menor elemento
    menor = i
    for j in range(i+1,tam):
        if vet[j] < vet[menor]:
            menor = j

    #Troca das posicoes
    temp = vet[i]    
    vet[i] = vet[menor] 
    vet[menor] = temp;



print(vet)
         
    
