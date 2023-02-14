# Aula 03 - Exercícios de Fixação

### 1. Implemente um seletor de canais para informar que canal a pessoa está assistindo, sendo:
	• 2 BANDEIRANTES 
	• 4 SBT 
	• 6 CNT 
	• 7 RECORD 
	• 9 CULTURA
	• 12 GLOBO 
	Informe uma mensagem caso um canal seja digitado errado.
Solução:
```
canal = int(input("Digite o número do canal que está assistindo: "))
if canal == 2:
    print("Você está assistindo o canal BANDEIRANTES.")
elif canal == 4:
    print("Você está assistindo o canal SBT.")
elif canal == 6:
    print("Você está assistindo o canal CNT.")
elif canal == 7:
    print("Você está assistindo o canal RECORD.")
elif canal == 9:
    print("Você está assistindo o canal CULTURA.")
elif canal == 12:
    print("Você está assistindo o canal GLOBO.")
else:
    print("Canal inválido. Por favor, digite um número de canal válido.")
```
	
### 2. Um estabelecimento, fornece uma comissão progressiva aos seus vendedores:
        a. 5%, para vendas até R$ 100,00
        b. 6% para vendas até R$ 500,00
        c. 7% para vendas até R$ 1000,00
        d. 8% para vendas acima de R$ 1000,00
	
	Implemente um algoritmo que calcule a comissão do vendedor.

Solução:
```
valor_vendas = float(input("Digite o valor das vendas: "))

if valor_vendas <= 100:
    comissao = valor_vendas * 0.05
elif valor_vendas <= 500:
    comissao = valor_vendas * 0.06
elif valor_vendas <= 1000:
    comissao = valor_vendas * 0.07
else:
    comissao = valor_vendas * 0.08

print(f"A comissão é de R${comissao:.2f}")

```
### 3. A partir de três notas de um aluno e informe o conceito a partir da média:
	Média de aproveitamento      Conceito
	Entre 9.0 e 10.0                A
	Entre 7.5 e 9.0                 B
	Entre 6.0 e 7.5                 C
	Entre 4.0 e 6.0                 D
	Entre 4.0 e zero                E

	Caso, o conceito seja abaixo de C, indique reprovado, caso contrário aprovado.

Solução:
```
print("Sistema de cálculo de conceito e situação de aprovação")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"

print("A média do aluno é: %.1f" % media)
print("O conceito do aluno é: %s" % conceito)

if media >= 6.0:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")

```
###  4. Informe o imposto a recolher de um salário, seguindo a tabela abaixo:
	      Salário			 IRPF
	Até R$1.903,98			Isento
	De R$1.903,99 até R$2.826,65	7,5%
	De R$2.826,66 até R$3.751,05	15%	
	De R$3.751,06 até R$4.664,68	22,5%

Solução:
```
print("Calculadora de imposto de renda (IRPF)")
salario = float(input("Informe o salário: R$"))

if salario <= 1903.98:
    print("Você está isento de imposto de renda.")
else:
    if salario <= 2826.65:
        irpf = salario * 0.075
    elif salario <= 3751.05:
        irpf = salario * 0.15
    elif salario <= 4664.68:
        irpf = salario * 0.225
    else:
        irpf = salario * 0.275

    print("O valor do imposto a recolher é: R$%.2f" % irpf)

```
### 5. Escreva um programa Python que ordena três números em ordem crescente.

Solução 1:
```
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if (num1 <= num2 and num2 <= num3):
	print("Os números em ordem crescente são:", num1, num2, num3);
elif (num1 <= num3 and num3 <= num2):
	print("Os números em ordem crescente são:", num1, num3, num2);
elif (num2 <= num1 and num1 <= num3):
	print("Os números em ordem crescente são:", num2, num1, num3);
elif (num2 <= num3 and num3 <= num1):
	print("Os números em ordem crescent são:", num2, num3, num1);
elif (num3 <= num1 and num1 <= num2):
	print("Os números em ordem crescente são:", num3, num1, num2);
else:
	print("Os números em ordem crescente são:", num3, num2, num1);
```

Solução 2:
```
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num2 < num1 and num2 < num3:
  aux = num1;
  num1 = num2;
  num2 = aux;

if num3 < num1:
  aux = num1;
  num1 = num3;
  num3 = aux;

if num3 < num2:
  aux = num2;
  num2 = num3;
  num3 = aux;

print("Os números em ordem crescente são:", num1, num2, num3);

```
Discuta: Porque precisamos de uma variavel 'aux' para realizar a troca de valores?

