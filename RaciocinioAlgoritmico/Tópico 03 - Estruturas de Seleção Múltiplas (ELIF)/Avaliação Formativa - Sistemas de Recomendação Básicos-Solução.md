# # Avaliação Formativa - Sistemas de Recomendação Básicos

Esta avaliação formativa visa trabalhar os tópicos de estruturas de seleção múltipla e aninhamentos de estruturas. 

Os alunos devem reunir-se em equipes para a realização dos exercícios

### 1. Sistema de recomendação de livros:

- Gêneros: romance, ficção científica, fantasia, biografia, história, thriller.
- Formatos: físico ou digital.
- Exemplos de livros (outros podem ser sugeridos):
  - Romance: "Orgulho e Preconceito", de Jane Austen.
  - Ficção científica: "Neuromancer", de William Gibson.
  - Fantasia: "O Senhor dos Anéis", de J.R.R. Tolkien.
  - Biografia: "Steve Jobs", de Walter Isaacson.
  - História: "Sapiens", de Yuval Noah Harari.
  - Thriller: "O Código Da Vinci", de Dan Brown.

```python

print("Bem-vindo ao sistema de recomendação de livros!")
print("Por favor, responda às perguntas abaixo para que possamos recomendar um livro para você.")

# perguntas de preferência do usuário
genero = input("Você prefere qual gênero de livro: romance, ficção científica, fantasia, biografia, história ou thriller? ")
formato = input("Você prefere livros em formato físico ou digital? ")

# recomendação de livro com base nas preferências do usuário
if genero == "romance":
  if formato == "físico":
    print("Nós recomendamos o livro 'Orgulho e Preconceito', de Jane Austen.")
  else:
    print("Nós recomendamos o livro 'O Morro dos Ventos Uivantes', de Emily Brontë.")
elif genero == "ficção científica":
  if formato == "físico":
    print("Nós recomendamos o livro 'Neuromancer', de William Gibson.")
  else:
    print("Nós recomendamos o livro 'Ready Player One', de Ernest Cline.")
elif genero == "fantasia":
  if formato == "físico":
    print("Nós recomendamos o livro 'O Senhor dos Anéis', de J.R.R. Tolkien.")
  else:
    print("Nós recomendamos o livro 'Harry Potter e a Pedra Filosofal', de J.K. Rowling.")
elif genero == "biografia":
  if formato == "físico":
    print("Nós recomendamos o livro 'Steve Jobs', de Walter Isaacson.")
  else:
    print("Nós recomendamos o livro 'O Poder e a Glória', de Graham Greene.")
elif genero == "história":
  if formato == "físico":
    print("Nós recomendamos o livro 'Sapiens', de Yuval Noah Harari.")
  else:
    print("Nós recomendamos o livro 'O Livro Negro do Capitalismo', de Robert Kurz.")
elif genero == "thriller":
  if formato == "físico":
    print("Nós recomendamos o livro 'O Código Da Vinci', de Dan Brown.")
  else:
    print("Nós recomendamos o livro 'Garota Exemplar', de Gillian Flynn.")
else:
  print("Desculpe, não pudemos recomendar um livro com base nas suas preferências.")

```

2. Sistema de recomendação de filmes:
- Gêneros: comédia, drama, ação, ficção científica, terror, romance.
- Classificação indicativa: Livre, 10 anos, 12 anos, 14 anos, 16 anos ou 18 anos.
- Exemplos de filmes (outros podem ser sugeridos):
  - Comédia: "Debi e Loide", dos irmãos Farrelly.
  - Drama: "Forrest Gump", de Robert Zemeckis.
  - Ação: "Duro de Matar", de John McTiernan.
  - Ficção científica: "Blade Runner", de Ridley Scott.
  - Terror: "O Iluminado", de Stanley Kubrick.
  - Romance: "Simplesmente Acontece", de Christian Ditter.

