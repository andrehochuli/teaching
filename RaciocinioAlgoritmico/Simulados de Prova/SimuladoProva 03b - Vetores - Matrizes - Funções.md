# Simulado de Prova - Vetores, Matrizes e Funções

Este simulado contém questões similares às que serão cobradas na avaliação individual a ser realizada em sala de aula. Durante a avaliação, você deverá escrever suas respostas à mão, sem consultar ou receber ajuda do computador. O objetivo é avaliar suas habilidades e conhecimentos em lógica de programação.

Por isso, para que o simulado seja eficaz, recomendamos que você resolva as questões diretamente em uma folha de papel.

As listas de exercícios realizadas ao longo das aulas também é uma excelente base de estudo.

# 3. Funções e Recursão

As questões a seguir avaliam a compreensão sobre criação de funções, passagem de parâmetros, retorno de valores, chamadas sucessivas e recursão. Em todos os exercícios, escreva o código à mão e evite utilizar funções prontas da linguagem, exceto quando indicado.

---

## 3.1 Testes de Mesa com Funções

a. Qual valor será impresso na tela?

```python
def soma(a, b):
    return a + b

def dobro(x):
    return x * 2

x = soma(3, 4)
y = dobro(x)
print(y)
```

---

b. Qual valor será impresso na tela?

```python
def altera(x):
    x = x + 10
    return x

a = 5
b = altera(a)

print(a)
print(b)
```

---

c. Qual será o conteúdo do vetor ao final da execução?

```python
def modifica(vet):
    for i in range(len(vet)):
        vet[i] = vet[i] * 2

v = [1, 2, 3, 4]
modifica(v)

print(v)
```

---

d. Qual será o valor impresso?

```python
def calcula(vet):
    soma = 0

    for i in range(len(vet)):
        if vet[i] % 2 == 0:
            soma += vet[i]

    return soma

v = [3, 6, 1, 8, 5, 10]
r = calcula(v)

print(r)
```

---

e. Qual será o valor impresso?

```python
def func(a, b):
    if a > b:
        return a - b
    else:
        return b - a

x = func(10, 4)
y = func(3, 9)

print(x + y)
```

---

f. Qual será o conteúdo do vetor impresso?

```python
def troca(vet, i, j):
    aux = vet[i]
    vet[i] = vet[j]
    vet[j] = aux

v = [10, 20, 30, 40]

troca(v, 0, 3)
troca(v, 1, 2)

print(v)
```

---

g. Qual será o valor impresso?

```python
def conta(vet, valor):
    c = 0

    for i in range(len(vet)):
        if vet[i] == valor:
            c += 1

    return c

v = [2, 3, 2, 5, 2, 7, 3]
print(conta(v, 2))
```

---

h. Qual será o valor impresso?

```python
def maior(a, b):
    if a > b:
        return a
    return b

def avalia(vet):
    m = vet[0]

    for i in range(1, len(vet)):
        m = maior(m, vet[i])

    return m

v = [4, 9, 1, 12, 3]
print(avalia(v))
```

---

## 3.2 Testes de Mesa com Recursão

a. Qual valor será impresso?

```python
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)

print(f(5))
```

---

b. Qual valor será impresso?

```python
def fat(n):
    if n == 0:
        return 1
    return n * fat(n - 1)

print(fat(4))
```

---

c. Qual valor será impresso?

```python
def func(n):
    if n == 1:
        return 1
    return 2 * func(n - 1)

print(func(5))
```

---

d. Qual será a saída?

```python
def imprime(n):
    if n == 0:
        return

    print(n)
    imprime(n - 1)

imprime(4)
```

---

e. Qual será a saída?

```python
def imprime(n):
    if n == 0:
        return

    imprime(n - 1)
    print(n)

imprime(4)
```

---

f. Qual valor será impresso?

```python
def soma_vetor(vet, i):
    if i == len(vet):
        return 0

    return vet[i] + soma_vetor(vet, i + 1)

v = [2, 4, 6, 8]
print(soma_vetor(v, 0))
```

