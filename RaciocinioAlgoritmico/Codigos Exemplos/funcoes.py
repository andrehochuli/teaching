def funcao_maior(vet):
    print("oi, estou na funcao")
    maior = vet[0]
    tam = len(vet)

    #Varre o vetor
    for i in range(tam):

        if vet[i] > maior:
            maior = vet[i]

    print("tchau, saindo da funcao")
    return maior


def imprime_vet_parcial(vet,a,b):
    print("Estou na funcao imprime_vet_parcial")
    for i in range(a,b):
        print(vet[i], end=' ')
        

print('a inicio do codigo')    
vet = [20,40,12,24,50,44,32]
print('b vai funcao')
a = funcao_maior(vet)
print('c voltou funcao')

vet = [20,23,6666,40,12,24,50,44,32,52]
print('d vai funcao')
b = funcao_maior(vet)
print('e voltou funcao')
print(a,b)

imprime_vet_parcial(vet,4,8)



  
