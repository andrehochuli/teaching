# Tópico 05 - Exercícios de Fixação - Funções

## 1.1 Maior elemento de um vetor

Implemente uma função `max_(vetor)` que receba um vetor numérico e retorne o maior elemento.

<details>
<summary>Ver resposta</summary>

```python
def max_(vetor):
    maior = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]

    return maior
```

</details>

---

## 1.2 Menor elemento de um vetor

Implemente uma função `min_(vetor)` que receba um vetor numérico e retorne o menor elemento.

<details>
<summary>Ver resposta</summary>

```python
def min_(vetor):
    menor = vetor[0]

    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]

    return menor
```

</details>

---

## 1.3 Inverter um vetor

Implemente uma função `invert_(vetor)` que receba um vetor e retorne um novo vetor com os elementos em ordem inversa.

<details>
<summary>Ver resposta</summary>

```python
def invert_(vetor):
    invertido = []

    for i in range(len(vetor) - 1, -1, -1):
        invertido.append(vetor[i])

    return invertido
```

</details>

---

## 1.4 Converter texto para minúsculo

Implemente uma função `lower_(texto)` que receba uma string e retorne uma nova string com todas as letras maiúsculas convertidas para minúsculas.

Não utilize o método `.lower()` do Python.

<details>
<summary>Ver resposta</summary>

```python
def lower_(texto):
    resultado = ""

    for c in texto:
        codigo = ord(c)

        if codigo >= ord('A') and codigo <= ord('Z'):
            resultado += chr(codigo + 32)
        else:
            resultado += c

    return resultado
```

</details>

---

## 1.5 Converter texto para maiúsculo

Implemente uma função `upper_(texto)` que receba uma string e retorne uma nova string com todas as letras minúsculas convertidas para maiúsculas.

Não utilize o método `.upper()` do Python.

<details>
<summary>Ver resposta</summary>

```python
def upper_(texto):
    resultado = ""

    for c in texto:
        codigo = ord(c)

        if codigo >= ord('a') and codigo <= ord('z'):
            resultado += chr(codigo - 32)
        else:
            resultado += c

    return resultado
```

</details>

---

## 1.6 Verificar se um caractere é dígito

Implemente uma função `isdigit_(c)` que receba um caractere e retorne `True` se ele for um dígito entre `'0'` e `'9'`, ou `False` caso contrário.

Não utilize o método `.isdigit()` do Python.

<details>
<summary>Ver resposta</summary>

```python
def isdigit_(c):
    return c >= '0' and c <= '9'
```

</details>

---

## 1.7 Verificar se um caractere é alfabético

Implemente uma função `ischar_(c)` que receba um caractere e retorne `True` se ele for uma letra maiúscula ou minúscula, ou `False` caso contrário.

<details>
<summary>Ver resposta</summary>

```python
def ischar_(c):
    return (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z')
```

</details>

---

## 1.8 Ordenar um vetor

Implemente uma função `sort_(vetor)` que receba um vetor numérico e retorne um novo vetor ordenado em ordem crescente.

Não utilize a função `sorted()` nem o método `.sort()` do Python.

<details>
<summary>Ver resposta</summary>

```python
def sort_(vetor):
    ordenado = vetor.copy()

    for i in range(len(ordenado)):
        for j in range(0, len(ordenado) - 1 - i):
            if ordenado[j] > ordenado[j + 1]:
                aux = ordenado[j]
                ordenado[j] = ordenado[j + 1]
                ordenado[j + 1] = aux

    return ordenado
```

</details>

---

## 1.9 Verificar se um valor existe no vetor

Implemente uma função `exist_(vetor, valor)` que receba um vetor e um valor, retornando `True` se o valor existir no vetor, ou `False` caso contrário.

Não utilize o operador `in`.

<details>
<summary>Ver resposta</summary>

```python
def exist_(vetor, valor):
    for elemento in vetor:
        if elemento == valor:
            return True

    return False
```

</details>

---

## 1.10 Calcular média e desvio padrão

Implemente uma função `dev_padrao(vetor)` que receba um vetor numérico e retorne a média e o desvio padrão dos valores.

A função deve retornar dois valores: `media` e `desvio`.

<details>
<summary>Ver resposta</summary>

```python
def dev_padrao(vetor):
    soma = 0

    for valor in vetor:
        soma += valor

    media = soma / len(vetor)

    soma_diferencas = 0

    for valor in vetor:
        soma_diferencas += (valor - media) ** 2

    variancia = soma_diferencas / len(vetor)
    desvio = variancia ** 0.5

    return media, desvio
```

</details>

---

## 1.11 Concatenar dois vetores

Implemente uma função `concatena_(vetor1, vetor2)` que receba dois vetores e retorne um novo vetor contendo os elementos do primeiro vetor seguidos dos elementos do segundo vetor.

Não utilize o operador `+` para concatenar listas.

<details>
<summary>Ver resposta</summary>

```python
def concatena_(vetor1, vetor2):
    resultado = []

    for valor in vetor1:
        resultado.append(valor)

    for valor in vetor2:
        resultado.append(valor)

    return resultado
```

</details>

---

## 2. Retornar os índices que possuem números pares

Implemente uma função `indices_pares(vetor)` que receba um vetor numérico e retorne uma lista contendo os índices dos elementos pares.

Exemplo:

```python
[10, 11, 12, 13, 14]
```

Saída esperada:

```python
[0, 2, 4]
```

<details>
<summary>Ver resposta</summary>

```python
def indices_pares(vetor):
    indices = []

    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            indices.append(i)

    return indices
```

</details>

---

## 3. Retornar a frequência dos elementos

Implemente uma função `frequencia(vetor)` que receba um vetor e retorne uma lista contendo cada elemento distinto e sua respectiva frequência.

Exemplo:

```python
[1, 2, 1, 3, 3, 4, 3, 1, 2, 1, 1]
```

Saída esperada:

```python
[[1, 5], [2, 2], [3, 3], [4, 1]]
```

<details>
<summary>Ver resposta</summary>

```python
def frequencia(vetor):
    resultado = []

    for i in range(len(vetor)):
        valor = vetor[i]
        ja_contado = False

        for j in range(len(resultado)):
            if resultado[j][0] == valor:
                ja_contado = True

        if not ja_contado:
            cont = 0

            for k in range(len(vetor)):
                if vetor[k] == valor:
                    cont += 1

            resultado.append([valor, cont])

    return resultado
```

</details>

---

## 4. Validação de CPF

Implemente uma função `valida_cpf(cpf)` que receba uma string representando um CPF e retorne `True` se o CPF for válido, ou `False` caso contrário.

A função deve:

1. Remover caracteres que não sejam dígitos;
2. Verificar se o CPF possui exatamente 11 dígitos;
3. Rejeitar CPFs com todos os dígitos iguais;
4. Calcular e validar os dois dígitos verificadores.

<details>
<summary>Ver resposta</summary>

```python
def valida_cpf(cpf):
    apenas_digitos = ""

    for c in cpf:
        if isdigit_(c):
            apenas_digitos += c

    cpf = apenas_digitos

    if len(cpf) != 11:
        return False

    todos_iguais = True

    for i in range(1, len(cpf)):
        if cpf[i] != cpf[0]:
            todos_iguais = False

    if todos_iguais:
        return False

    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    if digito1 != int(cpf[9]):
        return False

    soma = 0
    peso = 11

    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if digito2 != int(cpf[10]):
        return False

    return True
```

</details>