```python

print("Bem-vindo ao sistema de recomendação de filmes!")

genero = input("Qual é o seu gênero favorito? Comédia, drama, ação, ficção científica, terror ou romance?\n")
classificacao = input("Qual é a sua idade? Digite a classificação indicativa do filme que você procura (Livre, 10 anos, 12 anos, 14 anos, 16 anos ou 18 anos):\n")

if genero == "comédia":
    if classificacao == "Livre" or classificacao == "10 anos":
        print("Sugestão: Debi e Loide")
    else:
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")

elif genero == "drama":
    if classificacao == "Livre" or classificacao == "10 anos" or classificacao == "12 anos":
        print("Sugestão: Forrest Gump")
    elif classificacao == "14 anos":
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")
    else:
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")

elif genero == "ação":
    if classificacao == "Livre" or classificacao == "10 anos":
        print("Sugestão: Duro de Matar")
    elif classificacao == "12 anos" or classificacao == "14 anos" or classificacao == "16 anos":
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")
    else:
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")

elif genero == "ficção científica":
    if classificacao == "Livre" or classificacao == "10 anos" or classificacao == "12 anos":
        print("Sugestão: Blade Runner")
    elif classificacao == "14 anos" or classificacao == "16 anos":
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")
    else:
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")

elif genero == "terror":
    if classificacao == "Livre" or classificacao == "10 anos" or classificacao == "12 anos" or classificacao == "14 anos":
        print("Sugestão: O Iluminado")
    elif classificacao == "16 anos" or classificacao == "18 anos":
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")
    else:
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")

elif genero == "romance":
    if classificacao == "Livre" or classificacao == "10 anos" or classificacao == "12 anos" or classificacao == "14 anos":
        print("Sugestão: Simplesmente Acontece")
    elif classificacao == "16 anos" or classificacao == "18 anos":
        print("Sugestão: Nenhum filme encontrado para a sua classificação indicativa.")

```

3. Sistema de recomendação de restaurantes:
- Tipos de comida: japonesa, italiana, mexicana, brasileira, chinesa.
- Preços: barato, médio ou caro.
- Exemplos de restaurantes:
  - Japonesa: Sushi Yama (barato), Kanpai (médio), Aizomê (caro).
  - Italiana: Spaghetti Notte (barato), Forno de Minas (médio), Fasano (caro).
  - Mexicana: La Mexicana (barato), Si Señor (médio), Mexilhão (caro).
  - Brasileira: Churrascaria Vento Haragano (barato), Fogo de Chão (médio), Rubaiyat (caro).
  - Chinesa: China in Box (barato), Ting Yuan (médio), Mr. Lam (caro).

```python
print("Bem-vindo ao sistema de recomendação de restaurantes!")

# Pergunta o tipo de comida desejado
comida = input("Qual tipo de comida você deseja? Digite japonesa, italiana, mexicana, brasileira ou chinesa: ")

# Pergunta o preço desejado
preco = input("Qual o seu orçamento? Digite barato, médio ou caro: ")

# Verifica as opções de restaurantes de acordo com a comida e o preço selecionados
if comida == "japonesa":
  if preco == "barato":
    print("Recomendamos o Sushi Yama!")
  elif preco == "médio":
    print("Recomendamos o Kanpai!")
  else:
    print("Recomendamos o Aizomê!")
elif comida == "italiana":
  if preco == "barato":
    print("Recomendamos o Spaghetti Notte!")
  elif preco == "médio":
    print("Recomendamos o Forno de Minas!")
  else:
    print("Recomendamos o Fasano!")
elif comida == "mexicana":
  if preco == "barato":
    print("Recomendamos o La Mexicana!")
  elif preco == "médio":
    print("Recomendamos o Si Señor!")
  else:
    print("Recomendamos o Mexilhão!")
elif comida == "brasileira":
  if preco == "barato":
    print("Recomendamos a Churrascaria Vento Haragano!")
  elif preco == "médio":
    print("Recomendamos o Fogo de Chão!")
  else:
    print("Recomendamos o Rubaiyat!")
elif comida == "chinesa":
  if preco == "barato":
    print("Recomendamos o China in Box!")
  elif preco == "médio":
    print("Recomendamos o Ting Yuan!")
  else:
    print("Recomendamos o Mr. Lam!")
else:
  print("Desculpe, não temos recomendações para a combinação de tipo de comida e preço selecionados.")

```

