# 🧪 Simulado — Hash Tables

---

## 🧠 Questão 1 — Teórica

Explique o que é uma **tabela hash** e qual é o papel de uma **função hash**.

Em sua resposta, aborde:
- como ocorre o mapeamento de uma chave para um índice;
- o que caracteriza uma boa função hash;
- por que colisões podem ocorrer;
- técnicas para tratar colisões.

---

## 💻 Questão 2 — Prática

Considere uma tabela hash de tamanho **10**, com função:

```
h(k) = k mod 10
```

Tratamento de colisão: **encadeamento**

Insira, nesta ordem, as chaves:

```
15, 25, 12, 42, 22, 35, 5
```

### Pede-se:
a) Mostre o estado final da tabela  
b) Indique o índice de cada chave  
c) Identifique onde ocorreram colisões  

---

## 🔍 Questão 3 — Considere uma tabela hash de tamanho **7**, com:

**h(k) = k mod 7**

Tratamento de colisão: **encadeamento**

Estado final:

| Índice | Conteúdo |
|--------|----------|
| 0      | 21       |
| 1      | 15       |
| 2      | 9, 30    |
| 3      | vazio    |
| 4      | vazio    |
| 5      | 12, 19   |
| 6      | vazio    |

### Pede-se:

 
a) Identifique colisões  
b) Proponha um input que gere essa tabela  


---
## 🔍 Questão 4 — Considere uma tabela hash com tratamento de colisão por **encadeamento**.

Após a inserção de algumas chaves (em ordem desconhecida), obteve-se o seguinte estado final:

| Índice | Conteúdo        |
|--------|-----------------|
| 0      | 14, 21          |
| 1      | 8               |
| 2      | vazio           |
| 3      | 10, 17, 24      |
| 4      | 11              |
| 5      | vazio           |
| 6      | 13              |

Sabe-se que:
- Todas as chaves são números inteiros positivos
- A função hash é da forma: **h(k) = k mod m**
- O tamanho da tabela é igual a **m**

---

### Pede-se:

**Qual das funções hash abaixo é compatível com o estado da tabela?**

a) `h(k) = k % 5`  
b) `h(k) = k % 6`  
c) `h(k) = k % 7`  
d) `h(k) = (k + 1) % 7`  
e) `h(k) = (2 * k) % 7`  


# 🌳 Simulado — Árvores BST e AVL

---

## 🧠 Questão 1 — Conceitual

Explique a diferença entre uma **Binary Search Tree (BST)** e uma **AVL Tree**.

Aborde:
- propriedade de ordenação;
- balanceamento;
- impacto na complexidade das operações.

---

## 🌳 Questão 2 — Propriedade da BST

Considere a árvore:

```text
        40
       /  \
     20    60
    / \    / \
   10 30  50 70
```

### Pede-se:
a) A árvore é uma BST válida?  
b) Informe o percurso em-ordem, post-ordem e in-ordem  
c) Informe o menor e o maior valor  

---

## 💻 Questão 3 — Inserção em BST + Pseudocódigo

Considere o pseudocódigo:

```text
fun insert(root, key):
    se root == null:
        retorne novo_nodo(key)

    se key > root.valor:
        root.dir = insert(root.dir, key)
    senão:
        root.esq = insert(root.esq, key)

    retorne root
```

Valores:
```text
50, 30, 70, 20, 40, 60, 80
```

### Pede-se:
a) Informe a árvore resultante  
b) Informe o percurso em-ordem  
c) Informe a altura da árvore  

---

## 💻 Questão 4 — Inserção em BST + Pseudocódigo

Considere o pseudocódigo:

```text
fun insert(root, key):
    se root == null:
        retorne novo_nodo(key)

    se key < root.valor:
        root.dir = insert(root.dir, key)
    senão:
        root.esq = insert(root.esq, key)

    retorne root
```

Valores:
```text
45, 25, 65, 15, 35, 55, 75, 5, 20, 30, 40
```

### Pede-se:
a) Informe a árvore resultante  
b) Informe o percurso post-ordem  
c) Informe a altura da árvore  

---

## 🔍 Questão 7 — Sequência de Inserção em BST

Considere a seguinte árvore BST resultante:

```text
        40
       /  \
     20    60
    / \    / \
   10 30  50 70
```

Sabendo que a árvore foi construída por inserções sucessivas em uma **BST inicialmente vazia**, analise as sequências abaixo.

### Pede-se:
**Quais das sequências abaixo podem gerar exatamente essa árvore?**

i)  
```text
40, 20, 60, 10, 30, 50, 70
```

ii)  
```text
40, 60, 20, 70, 50, 30, 10
```

iii)  
```text
40, 20, 10, 30, 60, 50, 70
```

