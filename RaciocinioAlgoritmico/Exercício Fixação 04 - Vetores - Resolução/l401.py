import random

vet = []
#Populando o vetor com 10 elementos
for i in range(0,10):
    n = random.randint(0,100)
    vet.append(n)

#Encontrando o menor
menor = vet[0]
for i in range(0,10):
    if vet[i] < menor:
        menor = vet[i]

print("Menor: ", menor)
