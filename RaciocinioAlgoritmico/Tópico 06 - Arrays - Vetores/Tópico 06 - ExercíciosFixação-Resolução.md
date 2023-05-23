# Tópico 05 - Exercícios de Fixação - Arrays (Vetores)

Para estes exercícios, é importante que você não utilize funções built-in do Python, ou seja, aquelas que já vem pré-definidas na linguagem (max, mean, min, sort, etc). O objetivo é praticar a manipulação de vetores 1D em Python utilizando apenas as estruturas de controle, como laços de repetição e estruturas condicionais. Assim você irá aprimorar sua habilidade em programação 

1. Crie um vetor de 20 elementos aleatórios
   
   ```python
   import random
   
   # Criando um vetor vazio
   vetor = []
   
   # Preenchendo o vetor com 20 números aleatórios entre 0 e 100
   for i in range(20):
       vetor.append(random.randint(0, 100))
   
   # Imprimindo o vetor na tela
   print(vetor)
   
   ```
   
   ```python
   import random
   
   # Criando um vetor vazio de tamanho 20
   vetor = [0] * 20
   
   # Preenchendo o vetor com números aleatórios entre 0 e 100
   for i in range(20):
       vetor[i] = random.randint(0, 100)
   
   # Imprimindo o vetor na tela
   print(vetor)
   
   ```

2. Crie um vetor de 20 elementos incrementando-os de 5 em 5
   
   ```python
   # Criando um vetor vazio
   vetor = [0] * 20
   
   # Preenchendo o vetor com números incrementais de 5 em 5
   for i in range(20):
       vetor[i] = (i + 1) * 5
   
   # Imprimindo o vetor na tela
   print(vetor)
   
   ```

3. Crie um vetor contendo N elementos digitados pelo usuário
   
   ```python
   # Lendo o tamanho do vetor N
   N = int(input("Digite o tamanho do vetor: "))
   
   # Criando um vetor vazio
   vetor = []
   
   # Lendo os elementos do vetor e adicionando-os ao final do vetor
   for i in range(N):
       valor = int(input("Digite o valor do elemento %d: " % (i+1)))
       vetor.append(valor)
   
   # Imprimindo o vetor na tela
   print(vetor)
   
   ```
   
   

4. Enquanto o usuário não digitar números negativos, adicione elementos ao vetor:
   
   ```python
   # Criando um vetor vazio
   vetor = []
   
   # Lendo os elementos do vetor até que o usuário digite um número negativo
   valor = int(input("Digite um número (digite um número negativo para sair): "))
   while valor >= 0:
       vetor.append(valor)
       valor = int(input("Digite um número (digite um número negativo para sair): "))
   
   # Imprimindo o vetor na tela
   print(vetor)
   
   ```
   
   

5. Crie um vetor contendo somente elementos pares, digitados pelo usuário. Quando digitar 0, imprima todo o vetor na tela e encerre.
   
   ```python
   # Criando um vetor vazio
   vetor = []
   
   # Lendo os elementos pares do vetor e adicionando-os ao vetor
   valor = int(input("Digite um número (digite 0 para sair): "))
   while valor != 0:
       if valor % 2 == 0:
           vetor.append(valor)
       valor = int(input("Digite um número (digite 0 para sair): "))
   
   # Imprimindo o vetor na tela
   print(vetor)
   
   ```

6. Para cada posição [i] do vetor, imprima o valor atual, seu antecessor e sucessor
   
   ```python
   vetor = [1, 3, 5, 7, 9]
   
   for i in range(1, len(vetor)-1):
       print("Valor atual:", vetor[i])
       print("Antecessor:", vetor[i-1])
       print("Sucessor:", vetor[i+1])
   
   ```

7. Apresente a soma dos elementos opostos de um vetor de 100 elementos
   
   ```python
   vetor = [i+1 for i in range(100)]
   soma = 0
   
   for i in range(50):
       soma += vetor[i] + vetor[99-i]
   
   print("A soma dos elementos opostos do vetor é:", soma)
   
   ```

8. Compute a média e o desvio padrão de um vetor
   
   ```python
   # Importando a biblioteca math para usar a função sqrt
   import math
   
   # Definindo o vetor
   vetor = [1, 2, 3, 4, 5]
   
   # Calculando a média
   media = sum(vetor) / len(vetor)
   
   # Calculando o desvio padrão
   desvio_padrao = math.sqrt(sum([(x - media) ** 2 for x in vetor]) / (len(vetor)-1))
   
   # Imprimindo os resultados
   print("Média:", media)
   print("Desvio padrão:", desvio_padrao)
   
   ```

