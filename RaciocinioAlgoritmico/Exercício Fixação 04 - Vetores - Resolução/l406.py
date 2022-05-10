#6. Identifique situações em que o mesmo número de nota fiscal se repete.
# Apresente os índices do vetor que isso ocorre.

import random
nfs = []

#Populo 10K numeros de 0 a 499
#for i in range(0,10000):
#    nfs.append(random.randint(0,499))

#Sobrescrevo com um vetor menor para validar a logica
nfs = [10,200,10,300,45,300,200,10,45,200,762,10]

tam = len(nfs)

print(nfs)
nfs_rept = []
for idx_i in range(0,tam):

    #Se nao foi computado, imprimo o cabecalho
    if(nfs[idx_i] not in nfs_rept):
        print(nfs[idx_i], ' repete em [', end= '')
        
    for idx_j in range(idx_i+1,tam):

        #Se for igual e nao foi computado
        #Para simplificacao, permito o 'not in' neste momento        
        if (nfs[idx_i] == nfs[idx_j]) and (nfs[idx_i] not in nfs_rept):
            print(idx_j, end = ',')

    if(nfs[idx_i] not in nfs_rept):        
        print(']')
        
    nfs_rept.append(nfs[idx_i])
         
    
