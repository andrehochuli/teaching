#2.Adicione 50 números aleatórios (rand()) em um vetor.
# Calcule a média, desvio padrão, valores máximos e mínimos
import random

vet = []
#Populando o vetor com 50 elementos
for i in range(0,50):
    n = random.randint(0,100)
    vet.append(n)


tam = len(vet)
menor = vet[0]
maior = vet[0]
soma = 0


#Maior, menor, soma
for i in range(0,tam):

    if vet[i] < menor:
        menor = vet[i]
    
    if vet[i] > maior:
        maior = vet[i]
        
    soma += vet[i]


media = soma/tam
soma_dif=0

#Soma das diferencas ao quadrado
for i in range(0,tam):
    soma_dif += (vet[i] - media)**2

#desvio padrao
dvp = (soma_dif/tam)**0.5

print(vet)
print("Menor: ", menor)
print("Maior: ", menor)
print("Media: ", media)
print("Desv Padrao: ", dvp)
