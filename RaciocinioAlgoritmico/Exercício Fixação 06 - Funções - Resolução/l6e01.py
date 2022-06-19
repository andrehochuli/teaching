'''1.	Crie as funções:'''

#max()
def maior_elem(vet):

    maior = vet[0]
    for i in range(1,len(vet)):
        if vet[i] > maior:
            maior = vet[i]

    return maior

#min()
def menor_elem(vet):
    menor = vet[0]
    for i in range(1,len(vet)):
        if vet[i] < menor:
            menor = vet[i]

    return menor

#inv()
def vet_inv(vet):
    inverso = []
    
    for i in range(len(vet)-1, -1, -1):
        inverso.append(vet[i])

    return inverso

#converte letras min para maiusculas (somente de letras (a-z))
def maiusculo(plv):

    plv_nova = ""
    asc_ini = ord('a')
    asc_fim = ord('z')
    
    for i in range(0, len(plv)):

        #vejo se o ascii esta dentro do intervalo minusculo
        asc = ord(plv[i])        
        if (asc >= asc_ini) and (asc <= asc_fim):                         
            #32 reflete a diferenca de mai e min na tab ascii
            plv_nova += chr(asc - 32)              
        else:
            plv_nova += plv[i]
 
    return plv_nova

#converte letras maiusculas para min (somente de letras (A-Z))
def minusculo(plv):
    plv_nova = ""
    asc_ini = ord('A')
    asc_fim = ord('Z')
    
    for i in range(0, len(plv)):

        #vejo se o ascii esta dentro do intervalo maisculos
        asc = ord(plv[i])        
        if (asc >= asc_ini) and (asc <= asc_fim):                         
            plv_nova += chr(asc + 32)
             
        else:
            plv_nova += plv[i]
 
    return plv_nova


def isdigit(n):

    #Valores ascii do intervalo 0-9
    asc_ini = ord('0')
    asc_fim = ord('9')

    if ord(n) >= asc_ini and ord(n) <= asc_fim:
        return True
    else:
        return False

def ischar(n):

    #Valores ascii do intervalo A-z
    #Na tab ascii, maisculo vem antes do minisculo
    asc_ini = ord('A') 
    asc_fim = ord('z')

    if ord(n) >= asc_ini and ord(n) <= asc_fim:
        return True
    else:
        return False



vet = [7,12,-3,59,0]
print(vet)

maior = maior_elem(vet)
print("Maior: ", maior)

menor = menor_elem(vet)
print("Menor: ", menor)


frase = '12 Abacaxis por 20 Reais'
print(frase)
frase_max = maiusculo(frase)
print("TUDO MAISCULO: ", frase_max)

frase_min = minusculo(frase)
print("tudo min: ", frase_min)

d = '2'
c = 'F'

resp1 = isdigit(d) 
resp2 = isdigit(c) 
print('%c e %c sao digitos? %r, %r' % (d,c,resp1,resp2))

resp1 = ischar(d) 
resp2 = ischar(c) 
print('%c e %c sao caracteres? %r, %r' % (d,c,resp1,resp2))

vet= [10,20,30,40]
vet_inverso = vet_inv(vet)
print("Vetor Original ", vet)
print("Vetor inverso", vet_inverso)
