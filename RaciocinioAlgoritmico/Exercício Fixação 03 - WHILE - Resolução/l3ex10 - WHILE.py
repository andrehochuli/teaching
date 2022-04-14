#10.	Altere o programa anterior para imprimir até o N-enésimo elemento out até que elemento seja menor seja 500.
n2  = 0
n1  = 1

#Altero o final de linha para imprimir um espaço ao invés de nova linha
print(n2, end=' ') 
print(n1, end=' ') 

n_elem = int(input("Qual elemento da série deseja computar?: "))
n = 0
i=3
while (i <= n_elem and n < 500):
    #Calculo o elemento atual    
    print(n, end = ' ')
    n = n1 + n2
    #Atualizo os n1 e n2
    n2 = n1
    n1 = n
    i+=1
