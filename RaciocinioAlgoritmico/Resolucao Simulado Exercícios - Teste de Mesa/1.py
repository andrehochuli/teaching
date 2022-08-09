#retorna o maior elemento
#entre a b c
def func(a,b,c):
    
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
        
def imprime(vet):
    chr_list = []

    for i in range(len(vet)):
        print( chr(vet[i]) , end = ' ')
        

vet = [66,68,111,50,32,108,10,97,92]
vet_res = []
t = len(vet)

#atente-se ao passo do for (de 3 em 3)
for i in range(0,t,3):    
    ret = func(vet[i],vet[i+1],vet[i+2])
    
    if ret == 108:
        print(vet[i],vet[i+1],vet[i+2])
    
    vet_res.append(ret)            

print(vet_res)
imprime(vet_res)
















    
