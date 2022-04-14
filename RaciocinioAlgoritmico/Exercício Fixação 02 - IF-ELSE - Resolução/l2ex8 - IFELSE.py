# -*- coding: utf-8 -*-
#Informe se um número é múltiplo de um número N qualquer

#Dica: Um número é múltiplo de N se for divisível por N

num = int(input("Digite um número: "))
N = int(input("Digite outro número: "))

if (num % N == 0):
    print("O número ", num, "é múltiplo de ", N)
else:
    print("O número ", num, "não é múltiplo de ", N)
    
    
