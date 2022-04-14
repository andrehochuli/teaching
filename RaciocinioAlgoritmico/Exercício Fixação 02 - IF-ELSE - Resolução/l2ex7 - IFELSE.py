# -*- coding: utf-8 -*-
#Informe se um número é par (Use o módulo da divisão (%))

#Dica: Número par é todo numero divisível por 2, logo, os demais são impares

num = int(input("Digite um número: "))

if (num % 2 == 0):
    print("O número ", num, "é par")
else:
    print("O número ", num, "é ímpar")
    
