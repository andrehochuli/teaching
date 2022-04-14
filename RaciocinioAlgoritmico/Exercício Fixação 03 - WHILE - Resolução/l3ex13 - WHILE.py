# -*- coding: utf-8 -*-
#Juros Compostos: Sabendo-se o valor de uma casa atualmente, 
#calcule quanto ela valia X anos atras. Imprima ano a ano o valor atualizado da casa.


valor = float(input("Qual o valor atual do imovel?"))
juros = float(input("Qual era taxa de juros anual?"))
anos = int(input("Por quantos anos o investimento foi ma?"))


#Converto o juros entre 0 e 1
juros = juros/100.

i = 1
while( i <= anos):
    
    valor_regressivo = valor / (1 + juros)**i
    print("%d ano(s) atras, o imovel valia R$ %.2f" % (i,valor_regressivo))
    i+=1