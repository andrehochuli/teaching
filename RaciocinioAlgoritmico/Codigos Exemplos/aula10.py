#Triplo + 10
def m_formula(x):

    print("Estou na m_formula")
    
    y = 3*x
    y += 10  

    return y;

#Maior entre a e b
def maior(a,b):
    print("Estou na maior")
    if a > b:
        return a
    else:
        return b
    
def soma3(a,b,c):
    print("Estou na soma")
    soma = a + b + c
    return soma

def imprime_linha():
    print("-----------")
    print("***********")
    print("HHHHHHHHHHH")

def reverte(vetor):
    tam = len(vetor)
    rev = []
    for i in range(tam-1,-1,-1):
        rev.append(vetor[i])

    return rev

vr = reverte([10,20,30,40])
print(vr)
'''x = 10
print("Fui")
y = m_formula(x)
print("Voltei, ", y)

imprime_linha()

print("Fui")
m = maior(30,60)
print("Voltei ",m)

x = 200
print("Fui")
m_formula(x)
print("Voltei, ", y)

imprime_linha()

x = 10
y = 20
print("Fui")
soma3(x,y,30)
print("Voltei, ", y)'''






