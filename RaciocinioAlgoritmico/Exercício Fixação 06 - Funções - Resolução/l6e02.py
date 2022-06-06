'''2. Crie uma função que dado um vetor
    retorna todos os índices que contenham
    numeros pares'''

def ret_idx_pares(vet):

    #vetor de indices
    idx = []
    
    for i in range(len(vet)):
        if vet[i] %2 == 0:
            idx.append(i)

    return idx


vet = [12,4,5,8,7,21,872]

idx_pares = ret_idx_pares(vet) 
print(vet,idx_pares)


    