4- Sistema de recomendação de refeições:

1. Restaurante Verde Vida:
   
   - Opções veganas: sim.
   - Ambiente: casual e acolhedor.
   - Faixa de preço: médio.
   - Pratos recomendados: salada de quinoa com legumes grelhados, hambúrguer vegano com batatas fritas, pudim de chia com frutas vermelhas.

2. Restaurante Carne de Sol:
   
   - Opções veganas: não.
   - Ambiente: rústico e descontraído.
   - Faixa de preço: baixo-médio.
   - Pratos recomendados: carne de sol com macaxeira, arroz de camarão, feijão verde com torresmo.

3. Restaurante Sabor Japonês:
   
   - Opções veganas: sim.
   - Ambiente: moderno e elegante.
   - Faixa de preço: médio-alto.
   - Pratos recomendados: sushi vegano, tempurá de legumes, yakissoba de frutos do mar.

4. Restaurante La Bella Italia:
   
   - Opções veganas: sim.
   - Ambiente: sofisticado e acolhedor.
   - Faixa de preço: alto.
   - Pratos recomendados: lasanha de berinjela, penne ao molho de tomate e manjericão, torta de limão sem glúten.

Perguntas que você pode usar para criar um sistema de recomendação com base em preferências pessoais:

1. Qual é o seu orçamento?
2. Você prefere opções veganas ou não veganas?
3. Qual tipo de ambiente você prefere?
4. Qual é o seu prato favorito ou que você gostaria de experimentar?
5. Você tem alguma restrição alimentar, como glúten ou lactose?

    Neste caso, crie um sistema que a pessoa escolhe de 1 a 3 perguntas, ou seja, não precisa responder todas.

```python
print("Bem-vindo ao sistema de recomendação de refeições!")
print("Por favor, responda as seguintes perguntas para obter uma recomendação personalizada.")

preco = input("Qual é o seu orçamento? (baixo, médio, alto): ")
vegano = input("Você prefere opções veganas? (sim ou não): ")
ambiente = input("Qual tipo de ambiente você prefere? (casual e acolhedor, rústico e descontraído, moderno e elegante, sofisticado e acolhedor): ")
prato = input("Qual é o seu prato favorito ou que você gostaria de experimentar?: ")
rest_alimentos = input("Você tem alguma restrição alimentar, como glúten ou lactose? (sim ou não): ")

# Restaurante Verde Vida
if vegano == "sim" and ambiente == "casual e acolhedor" and preco == "médio" and rest_alimentos == "não":
    print("Nossa recomendação para você é o Restaurante Verde Vida! Experimente a salada de quinoa com legumes grelhados ou o hambúrguer vegano com batatas fritas.")

# Restaurante Carne de Sol
elif vegano == "não" and ambiente == "rústico e descontraído" and preco == "baixo-médio" and rest_alimentos == "não":
    print("Nossa recomendação para você é o Restaurante Carne de Sol! Experimente a carne de sol com macaxeira ou o feijão verde com torresmo.")

# Restaurante Sabor Japonês
elif vegano == "sim" and ambiente == "moderno e elegante" and preco == "médio-alto" and rest_alimentos == "não":
    print("Nossa recomendação para você é o Restaurante Sabor Japonês! Experimente o sushi vegano ou o tempurá de legumes.")

# Restaurante La Bella Italia
elif vegano == "sim" and ambiente == "sofisticado e acolhedor" and preco == "alto" and rest_alimentos == "sim":
    print("Nossa recomendação para você é o Restaurante La Bella Italia! Experimente a lasanha de berinjela ou o penne ao molho de tomate e manjericão. Eles também têm opções sem glúten!")

# Se nenhuma das opções acima for satisfeita, imprime uma mensagem de erro
else:
    print("Desculpe, não encontramos uma recomendação que atenda a todas as suas preferências.")

```
