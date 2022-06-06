'''4.	Implemente o Jogo da Velha
   OBS: Nesta resolucao me atentei a logica do jogo (linhas, colunas, diagonais)
   A questao de modo de jogo P vs P ou P vs Computador,
   Ja foi trabalhada em outro exercício e trabalho
 
'''


####Spoiler de funcoes :)####
''' Essa funcao recebe uma matriz e verifica se houve
    a condicao de velha nas linhas, colunas e diagonais.
    Caso sim, retorna 1, senao 0'''

def verifica_velha(mat):
    
    
    #Verifico a velha nas linhas
    for l in range(3):
        if mat[l][0] != ' ' and mat[l][0] == mat[l][1] and mat[l][1] == mat[l][2]:
            return 1 #velha
            
    
    #Verifico a velha nas colunas
    for c in range(3):
        if mat[0][c] != ' ' and mat[0][c] == mat[1][c] and mat[1][c] == mat[2][c]:
            return 1 #velha

    #Verifico a velha nas diagonais
    if mat[0][0] != ' ' and mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2]:
        return 1 #velha
    elif mat[0][2] != ' ' and mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0]:
        return 1 #velha

    
    return 0 #sem velha


mat = []

#Crio uma matriz em branco (caractere ' ')
for l in range(3):
    mat.append([])
    for c in range(3):
        mat[l].append(' ')    

velha = 0
num_jogadas = 0

while velha == 0 and num_jogadas <= 9:

    print('-------------------')

    for l in range(3):
        print(mat[l])
        
    print('-------------------')
    
    l = int(input("Escolha a linha: "))
    c = int(input("Escolha a coluna: "))
    
    jog = input("Jogue X ou O: ")
    num_jogadas += 1
    mat[l][c] = jog

    
    velha = verifica_velha(mat)
    
for l in range(3):
    print(mat[l])
    
print("Jogo Encerrado")

    
    
                                            
                    

        
