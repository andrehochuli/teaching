# Simulado de Prova - Vetores, Matrizes e Funções

Este simulado contém questões similares às que serão cobradas na avaliação individual a ser realizada em sala de aula. Durante a avaliação, você deverá escrever suas respostas à mão, sem consultar ou receber ajuda do computador. O objetivo é avaliar suas habilidades e conhecimentos em lógica de programação.

Por isso, para que o simulado seja eficaz, recomendamos que você resolva as questões diretamente em uma folha de papel.

As listas de exercícios realizadas ao longo das aulas também é uma excelente base de estudo.

### 1. Testes de Mesa

a. Qual valor será impresso na tela?

```python
vet = [1,2,3,4,5,6]

vet[0] = vet[3]
vet[3] = vet[0]
vet[2] = vet[4]
vet[5] += vet[1] + vet[3]
print(vet)
```

```python
vet = [0,1]
for i in range(2,8):
    vet.append(vet[i-1] + vet[i-2])

print(vet)
```

```python
vet = [4,6,4,1,2,9,13]
tam = len(vet)
a = 0

for i in range(tam):    
    if(vet[i] % 2 == 0):
        a += vet[i]        
print(a)
```

```python
vet = [4,6,4,1,2,9,13]
tam = len(vet)
b = 0

for i in range(tam):    
    if((vet[i] + vet[tam-1-i]) % 2 == 0):
        b += vet[i]
print(b)
```

```python
def altera(a,b):    
    temp = a
    a = b
    b = temp

    return a,b

vet = [4,6,4,1,2,9,13]
tam = len(vet)
for i in range(tam):    
    m = i        
    for j in range(i,tam):
        if vet[j] > vet[m]:
            m = j

    vet[i],vet[m] = altera(vet[i],vet[m])

print(vet)        
```

```python
def func(n,vet):    
    ret = False    
    for i in range(len(vet)):
        if n == vet[i]:
            ret = True
    return ret        

vet = [1,2,3,1,3,5,8,9,10,5]
r = func(3,vet)
print(r)
```

```python
def func_3(vetor):    
    temp = vetor[0]
    tam = len(vetor)
    vetor[0] = vetor[tam-1]
    vetor[tam-1] = temp        
    return vetor

def func_2(a):
    a += 1
    b = a*2    
    return b

def func_1(vet):    
    for i in range(len(vet)):
        vet[i] = func_2(vet[i])        
    return vet    

vet = [1,2,3,4,5]
print(vet)

vet = func_11([4,5,6,7,8])
print(vet)

vet = func_3(vet)
print(vet)
```

```python
vet = [66,111,109,32,100,105,97]

for i in range(len(vet)):
    print(chr(vet[i]), end='')

print()
```

```python
def avalia(string):
    count = 0
    for char in string:
        ascii_value = ord(char)
        if 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
            count += 1
    return count

texto = "aB@c@dabra1234"
resultado = avalia(texto)
print(resultado)
```

```python
def modifica(string):
    count = 0
    new_str = ''
    for char in string:
        ascii_value = ord(char)
        if 65 <= ascii_value <= 90:
            new_str += chr(ascii_value + 32)
        elif 97 <= ascii_value <= 122:
            new_str += chr(ascii_value - 32)            
        else:
            new_str += char

    return new_str

texto = "Em 24/06/2023 fez UM belo DIA de Sol"
resultado = modifica(texto)
print(resultado)
```

**OBS**: Em teste de mesa, podem existir variações destes exercícios, no qual se pede para corrigir o código apresentado.

# 2. Implemente o que se pede

a. Crie um vetor com 1000 números aleatórios, no entanto pares . (Dica: fique sorteando números e so incluia se for par. Facilita utilizar um while() ao invés do for)

b. Adicione números ao vetor, até que a soma deles ultrapasse 100mil.

c. Dado um vetor de 100 posições, calcule a média dos elementos múltiplos de 5

d. Dado um vetor de N posições, cálcule a soma dos produtos, sendo o índice o fato de multiplicação. Exemplo:

    [9,2,3,7,19,.....] = 9x0 + 2x1 + 3x2, 7x3, 19x4 .....

e. Determine uma função que recebe um valor N e cria um vetor contendo a série de fibonacci até N.

    def **fibo**(n):

        ....    

        ....    

        return vet

    

f. Converta números binários em decimais. Considere a entrada do binário em formato texto. (Dica: É similar a soma dos opostos de um vetor)

        "1011" -> $1x2^3 + 0x2^2 + 1x2^1 + 1x2^0=  11$

        "10101" -> $1x2^4 + 0x2^3 + 1x2^2 + 0x2^1 + 1x2^0 = 21$



g. Encontre o maior elemento de um vetor. 

h. Ordene um vetor númerico

i. Ordene uma string qualquer: "casario" -> "aaciors"

j. Crie uma função que conta quantos digitos tem uma string

k. Imprima uma string em ordem crescente, exemplo : "casaco"

```
c
ca
cas
casa
casac
casaco
```

l. Crie um validador de senha, considerando que a senha deve ter 8 dígitos, sendo ao menos 3 caracteres maiusculos e três númericos

m. Uma senha númerica não pode conter sequências de três digitos, determine se a senha é válida:

    4578218 -> válido

    4568218 -> inválida (456)

    4587618-> inválida (876)

    Neste caso, implemente uma função que recebe três números e determine se estão em sequência.

n. Determine uma função que recebe um vetor e verifica se o vetor é ordenado (return 1) ou não (return 1). Na função principal, chame a função e avalie o retorno, imprimindo na tela ou não ordenado.

    

**OBS**: Para os casos de implementação, reveja também as listas de exercícios.
