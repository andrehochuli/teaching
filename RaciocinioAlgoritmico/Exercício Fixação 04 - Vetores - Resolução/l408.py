#8. Tres notas sequencias

import random
nfs = []

#Populo 10K numeros de 0 a 499
for i in range(0,10000):
    nfs.append(random.randint(0,499))

#Sobrescrevo com um vetor menor para validar a logica
nfs = [10,200,10,300,301,300,200,201,202,200,762,10]

tam = len(nfs)
nfs_rept = []

#tam-2 pois nao preciso ir ate o fim
for idx in range(0,tam-2):
    
    
    if (nfs[idx]+1 == nfs[idx+1]) and (nfs[idx]+2 == nfs[idx+2]):
        print("3 Sequenciais: ", nfs[idx],nfs[idx+1],nfs[idx+2])
         
    
