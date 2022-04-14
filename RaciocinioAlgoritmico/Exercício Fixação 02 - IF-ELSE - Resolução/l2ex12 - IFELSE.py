# -*- coding: utf-8 -*-
#Peça o login e senha de uma pessoa e informe se o login é valido

ano = int(input("Digite seu ano de nascimento: "))

ano_atual = 2022

idade = ano_atual - ano

if (idade >= 16):
    print("Você tem ", idade, "anos e pode votar")
else:
    print("Você tem ", idade, "anos e infelizmente você ainda não pode votar")
    



