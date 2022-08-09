#Esta funcao retorna o menor elemento entre x e y
#Em caso de igualdade retorna z
def func(x,y,z):
    
    if x < y:
        return x
    elif y < x:
        return y
    else:
        return z
        
def imprime(vet):
    
    for i in range(len(vet)):
        print( chr(vet[i]) , end='')

vet = [55,35,36,68,67,35,75,75,64,83,90,100]

vet_res = []
t = len(vet)

#Atente-se ao passo do for (3 em 3)
for i in range(0,t,3):    
    ret = func(vet[i],vet[i+1],vet[i+2])
    
    if ret == 35:
        print("Aqui: ", vet[i],vet[i+1],vet[i+2])
    
    vet_res.append(ret)            

print(vet_res)
imprime(vet_res)




























    
