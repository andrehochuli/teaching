#Biblioteca random para gerar numeros aleatórios
import random


#Gerar números aleatórios entre 1 e 100000
a = random.randint(1, 10000)
print(a)

#veja que a cada chamada, o numero muda
a = random.randint(1, 10000)
print(a)

i=0
while(i<25):
    a = random.randint(1, 10000)
    print(i,a)
    i+=1
    
    
a = random.randint(1, 10000)
b = random.randint(1, 10000)

s = a + b

print(a,b,s)