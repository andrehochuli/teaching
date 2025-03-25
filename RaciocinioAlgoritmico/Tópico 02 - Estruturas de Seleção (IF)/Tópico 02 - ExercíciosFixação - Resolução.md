# Tópico 02 - Exercícios de Fixação

### 1. Informe se uma pessoa tem o mesmo nome que você

```
nome_pessoa = input("Informe o nome da pessoa: ")
seu_nome = input("Informe seu nome: ")

if nome_pessoa == seu_nome:
    print("A pessoa tem o mesmo nome que você")
else:
    print("A pessoa não tem o mesmo nome que você")
```

### 2. Informe se a pessoa digitou uma vogal ou consoante

```
letra = input("Digite uma letra: ")


if letra == "a" or letra == "e" or letra == "i" \
    or letra == "o" or letra == "u" or letra == "A"\
        or letra == "E" or letra == "I" or letra == "O"\
            or letra == "U":

    print("A letra digitada é uma vogal")

else:
    print("A letra digitada é uma consoante")
```

### 3. Informe o dia da semana a partir de um número entre 1 e 7. Exemplo, 1- Domingo, 2- Segunda etc. Se digitar outro valor deve aparecer “valor inválido”)

```
dia = int(input("Digite um número entre 1 e 7: "))

if dia == 1:
    print("Domingo")

if dia == 2:
    print("Segunda")

if dia == 3:
    print("Terça")

if dia == 4:
    print("Quarta")

if dia == 5:
    print("Quinta")

if dia == 6:
    print("Sexta")

if dia == 7:
    print("Sábado")

if dia < 1 and dia > 7:
    print("Valor inválido")
```

### 4. Informe o maior número entre dois números quaisquer

```
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print("O maior número é", num1)
else:
    print("O maior número é", num2)
```

### 5. Informe o maior número e o menor número entre dois números quaisquer

```
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print("O maior número é", num1)
    print("O menor número é", num2)
else:
    print("O maior número é", num2)
    print("O menor número é", num1)
```

### 6. Informe se um ano é bissexto ou não.

```
ano = int(input("Digite um ano qualquer : "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
```

### 7. Informe se um número é par (Use o módulo da divisão (%))

```
num = int(input("Digite um número qualquer : "))

if num % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")
```

### 8. Informe se um número é múltiplo de um número N qualquer

```
num = int(input("Digite um número: "))
n = int(input("Digite o múltiplo N: "))

if num % n == 0:
  print(num, "é múltiplo de", n)
else:
  print(num, "não é múltiplo de", n)
```

### 9. A partir de três notas de um aluno e informe se ele passou por média (70.0 ou mais)

```
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
if media >= 70.0:
  print("Aluno aprovado com média", media)
else:
  print("Aluno reprovado com média", media)
```

### 10. Verifique entre duas pessoas quem tem o maior nome e a mais velha.

```
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

if len(nome1) > len(nome2):
    print("A pessoa com o nome mais longo é", nome1)

if len(nome2) > len(nome1):
    print("A pessoa com o nome mais longo é", nome2)

if len(nome1) > len(nome2):
    print("As pessoas têm nomes de comprimento igual.")

if idade1 > idade2:
    print("A pessoa mais velha é", nome1)

lif idade2 > idade1:
    print("A pessoa mais velha é", nome2)

if idade1 == idade2:
    print("As pessoas têm a mesma idade.")
```

### 11. Peça o login e senha de uma pessoa e informe se o login é valido.

```
login = input("Informe o login: ")
senha = input("Informe a senha: ")

if login == "admin" and senha == "1234":
    print("Login válido!")
else:
    print("Login inválido.")
```

### 12. Informe se uma pessoa tem idade para votar em 2023, a partir de seu ano de nascimento

```
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = 2023 - ano_nascimento
if idade >= 16:
  print("Esta pessoa tem idade para votar")
else:
  print("Esta pessoa não tem idade para votar")
```

### 13. Informe se uma pessoa pode doar sangue (entre 18 e 59 anos)

```
ano_nascimento = int(input("Informe o seu ano de nascimento: "))

idade = 2023 - ano_nascimento
if 18 <= idade <= 59:
  print("Esta pessoa pode doar sangue")
else:
  print("Esta pessoa não pode doar sangue")
```

### 14. As maçãs custam 0,30 cada se forem compradas menos do que uma dúzia, e 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra

```
num_macas = int(input("Digite o número de maçãs compradas: "))

if num_macas < 12:
    preco = 0.3 
else:
    preco = 0.25


total = preco * num_macas
print("O valor total da compra é: R$", total)
```