iv)  
```text
40, 20, 60, 30, 10, 50, 70
```

v)  
```text
20, 40, 60, 10, 30, 50, 70
```

## 🔍 Questão 6 — Sequência de Inserção em BST

Considere a seguinte árvore BST resultante:

```text
            55
           /  \
         25    80
        / \    / \
      12  37  65  92
          /
         30
```

Sabendo que a árvore foi construída por inserções sucessivas em uma **BST inicialmente vazia**, analise as sequências abaixo.

### Pede-se:
**Quais das sequências abaixo podem gerar exatamente essa árvore?**

i)  
```text
55, 25, 80, 12, 37, 65, 92, 30
```

ii)  
```text
55, 80, 25, 92, 65, 37, 12, 30
```

iii)  
```text
55, 25, 12, 37, 30, 80, 65, 92
```

iv)  
```text
55, 25, 80, 37, 12, 30, 65, 92
```

v)  
```text
25, 55, 80, 12, 37, 30, 65, 92
```

---

## 🧠 Questão 7 — Conceitos de AVL

Explique:
a) Fator de balanceamento  
b) Quando ocorre desbalanceamento  
c) Tipos de rotação  

---

## 🔄 Questão 8 — AVL — Para as sequência a seguir, informe a árvore resultante e qual(is) rotações foram realizadas (LL,RR,LR,RL)

```text
a) 68, 42, 57
b) 24, 39, 57
c) 36, 81, 65
d) 72, 58, 43
e) 28, 67, 49
f) 65, 52, 38
g) 55, 31, 44
h) 41, 63, 78
```

## ❓ Questão 9 – AVL – Considere a inserção sucessiva dos seguintes valores em uma **árvore AVL** inicialmente vazia:

```text
58, 23, 71, 12, 37, 65, 82
```

---

### Pede-se:

**Qual das alternativas abaixo representa corretamente a árvore resultante?**

---

### a)
```text
        58
       /  \
     37    71
    /      / \
  23      65 82
 /
12
```
---

### b)
```text
        58
       /  \
     23    65
    / \    / \
  12  37  71  82
```

---

### c)
```text
        65
       /  \
     58    71
    /        \
  23          82
 /  \
12  37
```
### d)
```text
        58
       /  \
     23    71
    / \    / \
  12  37  65  82
```

---
### e)
```text
        37
       /  \
     23    58
    /        \
  12          71
             /  \
            65  82
```
---

## 🌳 Questão 10 — Construção de AVL

Considere a inserção dos valores:

```text
30, 20, 40, 10, 25, 22, 50
```

**Informe a árvore AVL resultante.**

---

## 🌳 Questão 11 — Construção de AVL

Considere a inserção dos valores:

```text
40, 20, 60, 10, 30, 25, 35
```

**Informe a árvore AVL resultante.**

---

## 💻 Questão 12 — Implementação de Rotações em AVL (Pseudocódigo)

Considere uma árvore AVL em que cada nó possui os campos:
- `valor`
- `esq`
- `dir`
- `altura`

### Pede-se:

Implemente, em pseudocódigo, as seguintes rotações:

### a) Rotação simples à direita (caso LL)


### b) Rotação simples à esquerda (caso RR)


### c) Rotação dupla esquerda-direita (caso LR)


### d) Rotação dupla direita-esquerda (caso RL)
``

### Requisitos:
- Atualize corretamente os ponteiros (`esq` e `dir`)
- Atualize a altura dos nós afetados



# 🌐 Simulado — Grafos e Algoritmos de Busca

---

## 🧠 Questão 1 — Conceitual

Explique a diferença entre:
- **Busca em Largura (BFS)**  
- **Busca em Profundidade (DFS)**  

Aborde:
- estratégia de exploração;
- estruturas de dados utilizadas;
- complexidade;
- aplicações típicas.

---

## 🔄 Questão 2 — BFS (Busca em Largura)

Considere o grafo:

```text
A ----- B ----- E
| \     | \     |
|  \    |  \    |
|   \   |   \   |
C ----- D ----- F ----- H
 \     /         \     /
  \   /           \   /
    G ------------- I
```

A busca de **A --> H**.

### Pede-se:
a) Informe a ordem de visita usando **BFS**
b) Informe a árvore gerada pela BFS  

---

## 🔄 Questão 3 — DFS (Busca em Profundidade)

Considere o mesmo grafo da questão anterior.

### Pede-se:
a) Informe a ordem de visita usando **DFS (pré-ordem)**  
b) Informe a árvore gerada pela DFS  

---

## 🚀 Questão 6 — Algoritmos Guloso e A*

Considere o grafo ponderado:

