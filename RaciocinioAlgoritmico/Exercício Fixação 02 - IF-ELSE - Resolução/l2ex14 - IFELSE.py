#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia
#e R$ 0,25 se forem compradas pelo menos doze.
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra

qtd_macas = int(input("Quantas maças voce deseja comprar: "))

if (qtd_macas < 12):
    preco = 0.30
else:
    preco = 0.25

total = qtd_macas*preco
print("O valor final para ", qtd_macas, "é de: R$ %.2f" % (total))