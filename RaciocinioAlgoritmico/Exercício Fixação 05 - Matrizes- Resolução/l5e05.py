'''5. Uma corrida tem 5 carros.
   Cada carro deve andar por 20 quadras.
   Cada carro percorre aleatoriamente de 1 a 3 quadras.
   
 
'''
#Utilizo algumas bibliotecas 
import random, time, os


mat = []

#Crio uma matriz em branco (caractere ' ')
for l in range(5):
    mat.append([])

fim = 0
rodada = 0
#So chega ao fim apos 20 colunas
while fim == 0:

    rodada += 1
    print("------------- Rodada %d----------------" % (rodada))

    for l in range(5):

        #Calculo o avanco do carro
        n = random.randint(1,3)    
        for c in range(n):
            mat[l].append('#')

        print("Carro ",l,mat[l])

        #Se o tamanho chegou a 20, acabou a corrida
        if len(mat[l]) >= 20:
            fim = 1
    
    #Espera 2 segundos para nova iteracao
    time.sleep(2) 
