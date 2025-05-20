
# Tópico 05 - Exercícios de Fixação com Laço `for`

## 1. Imprima os números de -100 a 100 utilizando `for`
```python
for i in range(-100, 101):
    print(i)
```

## 2. Imprima os números pares de 0 a 1000

Solução A
```python
for i in range(0, 1001, 2):
    print(i)
```
Solução B:
```python
for i in range(0, 1001, 1):
    if i % 2 == 0:
    	print(i)
```


## 3. Calcule o fatorial de um número N
```python
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"O fatorial de {n} é {fatorial}")
```

## 4. Juros compostos: Calcule quanto um investimento X deve render em Y anos
```python
valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): ")) / 100
anos = int(input("Digite o número de anos: "))

valor_final = valor_inicial
for i in range(0,anos):
    valor_final *= (1 + taxa_juros)

print(f"O valor final após {anos} anos será de R$ {valor_final:.2f}")
```

## 5. Informe o N-ésimo elemento de uma P.A de razão X
```python
a1 = float(input("Digite o primeiro termo da P.A: "))
razao = float(input("Digite a razão da P.A: "))
n = int(input("Digite o número do termo desejado: "))

atual = a1
for i in range(1, n):
    atual += razao
    print(i,atual)
print(f"O {n}º termo da P.A é: {atual}")
```

## 6. Informe o N-ésimo elemento de uma P.G de razão X
```python
a1 = float(input("Digite o primeiro termo da P.G: "))
razao = float(input("Digite a razão da P.G: "))
n = int(input("Digite o número do termo desejado: "))

atual = a1
for i in range(1, n):
    atual *= razao
    print(i,atual)

print(f"O {n}º termo da P.G é: {atual}")
```
