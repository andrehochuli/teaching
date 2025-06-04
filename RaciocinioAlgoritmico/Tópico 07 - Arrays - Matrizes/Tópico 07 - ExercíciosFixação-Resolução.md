# Tópico 07 - Exercícios de Fixação - Arrays (Matrizes)

Para estes exercícios, é importante que você não utilize funções built-in do Python, ou seja, aquelas que já vem pré-definidas na linguagem (max, mean, min, sort, etc). O objetivo é praticar a manipulação de Matrizes (arrays n-Dimensionais) em Python utilizando apenas as estruturas de controle, como laços de repetição e estruturas condicionais. Assim você irá aprimorar sua habilidade em lógica de programação 

1. Solicite para um usuário popular uma matriz de 3x3. Imprima essa matriz na tela, considerando a formatação correta. Exemplo
   
   | 40      | 120    | 76     |
   | ------- | ------ | ------ |
   | **672** | **12** | -**9** |
   | **30**  | **6**  | **39** |

```python
# Entrada de uma matriz 3x3 pelo usuário
matriz = []
print("Digite os 9 números da matriz 3x3:")

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)

# Impressão formatada sem join
print("\nMatriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(f"|\t{elemento}\t|", end="")
    print()
```


2. Dado uma matriz 7x5, populada aleatóriamente, informe:
   
   	- A média de cada coluna
   
   	- O maior elemento de cada coluna

```python
import random

# Criação da matriz 7x5 sem list comprehension
matriz = []
for i in range(7):
    linha = []
    for j in range(5):
        linha.append(random.randint(0, 100))
    matriz.append(linha)

# Impressão da matriz
print("Matriz 7x5:")
for i in range(7):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()

# Cálculo das médias e maiores elementos por coluna
print("\nEstatísticas por coluna:")
for col in range(5):
    soma = 0
    maior = matriz[0][col]
    for lin in range(7):
        soma += matriz[lin][col]
        if matriz[lin][col] > maior:
            maior = matriz[lin][col]
    media = soma / 7
    print("Coluna", col + 1, ": Média =", round(media, 2), ", Maior =", maior)
```
3. Dado uma matriz 50x50, apresente a média das diagonais

```python
# Criação da matriz 50x50
matriz = []
for i in range(50):
    linha = []
    for j in range(50):
        linha.append(random.randint(1, 100))
    matriz.append(linha)

# Cálculo das médias das diagonais
soma_principal = 0
soma_secundaria = 0

for i in range(50):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][49 - i]

media_principal = soma_principal / 50
media_secundaria = soma_secundaria / 50

print("Média da diagonal principal:", round(media_principal, 2))
print("Média da diagonal secundária:", round(media_secundaria, 2))
```

4. Implemente o jogo "campo minado". As células com 'X' representam bomba, e '  ' célula livre.

```python
def gerar_campo(tamanho, bombas):
    campo = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(' ')
        campo.append(linha)

    colocadas = 0
    while colocadas < bombas:
        i = random.randint(0, tamanho - 1)
        j = random.randint(0, tamanho - 1)
        if campo[i][j] != 'X':
            campo[i][j] = 'X'
            colocadas += 1
    return campo

def imprimir_campo(campo):
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            print(campo[i][j], end=" | ")
        print("\n" + "-" * (len(campo[i]) * 4 - 1))

campo = gerar_campo(5, 5)
print("Campo Minado:")
imprimir_campo(campo)
```
5. Implemente o jogo da velha
```python

def inicializar_tabuleiro():
    tabuleiro = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro

def imprimir_tabuleiro(tab):
    for i in range(3):
        for j in range(3):
            print(tab[i][j], end=" | ")
        print("\n" + "-" * 9)

def verificar_vitoria(tab, jogador):
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] == jogador:
            return True
        if tab[0][i] == tab[1][i] == tab[2][i] == jogador:
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] == jogador:
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] == jogador:
        return True
    return False

tabuleiro = inicializar_tabuleiro()
jogador = 'X'

for rodada in range(9):
    imprimir_tabuleiro(tabuleiro)
    print("Jogador", jogador, "informe linha e coluna (0-2):")
    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        if verificar_vitoria(tabuleiro, jogador):
            imprimir_tabuleiro(tabuleiro)
            print("Jogador", jogador, "venceu!")
            break
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print("Posição já ocupada. Tente novamente.")
else:
    imprimir_tabuleiro(tabuleiro)
    print("Empate!")
```
