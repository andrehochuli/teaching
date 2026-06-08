# Lista de Exercícios - Recursividade

## 1. Imprimir números de N até 0

Implemente uma função recursiva que imprime todos os números de `N` até `0`.

<details>
<summary>Ver resposta</summary>

```python
def print_rec(N):
    print(N)

    if N != 0:
        print_rec(N - 1)
```

</details>

---

## 2. Imprimir números de 0 até N

Implemente uma função recursiva que imprime todos os números de `0` até `N`.

<details>
<summary>Ver resposta</summary>

```python
def print_rec(N):
    if N != 0:
        print_rec(N - 1)

    print(N)
```

</details>

---

## 3. Soma dos números de N até 0

Desenvolva uma função recursiva que retorna a soma de todos os números inteiros de `N` até `0`.

<details>
<summary>Ver resposta</summary>

```python
def soma(N):
    if N == 0:
        return 0

    s = N + soma(N - 1)

    return s
```

</details>

---

## 4. Soma dos dígitos de um número inteiro

Crie uma função recursiva que calcula a soma dos dígitos de um número inteiro.

Exemplo:

```python
4871
```

Saída esperada:

```python
20
```

<details>
<summary>Ver resposta</summary>

```python
def soma_digitos(n):
    if n == 0:
        return 0

    return n % 10 + soma_digitos(n // 10)
```

</details>

---

## 5. Soma dos elementos de um vetor

Implemente uma função recursiva que retorna a soma dos elementos de um vetor de inteiros.

<details>
<summary>Ver resposta</summary>

```python
def soma_vet(vet):
    if len(vet) == 1:
        return vet[0]

    s = vet[0] + soma_vet(vet[1:])

    return s
```

</details>

---

## 6. Fatorial de N

Escreva uma função recursiva para calcular o fatorial de `N`.

<details>
<summary>Ver resposta</summary>

```python
def fat(N):
    if N == 1:
        return 1

    s = N * fat(N - 1)

    return s
```

</details>

---

## 7. Sequência de Fibonacci

Desenvolva uma função recursiva para calcular o `N`-ésimo termo da sequência de Fibonacci.

Considere:

```python
fibo(0) = 0
fibo(1) = 1
```

<details>
<summary>Ver resposta</summary>

```python
def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    s = fibo(N - 1) + fibo(N - 2)

    return s
```

</details>

---

## 8. Selection Sort recursivo

Implemente o algoritmo Selection Sort para ordenar um vetor de inteiros usando recursividade.

<details>
<summary>Ver resposta</summary>

```python
def selection_sort(vet, i=0):
    if i == len(vet) - 1:
        return vet

    min_index = i

    for j in range(i + 1, len(vet)):
        if vet[j] < vet[min_index]:
            min_index = j

    temp = vet[i]
    vet[i] = vet[min_index]
    vet[min_index] = temp

    return selection_sort(vet, i + 1)
```

</details>

