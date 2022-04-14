#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
#O usuário deve informar de qual numero ele deseja ver a tabuada. 


n = int(input("Qual tabuado voce quer ver : "))
i=1

while(i<=10):
    
    print("%d x %d = %d" % (n,i,n*i))
    i+=1    