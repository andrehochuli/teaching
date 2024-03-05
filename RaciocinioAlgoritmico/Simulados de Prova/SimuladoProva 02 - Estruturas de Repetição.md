# Simulado de Prova - Estruturas de Repetição

Este simulado contém questões similares às que serão cobradas na avaliação individual a ser realizada em sala de aula. Durante a avaliação, você deverá escrever suas respostas à mão, sem consultar ou receber ajuda do computador. O objetivo é avaliar suas habilidades e conhecimentos em lógica de programação.

Por isso, para que o simulado seja eficaz, recomendamos que você resolva as questões diretamente em uma folha de papel.

### 1. Testes de Mesa

a. Qual o resultado do print considerando R=10 , R=30 e R=50

```python
n = 85
i=0
soma = 0
r = int(input("Razao: "))


while (n < 100 and soma < 100):

  i += 1

  if i % 5 != 0: 
    n -= 1

  soma += r

print(n, i, soma)
```

b. Com relação ao código abaixo, marque a opção correta:

- Loop Infinito

- Soma x e y

- Imprime o intervalo entre x e y 
  
  ```python
  x = 10
  y = 30
  soma = 0
  
  while (soma < x*y or x < y):
  
      soma = y - x
      x += soma
      y -= soma    
  
  print(x, y, soma)
  ```

c. O que será impresso na tela para os inputs {a,b} sendo:

 a=10, b= 14

 a=0 , b = 10

 a=1003, b=1005

 a=20, b=10

 a= 0, b=1000

```python
a= ??
b= ??
r = 2

while (a < b and r < 50):
    print(a,b,r)
    a = a + 1
    b = b - 1
    r = r * r    
```

d. Apresente os valores de x e y para que os prints sejam executados, como se pede:

```python
n = 0
a = 0
b = 0
c = 0

while n <= 10:
    if n % 2 == 0:
        b += n
    else:
        c += n
    if n % 3 == 0:
        a += n
    n += 1

print("Saída 1: ", a)
print("Saída 2: ", b)
print("Saída 3: ", c)
```

### 2. Encontre os erros nas implementações abaixo:

Os erros podem ser lógicos ou de sintaxe    

**a. Imprima os números impares de 0 a 100:**

```python
soma_impares = 0
i = 0

while i < 100:
    if i % 2 == 1:
        soma_impares = soma_impares + i
    i = i + 2

print("A soma dos números ímpares entre 0 e 100 é: ", soma_impares)
```

**b. Imprima os números pares de 0 a 100:**

```python
soma_par = 2
i = 0

while i <= 100:
    if i % 2 == 0:
        soma_pares = soma_pares + i
        i = i + 1

print("A soma dos números pares entre 0 e 100 é: ", soma_pares)
```

**c. Soma os múltiplos de 4 e 8:  **

```python
i = 1
soma = 0

while i < 100:
    if i % 8 == 0 or i % 4 == 0:
      i = i + 1

    soma = soma + i


print("A soma dos números múltiplos de 4 e 8 simultaneos é: ", soma)
```

### 3. Implemente o que se pede

a. Escreva um programa que peça um número inteiro e exiba a sua tabuada de  
multiplicação de 1 a 10.

b. Escreva um programa que solicite um número inteiro e informe se ele é primo  
ou não.

c. Escreva um programa que solicite ao usuário um número e, em seguida, imprima todos os divisores de 2...9

d. Enquanto a soma não ultrapassar 10000, fique solicitando números ao usuário

e. Calcule o IMC (Índice de Massa Corporal), para pessoas variando de 60 a 90 kgs e altura de 1,60 a 1,90 metros. Considere incremento de 5 kgs para o peso, e 0,10 cm para a altura. Também informe em qual classe de IMC a pessoa se encontra

O cálculo do IMC é $IMC = \frac{peso}{altura^2}$, sendo 

- **Abaixo do peso:** IMC < 18,5
- **Normal:** 18,5 <= IMC < 25
- **Sobrepeso:** 25 <= IMC < 30
- **Obesidade:** IMC >= 30 