```text
A --2-- B --3-- D --4-- G --2-- J
|       |       |       |
5       1       2       3
|       |       |       |
C --2-- E --3-- F --2-- H
 \               \     /
  \------6-------- I -1
``` 

### Tabela de heurística `h(n)` até o objetivo `J`
| Nó | h(n) até J |
| -- | ---------- |
| A  | 8          |
| B  | 6          |
| C  | 7          |
| D  | 4          |
| E  | 5          |
| F  | 4          |
| G  | 2          |
| H  | 3          |
| I  | 5          |
| J  | 0          |

---

### Pede-se:

a) Execute o algoritmo **guloso (Greedy Best-First)** a partir de **A até J**  
- Informe a ordem de expansão  (arvore)
- Informe o caminho encontrado  
- Informe o custo total  
---

b) Execute o algoritmo **A\***  
- Considere \( f(n) = g(n) + h(n) \)  
- Informe a ordem de expansão  
- Informe o caminho  
- Informe o custo total  

---

c) Compare as duas soluções
---

## ❓ Questão 4 – Algoritmo A* (Múltipla Escolha)

Considere o grafo ponderado:

```text
A --2-- B --3-- D
|       |       |
4       2       2
|       |       |
C --2-- E --3-- J
 \             /
  \-----6-----/
```

### Tabela de heurística `h(n)` até o objetivo `J`

| Nó | h(n) até J |
|----|------------|
| A  | 6          |
| B  | 4          |
| C  | 5          |
| D  | 2          |
| E  | 3          |
| J  | 0          |

---

### Pede-se:

**Assinale a alternativa correta sobre a execução do algoritmo A\***, considerando:

- início em **A**
- objetivo em **J**
- `f(n) = g(n) + h(n)`

### a) Caminho encontrado: `A → B → D → J`


### b) Caminho encontrado: `A → C → E → J`

### c) Caminho encontrado: `A → B → E → J`

### d) Caminho encontrado: `A → C → J`

### e) Caminho encontrado: `A → B → D → J`

---

### Gabarito:
**Alternativa correta: c**


## 🌐 Questão 5 — Grafo Ponderado (Dijkstra)

Considere o grafo ponderado:

```text
        (A)
       /   \
     2↓     ↓5
     /       \
   (B) →1→ (C)
    |  ↘3     ↓2
   4↓   ↘     (E)
    |     ↘     ↓3
   (D)     ↘   (G)
    |1       ↘ ↑
    ↓         2
   (F) --------
```

### Pede-se:

b) Informe:
- o menor custo de **A até G**  
- o caminho correspondente  

---

c) Compare com BFS:
- A BFS encontraria o mesmo caminho?  
- Justifique com base no tipo de grafo  

---

## 🌐 Questão 6 — Grafo Ponderado (Dijkstra)

Considere o grafo ponderado:

```text
        (A)
       /   \
     3/     \6
     /       \
   (B)       (C)
    | \       |
   2|  4\     |2
    |     \   |
   (D)     (E)
    | \       |
   3|  5\     |1
    |     \   |
   (F)     (G)
      \     /
       \2  /3
        (H)
```

### Pede-se:

b) Informe:
- o menor custo de **A até H**  
- o caminho correspondente  


# 🌊 Simulado — Fluxo Máximo (Max Flow)

---

## 🧠 Questão 1 — Conceitual

Explique o problema de **fluxo máximo** em grafos.

Aborde:
- definição de grafo de fluxo (origem, destino, capacidade);
- conceito de fluxo válido;
- restrições (capacidade e conservação de fluxo);
- ideia geral do algoritmo de **Ford-Fulkerson**.

---

## 🔄 Questão 2 — Execução do Algoritmo (Ford-Fulkerson)

Considere o grafo de fluxo:

```text
        (S)
       /   \
     10     5
     /       \
   (A)----15--(B)
    | \        |
   10  4       10
    |    \     |
   (C)----10--(D)
        \     /
         \   /
          (T)
           10
``` 
 

### Pede-se:

a) Apresente o gráfico residual

b) Informe o **fluxo máximo final**


## ❓ Questão 3 – Execução do Algoritmo (Ford-Fulkerson)

Considere o seguinte **grafo de fluxo**:

```text
          (S)
         /   \
      12/     \8
       /       \
     (A)---6---(B)
     /  \       / \
   10    5     7   10
   /      \   /     \
 (C)---8---(D)------(T)
      \         6
       \-------/
```

---

Considere o caminho (S) --> (T)

### Pede-se:

a) Apresente o **grafo residual final** após a execução do algoritmo de Ford-Fulkerson  

b) Informe o **fluxo máximo final**  

c) Indique ao menos **dois caminhos aumentantes** que podem ser utilizados durante a execução  

---

