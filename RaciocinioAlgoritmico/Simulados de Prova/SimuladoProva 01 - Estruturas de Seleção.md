# Simulado de Prova - Estruturas de Seleção

Este simulado contém questões similares às que serão cobradas na avaliação individual a ser realizada em sala de aula. Durante a avaliação, você deverá escrever suas respostas à mão, sem consultar ou receber ajuda do computador. O objetivo é avaliar suas habilidades e conhecimentos em lógica de programação.

Por isso, para que o simulado seja eficaz, recomendamos que você resolva as questões diretamente em uma folha de papel.

### 1. Testes de Mesa

a. Qual o resultado do print para as entradas {4 , 7,  -9, -5}

```python
num = int(input("Digite um número inteiro: "))

if num > 0:
    if num % 2 == 0:
        resultado = num / 2
    else:
        resultado = num * 3

elif num == 0:
    resultado = 0
else:
    if num % 3 == 0:
        resultado = num ** 2
    else:
        resultado = num * -1


print(f'Resultado == {resultado}')
```

b. Qual o resultado do print, considerando os input's de (x,y) sendo:

- (x=10,y=10)

- (x=15,y=15)

- (x=-10,y=-5)

- (x=0,y=-60)

 

```python
x = int(input("Digite um número: "))
y = int(input("Digite um número: "))

result = 0

if x > 10 and y < 30 or x < 0:
  result = x + y

elif y < 0 and (x > 0 or (x+y) > 20):
  result = y * (-1) + x**2

print(result)
```

c. O que será impresso na tela para os inputs: 3, 5, 8, 10, 13, 15, 25

```python
x = int(input("Digite um número: "))
res = 1

if x < 15:
  print("Menor que 15")
  res = x * 1

if x < 10:
  print("Menor que 10")
  res = x * 2

if x < 5:
  print("Menor que 5")
  res = x * 3

print(res)  
```

d. O que será impresso na tela para os inputs: 3, 5, 8, 10, 13, 15, 25:

```python
x = int(input("Digite um número: "))
res = 1

if x < 15:
  print("Menor que 15")
  res = x * 1

elif x < 10:
  print("Menor que 10")
  res = x * 2

elif x < 5:
  print("Menor que 5")
  res = x * 3

print(res)  
```

e. O que será impresso na tela para os inputs:  3, 5, 8, 10, 13, 15, 25:

```python
x = int(input("Digite um número: "))

res = 1
if x < 5:
  print("Menor que 5")
  res = x * 3

elif x < 10:
  print("Menor que 10")
  res = x * 2

elif x < 15:
  print("Menor que 15")
  res = x * 1

print(res)  
```

f. Apresente os valores de x e y para que os prints sejam executados, como se pede:

```python
if x == 0 and y % 3 != 0:
    print("Situação A")

elif x > 50 and y % 2 == 0:
    print("Situação B")

elif x > 10 and y < 20 or y % 5 == 0:
    print("Situação C")

elif x % 10 == 0 and y % 4 == 0 and y > 24:
    print("Situação D")
```

x = ******____****** , y = __ para "Situação A"

x = ******____****** , y = __ para "Situação B"

x = ******____****** , y = __ para "Situação C"

x = ******____****** , y = __ para "Situação D"

g. Qual o valor de 'a' e 'b' ao final do algoritmo?

```python
a = 10
b = 20

temp = a
a=b
b=temp

print(a,b)
```

### 2. Encontre os erros nas implementações abaixo:

Os erros podem ser lógicos ou de sintaxe    

**a. Determine se um número é positivo ou negativo:**

```python
if num < 0:
    print(Positivo)
else:
    print("Negativo")
else:
    print("Zero")
```

**b. Determine se dois números são iguais:**

```python
if a = b:
    print("Iguais")
else:
    print("Diferentes")
```

**c. Calcula o reajuste da gasolina e informa o novo valor**

```python
valor_atual = input("Digite o valor da gasolina: ")
reajuste = input("Percentual de reajuste: ")
valor_reajustado == valor_atual * reajuste
print("Novo valor da gasolina: ", valor_reajuste)
```

**d. Login para username 'João' e senha 1234:**

```python
username = input("Nome de Usuario: ")
senha = float(input("Digite sua senha: ")

username_correto = 'João'
senha_correta = '1234'

if username = 'João' or senha_correta = '1234':
    print("Login Efetuado")


print("Login Falhou")
```

### 3. Implemente o que se pede

a. Implemente um jogo de dupla de par ou impar

b. Determine se um número é positivo ou negativo

c. Escreva um programa que receba o ano de nascimento e determine se ela pode dirigir (maior que 18 anos)

d. Escreva um programa que receba um número e verifique se ele é divisível por 3 ou por 5.

e. Escreva um programa que ordena três números em ordem crescente.

f. Escreva um programa que receba duas notas e calcule a média aritmética. Se a média for maior ou igual a 7, imprima "Aprovado". Se a média for menor que 7 e maior ou igual a 5, imprima "Recuperação". Caso contrário, imprima "Reprovado".

g. Escreva um programa que receba o valor da altura e do peso de uma pessoa e calcule o seu índice de massa corporal (IMC). Se o IMC for menor que 18,5, imprima "Abaixo do peso". Se o IMC for maior ou igual a 18,5 e menor que 25, imprima "Peso normal". Se o IMC for maior ou igual a 25 e menor que 30, imprima "Acima do peso". Se o IMC for maior ou igual a 30, imprima "Obeso".

h. d. Informe o imposto a recolher de um salário, seguindo a tabela abaixo:**

```
      Salário             IRPF
Até R$1.903,98            Isento
De R$1.903,99 até R$2.826,65    7,5%
De R$2.826,66 até R$3.751,05    15%    
De R$3.751,06 até R$4.664,68    22,5%
```

i. A partir de três notas de um aluno e informe o conceito a partir da média:**

```
Média de aproveitamento      Conceito
Entre 9.0 e 10.0                A
Entre 7.5 e 9.0                 B
Entre 6.0 e 7.5                 C
Entre 4.0 e 6.0                 D
Entre 4.0 e zero                E

Caso, o conceito seja abaixo de C, indique reprovado, caso contrário aprovado.
```

j. Calcule o frete dada as seguintes condições:**

- Para compras até R$ 100,00 reais, o frete é 10% do valor do produto

- Para compras acima de R$ 100,00 o frete é gratis, se o volume não ultrapassar a franquia de 1m3 e 3 KGs

- Para os demais casos, o frete custa 25 reais a cada m3 ou KG (o que for mais caro).
