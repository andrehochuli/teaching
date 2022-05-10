#4.Crie um vetor aleatório com 100 elementos,
# apresente a soma de cada elemento inversamente opostos
import random

vet = []
#Populando o vetor com 50 elementos
for i in range(0,100):
    n = random.randint(100,500)
    vet.append(n)

tam = len(vet)

print(vet)


for idx in range(0,tam):

    idx_oposto = (tam-1) - idx #elemento oposto    
    soma = vet[idx] + vet[idx_oposto]
    
    print("vet[%d] + vet[%d] => %d + %d => %d" %
          (idx,idx_oposto,vet[idx],vet[idx_oposto],soma))
