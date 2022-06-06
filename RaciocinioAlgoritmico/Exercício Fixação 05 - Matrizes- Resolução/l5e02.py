'''2. Crie uma matriz quadrada e informe a média da diagonal'''

import random

mat = []
#Populo a matriz
for l in range(5):
    mat.append([])
    for c in range(5):
        num = random.randint(0,50)
        mat[l].append(num)

    
#Diagonal Principal l == c
#Metodo 1: if
soma=0
for l in range(5):
    for c in range(5):        
        if l == c:
            soma += mat[l][c]

print("Soma diagonal principal metodo-1: ",soma)


#Metodo 2: Utilizando 1 laco
soma=0
for i in range(5):
    soma += mat[i][i]

print("Soma diagonal principal metodo-2: ",soma)

#Diagonal Secundaria l[0] == c[4], l[1] == c[3] ...
soma=0
for i in range(5):
    soma += mat[i][4-i]

print("Soma diagonal secundaria: ",soma)

