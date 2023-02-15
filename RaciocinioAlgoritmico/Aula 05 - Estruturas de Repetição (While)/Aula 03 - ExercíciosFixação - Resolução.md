# Aula 05 - Exercícios de Fixação

### 1. Escreva um programa que exiba os múltiplos de 3 de 0 a 100.
```
i = 0
while i <= 100:
    if i % 3 == 0:
        print(i)
    i += 1
```

### 2. Escreva um programa que faça a contagem regressiva de 10 a 0.
```
i = 10
while i >= 0:
    print(i)
    i -= 1
```

### 3. Escreva um programa que calcule a soma dos números ímpares de 1 a 100.
```
soma = 0
i = 1

while i <= 100:
    if i % 2 != 0:
        soma += i
    i += 1

print(f"A soma dos números ímpares de 1 a 100 é {soma}")
```

### 4. Escreva um programa que gere um número aleatório entre 1 e 100 e peça para o usuário adivinhá-lo.
```
import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1
    if tentativa == numero:
        print(f"Parabéns, você acertou em {tentativas} tentativas!")
        break
    elif tentativa < numero:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
```

### 5. Escreva um programa que peça um número inteiro e exiba a sua tabuada de multiplicação de 1 a 10.

```
n = int(input("Digite um número inteiro: "))
i = 1

while i <= 10:
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
    i += 1
```    
### 6. Escreva um programa que solicite um número inteiro e calcule a soma de seus dígitos.
```
numero = int(input("Digite um número inteiro: "))
soma = 0

while numero > 0:
    resto = numero % 10
    soma += resto
    numero = numero // 10

print(f"A soma dos dígitos é {soma}")
```

### 7. Escreva um programa que imprima os n primeiros números da sequência de Fibonacci.
```
n = int(input("Digite o número de elementos da sequência de Fibonacci: "))
anterior = 0
atual = 1
i = 1

while i <= n:
    print(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    i += 1
```

### 8. Escreva um programa que solicite um número inteiro e informe se ele é primo ou não.
```
numero = int(input("Digite um número inteiro: "))
i = 2

while i < numero:
    if numero % i == 0:
        print(f"{numero} não é um número primo.")
        break
    i += 1
else:
    print(f"{numero} é um número primo.")
```

### 9. Escreva um programa que exiba uma tabela de conversão de graus Celsius para Fahrenheit, de -10 até 100 celsius.
```
celsius = -10

while celsius <= 100:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} °C = {fahrenheit} °F")
    celsius += 10
```


### 10. Escreva um programa que gere um número aleatório entre 1 e 100 e peça para o usuário adivinhá-lo em até 5 tentativas.
```
import random

numero = random.randint(1, 100)
tentativas = 0

while tentativas < 5:
    tentativa = int(input("Adivinhe o número (entre 1 e 100): "))
    tentativas += 1
    if tentativa == numero:
        print(f"Parabéns, você acertou em {tentativas} tentativas!")
        break
    elif tentativa < numero:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
else:
    print(f"Você não conseguiu adivinhar o número em 5 tentativas. O número era {numero}.")
```
### 11. Você deve implementar um sistema de votação. A eleição deve ser decidida entre dois candidatos: "Joao da Silva - 28765"  "Carlos Alberto - 32928"). Faça um algoritmo que fique computando os votos até que a opção "ENCERRAR" seja digitada. Apresente também a opção de mostrar resultados parciais.
```jose_votos = 0
carlos_votos = 0

while True:
    print("Digite o número do candidato que deseja votar:")
    print("28765 - Joao da Silva")
    print("32928 - Carlos Alberto")
    print("Digite ENCERRAR para encerrar a votação")
    print("Digite RESULTADO para ver o resultado parcial da votação")
    voto = input()

    if voto == "ENCERRAR":
        break

    if voto == "RESULTADO":
        print("Resultado parcial da votação:")
        print("Joao da Silva: " + str(jose_votos) + " votos")
        print("Carlos Alberto: " + str(carlos_votos) + " votos")
    elif voto == "28765":
        jose_votos += 1
        print("Voto registrado para Joao da Silva")
    elif voto == "32928":
        carlos_votos += 1
        print("Voto registrado para Carlos Alberto")
    else:
        print("Opção inválida. Tente novamente.")

print("Resultado final da votação:")
print("Joao da Silva: " + str(jose_votos) + " votos")
print("Carlos Alberto: " + str(carlos_votos) + " votos")
if jose_votos > carlos_votos:
    print("Joao da Silva foi eleito.")
elif carlos_votos > jose_votos:
    print("Carlos Alberto foi eleito.")
else:
    print("Houve empate na votação.")
```