---

g. Qual valor será impresso?

```python
def conta_pares(vet, i):
    if i == len(vet):
        return 0

    if vet[i] % 2 == 0:
        return 1 + conta_pares(vet, i + 1)
    else:
        return conta_pares(vet, i + 1)

v = [1, 4, 7, 8, 10, 13]
print(conta_pares(v, 0))
```

---

h. Qual valor será impresso?

```python
def potencia(base, exp):
    if exp == 0:
        return 1

    return base * potencia(base, exp - 1)

print(potencia(2, 5))
```

---

## 3.3 Implemente Funções

a. Crie uma função que recebe dois números inteiros e retorna o maior deles.

```python
def maior(a, b):
    ...
```

---

b. Crie uma função que recebe um vetor e retorna a soma de todos os elementos.

```python
def soma_vetor(vet):
    ...
```

---

c. Crie uma função que recebe um vetor e retorna a quantidade de números pares.

```python
def conta_pares(vet):
    ...
```

---

d. Crie uma função que recebe uma string e retorna a quantidade de letras maiúsculas.

```python
def conta_maiusculas(texto):
    ...
```

---

e. Crie uma função que recebe uma string e retorna a quantidade de dígitos numéricos.

```python
def conta_digitos(texto):
    ...
```

---

f. Crie uma função que recebe um vetor e retorna o maior elemento.

```python
def maior_vetor(vet):
    ...
```

---

g. Crie uma função que recebe um vetor e retorna o menor elemento.

```python
def menor_vetor(vet):
    ...
```

---

h. Crie uma função que recebe um vetor e um valor, retornando `True` caso o valor exista no vetor e `False` caso contrário.

```python
def existe(vet, valor):
    ...
```

---

i. Crie uma função que recebe um vetor e retorna um novo vetor contendo apenas os números pares.

```python
def filtra_pares(vet):
    ...
```

---

j. Crie uma função que recebe um vetor e retorna um novo vetor invertido.

```python
def inverte(vet):
    ...
```

---

k. Crie uma função que recebe uma string e retorna uma nova string invertida.

```python
def inverte_string(texto):
    ...
```

---

l. Crie uma função que recebe uma string e verifica se ela é um palíndromo.

Exemplos:

```python
"arara" -> True
"casa"  -> False
```

```python
def palindromo(texto):
    ...
```

---

m. Crie uma função que recebe uma string e retorna quantas vogais ela possui.

```python
def conta_vogais(texto):
    ...
```

---

n. Crie uma função que recebe um vetor e retorna `True` se ele estiver ordenado em ordem crescente. Caso contrário, retorna `False`.

```python
def esta_ordenado(vet):
    ...
```

---

o. Crie uma função que recebe uma matriz e retorna a soma de todos os seus elementos.

```python
def soma_matriz(mat):
    ...
```

---

p. Crie uma função que recebe uma matriz quadrada e retorna a soma da diagonal principal.

```python
def soma_diagonal_principal(mat):
    ...
```

---

q. Crie uma função que recebe uma matriz quadrada e retorna a soma da diagonal secundária.

```python
def soma_diagonal_secundaria(mat):
    ...
```

---

r. Crie uma função que recebe uma matriz e retorna o maior elemento da matriz.

```python
def maior_matriz(mat):
    ...
```

---

s. Crie uma função que recebe dois vetores de mesmo tamanho e retorna um terceiro vetor com a soma posição a posição.

Exemplo:

```python
[1, 2, 3]
[4, 5, 6]

resultado -> [5, 7, 9]
```

```python
def soma_vetores(a, b):
    ...
```

---

t. Crie uma função que recebe uma string e retorna uma nova string contendo apenas os caracteres alfabéticos.

Exemplo:

```python
"a1b2@c" -> "abc"
```

```python
def somente_letras(texto):
    ...
```

---

## 3.4 Implemente Funções Recursivas

