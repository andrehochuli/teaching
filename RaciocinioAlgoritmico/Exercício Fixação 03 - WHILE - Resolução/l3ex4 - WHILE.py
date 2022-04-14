# -*- coding: utf-8 -*-
#4.	Faça um programa que leia 5 números e informe a soma e a média dos números.
i = 0
soma = 0


while(i<5):
    
    n = int(input("Digite um numero: "))
    
    soma += n
    
    i+=1

media = soma / 5
print("A soma eh: %d e a média é %.2f" % (soma,media))
