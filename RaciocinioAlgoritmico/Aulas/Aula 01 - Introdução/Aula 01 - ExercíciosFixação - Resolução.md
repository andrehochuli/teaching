# Aula 01 - Exercícios de Fixação

### 1 - Calcule a soma de dois números
```
num1 = 10
num2 = 20

soma = num1 + num2

print("A soma de ",num1, " com ", num2, " é igual a: ", soma)
```

### 2 - Calcule o antecessor e o sucessor de um número 
```
num = 10

# Antecessor
antecessor = num - 1

# Sucessor
sucessor = num + 1

# Exibir o resultado
print("Antecessor:", antecessor)
print("Sucessor:", sucessor)

```

### 3 - Calcular o troco de uma compra 
```
valor_compra = 232.75
valor_pago = 250.00
troco = valor_pago - valor_compra

print("O troco é de: ", troco)
```

### 4 - Calcule a gorjeta de um garçom (10%)
```
valor_conta = 325.50
gorjeta = valor_conta * 0.1

print("O Garçom receberá: ", gorjeta)
```

### 5 - Calcule a metragem quadrada de uma área qualquer (casa, terreno, quarto, sala, etc)
```
comprimento = 30.57
largura = 65.21

area = comprimento * largura

print("A área é de", area,"metros quadrados")
```

### 6 - Calcule a metragem quadrada de uma casa com 3 pavimentos
```
comprimento = 12.5
largura = 5.35
area = comprimento * largura * 3
print("A casa tem", area, "metros quadrados")

```
### 7 - Calcule a média de idade de 5 pessoas
```
idade1 = 25
idade2 = 30
idade3 = 35
idade4 = 40
idade5 = 45
media = (idade1 + idade2 + idade3 + idade4 + idade5) / 5
print("A média de idade é de", media ,"anos")
```

### 8 - Calcule a idade a partir do ano de nascimento
  * Em anos 
  ```
  ano_nascimento = 1983
  ano_atual = 2023
  idade_em_anos = ano_atual - ano_nascimento
  
  print("A idade em anos é de", idade_em_anos, "anos")  
  ```
  
  * Em meses
  ```
  ano_nascimento = 1983
  ano_atual = 2023
  idade_em_anos = ano_atual - ano_nascimento
  idade_em_meses = idade_em_anos * 12
  
  print("A idade em meses é de", idade_em_meses, "meses")
  ```
  
  * Em dias
  ```
  ano_nascimento = 1983
  ano_atual = 2023
  idade_em_anos = ano_atual - ano_nascimento
  idade_em_dias = idade_em_anos * 365
  
  print("A idade em dias é de", idade_em_dias, "dias")
  ```
  
  * Tudo junto!
  ```
  ano_nascimento = 1983
  ano_atual = 2023

  idade_em_anos = ano_atual - ano_nascimento
  print("A idade em anos é de", idade_em_anos, "anos")

  idade_em_meses = idade_em_anos * 12
  print("A idade em meses é de", idade_em_meses, "meses")

  idade_em_dias = idade_em_anos * 365
  print("A idade em dias é de", idade_em_dias, "dias")
  ```


## Generalização dos Exercícios #4 e #5 

## 9 - Calcular a gorjeta de N% 
```
valor_conta = 325.50
perc_gorjeta = 0.1 #10%
gorjeta = valor_conta * perc_gorjeta

print("O Garçom receberá: ", gorjeta)
```

## 10 - Calcule a metragem quadrada de uma casa com N pavimentos 
```
comprimento = 12.5
largura = 5.35
pavimentos = 3
area = comprimento * largura * pavimentos
print("A casa tem", area, "metros quadrados")

```


