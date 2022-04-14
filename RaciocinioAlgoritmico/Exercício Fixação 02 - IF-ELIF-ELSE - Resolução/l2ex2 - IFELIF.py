# -*- coding: utf-8 -*-
#1.	Um estabelecimento, fornece uma comissão progressiva aos seus vendedores:
#a.	5%, para vendas até R$ 100,00
#b.	6% para vendas até R$ 500,00
#c.	7% para vendas até R$ 1000,00
#d.	8% para vendas acima de R$ 1000,00
#Implemente um algoritmo que calcule a comissão do vendedor.



valor = float(input('Digite o valor da venda: '))
comissao = 0

#Lembrando '%' é o modulo da divisão inteira
if (valor < 100.00):
    comissao = 0.05
elif (valor < 500.00):
    comissao = 0.06
elif (valor < 1000.00):
    comissao = 0.07
#senao é acima de 1000
else:
    comissao = 0.08

vlr_comissao = valor * comissao

print("A comissão do vendedor é: ", vlr_comissao)