9. Crie um vetor aleatorio. Posteriormente apresente a soma dos pares e depois dos múltiplos de 5. Também, crie um vetor com os múltiplos de 10 do vetor original.
   
   ```python
   import random
   
   # Criando um vetor aleatório de tamanho 10 com valores entre 0 e 100
   vetor = []
   for i in range(10):
       vetor.append(random.randint(0, 100))
   print("Vetor aleatório:", vetor)
   
   # Soma dos números pares (iterando por valor)
   soma_pares = 0
   for valor in vetor:
       if valor % 2 == 0:
           soma_pares += valor
   print("Soma dos números pares:", soma_pares)
   
   # Soma dos múltiplos de 5 (iterando por indice)
   soma_mult_5 = 0
   for i in range(len(vetor)): 
       if vetor[i] % 5 == 0:
           soma_mult_5 += vetor[i]
   print("Soma dos múltiplos de 5:", soma_mult_5)
   
   # Vetor com os múltiplos de 10 do vetor original 
   #(aqui usei while pare exemplificar)
   mult_10 = []
   i = 0
   while i < len(vetor):
       if vetor[i] % 10 == 0:
           mult_10.append(vetor[i])
       i += 1
   print("Vetor com os múltiplos de 10 do vetor original:", mult_10)
   
   ```

10. Crie dois vetores de 5 elementos cada, e posteriormente crie um terceiro resultante da soma deste dois
    
    ```python
    # Criando os dois vetores de 5 elementos
    vetor1 = []
    vetor2 = []
    for i in range(5):
        vetor1.append(i)
        vetor2.append(i*2)
    print("Vetor 1:", vetor1)
    print("Vetor 2:", vetor2)
    
    # Criando o terceiro vetor com a soma dos dois vetores anteriores
    vetor3 = []
    for i in range(5):
        vetor3.append(vetor1[i] + vetor2[i])
    print("Vetor 3 (soma de Vetor 1 e Vetor
    
    ```

11. Dado um vetor de 20 elementos, divida este em dois sub-vetores de 10 elementos 
    
    ```python
    # Criando um vetor de 20 elementos
    vetor = list(range(20))
    print("Vetor original:", vetor)
    
    # Dividindo o vetor em dois sub-vetores de 10 elementos cada
    sub_vetor1 = []
    sub_vetor2 = []
    for i in range(len(vetor)):
        if i < 10:
            sub_vetor1.append(vetor[i])
        else:
            sub_vetor2.append(vetor[i])
    print("Sub-vetor 1:", sub_vetor1)
    print("Sub-vetor 2:", sub_vetor2)
    
    ```

12. Encontre o maior elemento de um vetor
    
    ```python
    # Criando um vetor aleatório
    vetor = [3, 8, 2, 1, 10, 5]
    
    # Inicializando a variável maior_elemento com o primeiro valor do vetor
    maior_elemento = vetor[0]
    
    # Percorrendo o vetor e comparando cada elemento com o maior_elemento atual
    for i in range(len(vetor)):
        if vetor[i] > maior_elemento:
            maior_elemento = vetor[i]
    
    # Imprimindo o resultado na tela
    print("Maior elemento do vetor:", maior_elemento)
    
    ```

13. Encontre os dois maiores elementos de um vetor
    
    ```python
    # Criando um vetor aleatório
    vetor = [3, 8, 2, 1, 10, 5]
    
    # Inicializando as variáveis para os dois maiores elementos com os dois primeiros valores do vetor
    maior_elemento = vetor[0]
    segundo_maior_elemento = vetor[1]
    
    # Percorrendo o vetor e atualizando as variáveis para os dois maiores elementos
    for i in range(len(vetor)):
        if vetor[i] > maior_elemento:
            segundo_maior_elemento = maior_elemento
            maior_elemento = vetor[i]
        elif vetor[i] > segundo_maior_elemento:
            segundo_maior_elemento = vetor[i]
    
    # Imprimindo o resultado na tela
    print("Maior elemento do vetor:", maior_elemento)
    print("Segundo maior elemento do vetor:", segundo_maior_elemento)
    
    ```

14. Dado um vetor, crie um segundo vetor rotulando os indices do primeiro que contem valores acima (1) e abaixo da média (-1). Se caso for exatamente a média, então rotule como (0):
    
    Ex: [30,10,40,50,20] --> média 30 -> [0,-1,1,1,-1]
    
    ```python
    # criar vetor aleatório
    vetor = [2, 4, 5, 8, 12, 7, 3, 9, 6, 10]
    
    # calcular média do vetor
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    media = soma / len(vetor)
    
    # rotular índices
    rotulos = []
    for i in range(len(vetor)):
        if vetor[i] < media:
            rotulos.append(-1)
        elif vetor[i] > media:
            rotulos.append(1)
        else:
            rotulos.append(0)
    
    print("Vetor original:", vetor)
    print("Rotulos:", rotulos)
    
    ```

15. Dado um vetor de 20 elementos, imprima o vetor como se fosse uma piramide:
    
    vet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    1
    
    12
    
    123
    
    1234
    
    .....
    
    12345.......181920
    
    ```python
    vet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    n = len(vet)
    for i in range(n):
        #print(" "*(n-i-1), end="")
        for j in range(i+1):
            print(vet[j], end=" ")
        print()
    ```

16. Imprima a piramide invertida o exercício 14.
    
    ```python
    vet = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    for i in range(n-1,0,-1):
        #print(" "*(n-i-1), end="")
        for j in range(i+1):
            print(vet[j], end=" ")
        print()
    ```

16. Contrua e descontrua a pirâmide (dos exercíciso 14 e 15)
    
    ```python
    
    ```
