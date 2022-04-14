# -*- coding: utf-8 -*-
#1.	Solicite números até que se digite um número primo

n_primo = False
n=0 

#Enquanto nao for primo
while (n_primo != True):
    
    n_primo = True        
    n = int(input("Digite um numero: "))
    
    i = 2
    
    #Verifica se eh divisivel entre 2 e N
    
    while( i < n ):
    
        #Caso seja, nao eh primo
        if n % i == 0:
            n_primo = False        
            
        i += 1        
        
        

print('Foi digitado o primo %d. Programa encerrado.' % (n) )