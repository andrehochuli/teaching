#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

n = int(input("Qual o número a ser fatorado ?"))



fat = n

print("%d! = %d" % (fat,n) , end=' ')

while (n > 1):
    n = n -1
    print(". %d" % (n) , end = ' ')
    fat = fat * n


print("= %d" % (fat)) 
