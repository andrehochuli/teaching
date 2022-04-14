# -*- coding: utf-8 -*-
#10 elementos de fibonacci

n2  = 0
n1  = 1

#Altero o final de linha para imprimir um espaço ao invés de nova linha
print(n2, end=' ') 
print(n1, end=' ') 

i=3
while (i <= 10):
    #Calculo o elemento atual
    n = n1 + n2
    print(n, end = ' ')
    
    #Atualizo os n1 e n2
    n2 = n1
    n1 = n
    i+=1
    