### 6. Escreva um programa Python que simula um jogo de pedra-papel-tesoura entre dois jogadores.

Solução:
```
jogador1 = input("Jogador 1: escolha pedra, papel ou tesoura: ")
jogador2 = input("Jogador 2: escolha pedra, papel ou tesoura: ")
if jogador1 == jogador2:
    print("Empate!")
elif jogador1 == "pedra":
    if jogador2 == "tesoura":
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")
elif jogador1 == "papel":
    if jogador2 == "pedra":
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")
else:
    if jogador2 == "papel":
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")

```

### 7. Detetive: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

	• Telefonou para a vítima? [S/N]
	• Esteve no local do crime? [S/N]
	• Mora perto da vítima? [S/N]
	• Tinha algum dívida com a vítima? [S/N]
	• Já trabalhou com a vítima? [S/N]

	O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
	Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”.
	Entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. 
	Caso contrário, ele será classificado como “Inocente“. 

Solução:
```
print("Bem-vindo ao jogo Detetive!")
print("Você é um detetive encarregado de investigar um crime. Sua missão é fazer perguntas para determinar a classificação da pessoa no crime.")

# Fazer as perguntas
pergunta1 = "Telefonou para a vítima? [S/N] "
resposta1 = input(pergunta1)
pergunta2 = "Esteve no local do crime? [S/N] "
resposta2 = input(pergunta2)
pergunta3 = "Mora perto da vítima? [S/N] "
resposta3 = input(pergunta3)
pergunta4 = "Devia para a vítima? [S/N] "
resposta4 = input(pergunta4)
pergunta5 = "Já trabalhou com a vítima? [S/N] "
resposta5 = input(pergunta5)

# Determinar a classificação
respostas_positivas = 0
if resposta1 == "S":
    respostas_positivas += 1
if resposta2 == "S":
    respostas_positivas += 1
if resposta3 == "S":
    respostas_positivas += 1
if resposta4 == "S":
    respostas_positivas += 1
if resposta5 == "S":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("\nA pessoa é suspeita.")
elif respostas_positivas >= 3 and respostas_positivas <= 4:
    print("\nA pessoa é cúmplice.")
elif respostas_positivas == 5:
    print("\nA pessoa é o assassino.")
else:
    print("\nA pessoa é inocente.")
```

### 8. Elabore um sistema que recomende o tipo de roupa para um evento:

	• O evento é profissional ou lazer?
	• É com amigos ou família?
	• Faz calor ou frio?
	• O evento é em uma cachara, cidade ?
	• O local fechado ou aberto?
    
	Baseado nestas respostas, criar uma estrutura de seleção capaz de indicar desde um terno até bermuda e calção. 	
	Fique livre para propor mais perguntas ou até mesmo outro sistema de recomendação (viagem, esporte, filme, musica, etc) 
	
Solução:
```
print("Bem-vindo ao sistema de recomendação de roupa!")
print("Responda às perguntas abaixo para que possamos recomendar uma roupa adequada para você.")

# Fazer as perguntas
pergunta1 = "O evento é profissional ou lazer? [S/N]"
resposta1 = input(pergunta1)
pergunta2 = "É com amigos ou família? [S/N]"
resposta2 = input(pergunta2)
pergunta3 = "Faz calor ou frio? [S/N]"
resposta3 = input(pergunta3)
pergunta4 = "O evento é em uma cidade ou no campo? [S/N]"
resposta4 = input(pergunta4)
pergunta5 = "O local é fechado ou aberto? [S/N]"
resposta5 = input(pergunta5)

# Determinar a recomendação
if resposta1 == "profissional":
    if resposta3 == "frio":
        print("\nRecomendamos que você use um terno ou um vestido formal.")
    else:
        print("\nRecomendamos que você use uma roupa social, como calça social e camisa.")
elif resposta2 == "família":
    if resposta3 == "frio":
        print("\nRecomendamos que você use um suéter ou uma jaqueta com calça jeans.")
    else:
        print("\nRecomendamos que você use uma roupa casual, como camiseta e shorts.")
else:
    if resposta3 == "frio":
        print("\nRecomendamos que você use uma jaqueta e calça.")
    else:
        print("\nRecomendamos que você use uma roupa confortável, como t-shirt e shorts.")
```



