#Altere o programa anterior para mostrar a soma do intervalo de números

#Faça um programa que receba dois números inteiros e
#gere os números inteiros que estão no intervalo compreendido por eles

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
soma = 0

#Inverto os numeros se o segundo é maior que o primeiro
if (n2 < n1):
    temp = n1
    n1 = n2
    n2 = temp
    

while(n1 <= n2):
    print(n1)
    soma += n1    
    n1 += 1
    

print("A soma é ", soma)