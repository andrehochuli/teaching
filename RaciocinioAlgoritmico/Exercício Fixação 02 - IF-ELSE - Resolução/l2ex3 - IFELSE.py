# -*- coding: utf-8 -*-
#Informe o dia da semana a partir de um número entre 1 e 7. 
#Exemplo, 1- Domingo, 2- Segunda etc. 
#Se digitar outro valor deve aparecer “valor inválido”)

num = input("Digite um numero: ")

#int() converte o que foi digitado para inteiro
num = int(num)

if (num == 1):
    print("Domingo")
    
if (num == 2):
    print("Segunda")
    
if (num == 3):
    print("Terça")
    
if (num == 4):
    print("Quarta")
    
if (num == 5):
    print("Quinta")
    
if (num == 6):
    print("Sexta")
    
if (num == 7):
    print("Sabado")
    
if (num <= 0 or num >= 1):
    print('Valor Invalido')


#Obs: Futuramente, utilizaremos IF-ELIF para resover este exercício
