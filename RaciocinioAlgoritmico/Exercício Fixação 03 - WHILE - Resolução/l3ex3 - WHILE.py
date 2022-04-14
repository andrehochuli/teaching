#3.	Faça um programa que leia 5 números e informe o maior número

i = 0
maior = -999999


while(i<5):
    
    n = int(input("Digite um numero: "))
    
    if n > maior:
        maior = n
    
    i+=1

print("O maior numero digitado foi: ", maior)