# -*- coding: utf-8 -*-
#Informe o maior número entre dois números quaisquer
#Desconsidere neste momento dois números iguais

#Obs: Os exercícios 4 e 5 são idênticos

#Outra forma de converter o input é int(input(..))
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

#Soluçao 1: Com repetição do print alterando a ordem das variaveis
if num1 > num2:
    print("Solução-1: O número ", num1, "é maior que ", num2)
else:
    print("Solução-1: O número ", num2, "é maior que ", num1)
    
    
#Solucao 2: Determinando o maior e o menor    
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1    
    
print("Solução-2: O número ", maior, "é maior que ", menor)