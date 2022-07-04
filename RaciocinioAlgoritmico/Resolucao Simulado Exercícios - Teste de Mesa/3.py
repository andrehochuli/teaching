'''Resumo: Aqui implementamos a ordenacao de um vetor
O for externo determina a posição no vetor a ser avaliada,
enquanto que o for interno percorre o restante do vetor
O algoritmo é conhecido pelo nome de 'Selection Sort'
'''
'''
Funcao que Inverte o valor de a e b
Atentem-se ao uso de temp,
ao inves de a=b e b=a diretamente'''
def troca(a,b):

    temp = a
    a = b
    b = temp        
    return a,b

vet = [30,-2,60,2,50,70,-14,45]

t = len(vet)

'''For externo que percorre o vetor com o indice 'i' '''
for i in range(t):    

    '''atentem-se que ira imprimir o vetor inteiro
    caso 'i' (não vet[i]) seja 2. O que representa a terceira
    iteracao do laço'''
    if i == 2:
        print(vet)

    '''Este for mais interno, comecando sempre em i+i'''
    for j in range(i+1,t):

        '''Troca caso o elemente em vet[i] sejam maior que em vet[j]'''
        if vet[i] > vet[j]:            
            vet[i],vet[j] = troca(vet[i],vet[j])


print(vet)
