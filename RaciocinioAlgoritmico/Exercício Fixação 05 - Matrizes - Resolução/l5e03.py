'''2. Implemente o jogo do campo minado 
    Obs: considere uma versao minimalista do jogo'''


import random

mat = []

#Campo minado 30x30
for l in range(30):
    mat.append([])
    for c in range(30):
        num = random.random() #aleatorio entre 0 e 1

        #Se prob for maior que 80, entao bomba
        if num > 0.80:
            mat[l].append(1) #1 bomba
        else:
            mat[l].append(0) #0 livre


tem_bomba = 0

while tem_bomba == 0:

    for l in range(30):
        print(mat[l])
        
    l = int(input("Digite a linha: "))
    c = int(input("Digite a coluna: "))
    
    #se houver bomba, == 1
    tem_bomba = mat[l][c]
    if(tem_bomba == 0):
        print("Ufa, voce não pisou na bomba")

print("A bomba explodiu")