a. Crie uma função recursiva que recebe um número inteiro `n` e retorna a soma de `1` até `n`.

Exemplo:

```python
soma_rec(5) -> 15
```

```python
def soma_rec(n):
    ...
```

---

b. Crie uma função recursiva que calcula o fatorial de um número.

Exemplo:

```python
fatorial(5) -> 120
```

```python
def fatorial(n):
    ...
```

---

c. Crie uma função recursiva que calcula a potência de um número.

Exemplo:

```python
potencia(2, 4) -> 16
```

```python
def potencia(base, exp):
    ...
```

---

d. Crie uma função recursiva que recebe um vetor e um índice inicial, retornando a soma dos elementos do vetor.

```python
def soma_vetor_rec(vet, i):
    ...
```

---

e. Crie uma função recursiva que recebe um vetor e um índice inicial, retornando a quantidade de números pares.

```python
def conta_pares_rec(vet, i):
    ...
```

---

f. Crie uma função recursiva que recebe uma string e um índice inicial, retornando a quantidade de dígitos numéricos.

```python
def conta_digitos_rec(texto, i):
    ...
```

---

g. Crie uma função recursiva que recebe uma string e imprime seus caracteres na ordem original.

Exemplo:

```python
"casa"

c
a
s
a
```

```python
def imprime_string(texto, i):
    ...
```

---

h. Crie uma função recursiva que recebe uma string e imprime seus caracteres em ordem inversa.

Exemplo:

```python
"casa"

a
s
a
c
```

```python
def imprime_inverso(texto, i):
    ...
```

---

i. Crie uma função recursiva que recebe um vetor e retorna o maior elemento.

```python
def maior_rec(vet, i):
    ...
```

---

j. Crie uma função recursiva que recebe um vetor, um índice inicial e um valor, retornando `True` se o valor existir no vetor e `False` caso contrário.

```python
def existe_rec(vet, i, valor):
    ...
```

---

k. Crie uma função recursiva que recebe um número inteiro e retorna a soma dos seus dígitos.

Exemplo:

```python
soma_digitos(472) -> 13
```

```python
def soma_digitos(n):
    ...
```

---

l. Crie uma função recursiva que recebe um número inteiro e retorna a quantidade de dígitos.

Exemplo:

```python
conta_digitos_num(4729) -> 4
```

```python
def conta_digitos_num(n):
    ...
```

---

m. Crie uma função recursiva que recebe um número inteiro e retorna seu valor invertido.

Exemplo:

```python
inverte_numero(1234) -> 4321
```

Sugestão: utilizar um segundo parâmetro acumulador.

```python
def inverte_numero(n, invertido):
    ...
```

---

n. Crie uma função recursiva que recebe uma string e verifica se ela é um palíndromo.

Exemplo:

```python
palindromo_rec("arara", 0, 4) -> True
palindromo_rec("casa", 0, 3)  -> False
```

```python
def palindromo_rec(texto, ini, fim):
    ...
```

---

o. Crie uma função recursiva que calcula o n-ésimo termo da sequência de Fibonacci.

Considere:

```python
fib(0) -> 0
fib(1) -> 1
fib(2) -> 1
fib(3) -> 2
fib(4) -> 3
fib(5) -> 5
```

```python
def fib(n):
    ...
```

---

## 3.5 Corrija os Códigos

a. O código abaixo deveria retornar a soma dos elementos do vetor, mas contém erro. Corrija.

```python
def soma(vet):
    total = 0

    for i in range(len(vet)):
        total = vet[i]

    return total
```

---

b. O código abaixo deveria retornar o maior elemento do vetor, mas contém erro. Corrija.

```python
def maior(vet):
    m = 0

    for i in range(len(vet)):
        if vet[i] > m:
            m = vet[i]

    return m
```

---

c. O código abaixo deveria verificar se um valor existe no vetor, mas contém erro. Corrija.

