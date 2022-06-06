'''1.	Crie e popule as seguintes matrizes:
    a.	2x2, 5x3, 10x5
    b.	Apresente a soma de cada coluna
    c.	Apresente o maior elemento de cada linha'''

import random

mat = []
#Populo a matriz
for l in range(10):
    mat.append([])
    for c in range(5):
        num = random.randint(0,50)
        mat[l].append(num)

    
#Para somar cada coluna
#Inverto a ordem de caminhamento
for c in range(5):
    soma = 0
    for l in range(10):
        soma += mat[l][c]    

    print("Soma da coluna [%d] %d" % (c,soma)) 


print("----------------------")

for l in range(10):

    #considero o primeiro o maior
    max_v = mat[l][0]

    #caminho a partir do segundo
    for c in range(1,5):
        if mat[l][c] > max_v:
            max_v = mat[l][c]

    print("Maior elemento da linha [%d] %d" % (l,max_v))
