# -*- coding: utf-8 -*-
#Detetive: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#“Telefonou para a vítima? “
#“Esteve no local do crime?”
#“Mora perto da vítima? “
#“Devia para a vítima? “
#“Já trabalhou com a vítima? “

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“. 

print("Responda as perguntas abaixo, utilizando (s)im ou (n)ao: ")

resp1 = input("Telefonou para vítima ? (s/n): ")
resp2 = input("Esteve no local do crime ? (s/n): ")
resp3 = input("Morava perto da vítima ? (s/n): ")
resp4 = input("Devia dinheiro a vítima ? (s/n): ")
resp5 = input("Já trabalhou com a vítima ? (s/n): ")

n_sim = 0

if resp1 == 's':
    n_sim = n_sim + 1

if resp2 == 's':
    n_sim = n_sim + 1

if resp3 == 's':
    n_sim = n_sim + 1

if resp4 == 's':
    n_sim = n_sim + 1

if resp5 == 's':
    n_sim = n_sim + 1


if n_sim < 2:
    print("Inocente")

elif n_sim == 2:
    print("Suspeita")

elif n_sim < 4:
    print("Cúmplice")

else:
    print("Assasina")
    