```python
def existe(vet, valor):
    for i in range(len(vet)):
        if vet[i] == valor:
            return True
        else:
            return False
```

---

d. O código abaixo deveria calcular o fatorial recursivamente, mas contém erro. Corrija.

```python
def fatorial(n):
    return n * fatorial(n - 1)
```

---

e. O código abaixo deveria somar os elementos do vetor recursivamente, mas contém erro. Corrija.

```python
def soma_rec(vet, i):
    return vet[i] + soma_rec(vet, i + 1)
```

---

f. O código abaixo deveria imprimir os números de `n` até `1`, mas contém erro. Corrija.

```python
def imprime(n):
    if n == 0:
        print(n)
    imprime(n - 1)
```

---

g. O código abaixo deveria contar quantos números pares existem no vetor, mas contém erro. Corrija.

```python
def pares(vet):
    c = 0

    for i in range(len(vet)):
        if vet[i] % 2 == 0:
            c = 1

    return c
```

---

h. O código abaixo deveria retornar `True` se a string possui apenas dígitos, mas contém erro. Corrija.

```python
def somente_digitos(texto):
    for c in texto:
        if c >= '0' and c <= '9':
            return True
        else:
            return False
```

---

## 3.6 Desafios Integradores

a. Crie uma função que recebe uma senha e verifica se ela é válida. A senha deve atender aos seguintes critérios:

* possuir pelo menos 8 caracteres;
* possuir pelo menos 2 letras maiúsculas;
* possuir pelo menos 2 letras minúsculas;
* possuir pelo menos 2 dígitos numéricos;
* não possuir espaço em branco.

```python
def valida_senha(senha):
    ...
```

---

b. Crie uma função que recebe um vetor de números inteiros e retorna uma matriz de frequência.

Exemplo:

```python
[1, 2, 1, 3, 2, 1]

resultado -> [[1, 3], [2, 2], [3, 1]]
```

```python
def frequencia(vet):
    ...
```

---

c. Crie uma função que recebe um texto e retorna uma matriz contendo a frequência de cada caractere alfabético, ignorando números e símbolos.

Exemplo:

```python
"banana!"

resultado -> [['b', 1], ['a', 3], ['n', 2]]
```

```python
def frequencia_letras(texto):
    ...
```

---

d. Crie uma função que recebe uma matriz e retorna um vetor contendo a soma de cada linha.

Exemplo:

```python
[[1, 2, 3],
 [4, 5, 6]]

resultado -> [6, 15]
```

```python
def soma_linhas(mat):
    ...
```

---

e. Crie uma função que recebe uma matriz e retorna um vetor contendo a soma de cada coluna.

Exemplo:

```python
[[1, 2, 3],
 [4, 5, 6]]

resultado -> [5, 7, 9]
```

```python
def soma_colunas(mat):
    ...
```

---

f. Crie uma função que recebe uma matriz quadrada e verifica se ela é uma matriz identidade.

Exemplo:

```python
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]

resultado -> True
```

```python
def identidade(mat):
    ...
```

---

g. Crie uma função recursiva que recebe um vetor e verifica se ele está ordenado em ordem crescente.

```python
def ordenado_rec(vet, i):
    ...
```

---

h. Crie uma função recursiva que recebe uma string e retorna uma nova string invertida.

```python
def inverte_string_rec(texto, i):
    ...
```

---

i. Crie uma função recursiva que recebe um número inteiro positivo e verifica se todos os seus dígitos são pares.

Exemplo:

```python
2468 -> True
2438 -> False
```

```python
def todos_digitos_pares(n):
    ...
```

---

j. Crie uma função recursiva que recebe um número inteiro positivo e verifica se ele possui algum dígito igual a zero.

Exemplo:

```python
1205 -> True
1235 -> False
```

```python
def possui_zero(n):
    ...
```

---

**OBS**: Nas questões de recursão, lembre-se de definir claramente:

1. o caso base;
2. o passo recursivo;
3. o valor retornado em cada situação.

