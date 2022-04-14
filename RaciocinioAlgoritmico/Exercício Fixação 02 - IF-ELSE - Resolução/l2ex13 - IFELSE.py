# -*- coding: utf-8 -*-
#Informe se uma pessoa pode doar sangue (entre 18 e 59 anos)

ano = int(input("Digite seu ano de nascimento: "))

ano_atual = 2022

idade = ano_atual - ano

#Apresento duas soluçoes: Utilizando 'and' ou 'or'

#Solucao 1
if (idade >= 18 and idade <= 59):    
    print("Solucao 1: Você tem ", idade, "anos e pode doar sangue")
else:
    print("Solucao 1: Você tem ", idade, "anos e infelizmente você ainda não pode doar sangue")
    
    
#Solucao 2
if (idade < 18 or idade > 59):    
    print("Solucao 2: Você tem ", idade, "anos e infelizmente você ainda não pode doar sangue")
else:
    print("Solucao 2: Você tem ", idade, "anos e pode doar sangue")
    



