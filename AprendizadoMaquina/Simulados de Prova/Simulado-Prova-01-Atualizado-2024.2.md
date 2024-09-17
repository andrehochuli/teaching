
# SIMULADO DE PROVA

## APRENDIZADO DE MÁQUINA SUPERVISIONADO

### Conceitos Gerais


- **O que é o aprendizado de máquina supervisionado?**  
  O aprendizado de máquina supervisionado é uma técnica onde um modelo é treinado usando um conjunto de dados rotulados. Nesse contexto, os algoritmos aprendem a partir de exemplos onde os dados de entrada estão associados a saídas desejadas (rótulos ou classes), permitindo que o modelo preveja corretamente as saídas de novos dados não vistos.

- **O que significa a anotação dos dados?**  
  A anotação dos dados refere-se ao processo de rotular ou marcar dados de entrada com informações relevantes (classes ou valores). No contexto de aprendizado supervisionado, a anotação é essencial para fornecer aos modelos exemplos que relacionem entradas (atributos) com suas saídas corretas (classes), a fim de que o algoritmo aprenda essa relação.

- **O que são atributos e classes?**  
  Atributos (ou características) são as variáveis ou propriedades observáveis que descrevem uma instância de dados. Classes, por outro lado, são os rótulos ou categorias associadas às instâncias que o modelo deve aprender a prever. Em um problema de classificação, os atributos constituem os dados de entrada, e as classes são as saídas que o modelo tenta prever.

- **Dê um exemplo de uma instância (amostra) de um problema de classificação qualquer. Por exemplo, como você classificaria carros? E cães e gatos?**  
  Exemplo de classificação de carros: Um conjunto de atributos para um carro pode incluir `marca`, `modelo`, `ano`, `preço` e `quilometragem`, e a classe a ser prevista pode ser o `tipo do carro` (SUV, sedan, hatch, etc.).  
  Exemplo de classificação de cães e gatos: Para diferenciar entre cães e gatos, os atributos podem ser `tamanho`, `formato das orelhas`, `comprimento do pelo`, e `peso`. A classe a ser prevista seria `cão` ou `gato`.

- **O que significa representatividade em termos de características?**  
  Representatividade em termos de características significa que os atributos escolhidos para descrever as instâncias de dados devem ser suficientes e adequados para capturar as informações necessárias para que o modelo consiga realizar previsões precisas. Um conjunto de dados é representativo se as características selecionadas refletirem de maneira adequada as variações e padrões relevantes no problema que está sendo modelado.

- **Dado os datasets abaixo, determine o que são atributos e o que são classes (target):**

1. **Dataset de Cães e Gatos**:

| Tamanho (cm) | Peso (kg) | Comprimento do Pelo (cm) | Animal  |
|--------------|-----------|--------------------------|---------|
| 40           | 15        | 4                        | Cão     |
| 50           | 20        | 6                        | Cão     |
| 35           | 10        | 3                        | Gato    |
| 25           | 8         | 2                        | Gato    |
| 45           | 18        | 5                        | Cão     |

   - **Atributos**: Tamanho (cm), Peso (kg), Comprimento do Pelo (cm)
   - **Classe (target)**: Classe (Cão ou Gato)

2. **Dataset de Veículos**:

| Marca  | Ano  | Preço (R$) | Quilometragem (km) | Tipo   |
|--------|------|------------|--------------------|--------|
| Ford   | 2018 | 45000      | 50000              | Sedan  |
| Honda  | 2020 | 60000      | 30000              | SUV    |
| Toyota | 2019 | 55000      | 40000              | Hatch  |
| Fiat   | 2021 | 40000      | 25000              | Sedan  |
| BMW    | 2017 | 75000      | 60000              | SUV    |

   - **Atributos**: Marca, Ano, Preço (R$), Quilometragem (km)
   - **Classe (target)**: Classe (Sedan, SUV, Hatch)


- **Quais etapas possui um fluxo (pipeline) de aprendizado de máquina?**
  1. **Coleta de Dados**: Obter os dados relevantes para o problema.
  2. **Pré-processamento de Dados**: Limpeza dos dados, tratamento de valores ausentes, normalização ou padronização e transformação dos dados.
  3. **Divisão dos Dados**: Separar o conjunto de dados em dados de treino e teste (e, opcionalmente, dados de validação).
  4. **Seleção de Atributos**: Escolher as características (atributos) mais importantes para o modelo.
  5. **Treinamento do Modelo**: Aplicar um algoritmo de aprendizado sobre os dados de treino para construir o modelo.
  6. **Avaliação do Modelo**: Testar o modelo com dados de teste para avaliar sua performance usando métricas adequadas (acurácia, recall, F1, etc.).
  7. **Ajuste de Hiperparâmetros**: Ajustar os parâmetros do modelo (como número de vizinhos no KNN, profundidade da árvore, etc.) para otimizar a performance.
  8. **Predição e Implantação**: Aplicar o modelo final para realizar previsões em novos dados e colocar o modelo em produção.

  ou conforme na figura abaixo:

  
  ![image](https://github.com/user-attachments/assets/9ca14f59-9bb1-4948-9035-043504aa452b)


- **O que é classificação binária e multi-classes?**
  - **Classificação binária**: É o problema onde existem apenas duas classes possíveis para a predição. Exemplo: classificar se um e-mail é "spam" ou "não spam".
  - **Classificação multi-classes**: É o problema em que existem mais de duas classes possíveis. Exemplo: classificar um tipo de fruta como "maçã", "banana" ou "laranja".
     
  ![image](https://github.com/user-attachments/assets/e8a58ccb-8a1f-4371-97a7-d38aded89234)


- **Como abordar classificação multi-classes a partir de modelos binários?**
  Uma maneira comum de lidar com classificação multi-classes em modelos que originalmente lidam apenas com classificação binária é dividir o problema multi-classes em vários problemas binários. Isso pode ser feito com as técnicas **One vs One** ou **One vs All**.

- **Diferencie a técnica One vs One e One vs All**
  - **One vs One (OvO)**: Para cada par de classes, um classificador binário é treinado. Se existem 3 classes, serão treinados 3 classificadores binários (A vs B, B vs C, e A vs C). Durante a predição, o modelo que obtiver mais "vitórias" será escolhido.

![image](https://github.com/user-attachments/assets/f4cd85b8-09f4-4342-b63c-2fef1b9f5581)


  - **One vs All (OvA)**: Para cada classe, um classificador binário é treinado para diferenciá-la de todas as outras classes. Se existem 3 classes, serão treinados 3 classificadores: um para distinguir A de {B, C}, outro para B de {A, C}, e assim por diante. A classe com a maior pontuação é escolhida como a predição final.

![image](https://github.com/user-attachments/assets/50bc58c9-40ea-486e-8f60-25fda22ce86c)


### Análise Inicial

- Porque é interessante visualizar a distribuição dos dados? O que desejamos verificar com isso?
  Ao plotar distribuições, podemos verificar como os dados estão espalhados, se estão balanceados entre as classes e como as variáveis se comportam, permitindo ajustes ou tratamentos antes da modelagem.
  
- Analisando as distribuições abaixo (A e B), qual apresenta as fronteiras de decisão mais definidas? Justifique sua resposta.

<img title="" src="./images/2023-04-18-15-50-29-image.png" alt="" data-align="center">

A Distribuição A mostra fronteiras de decisão mais definidas, pois as amostras de cada classe estão mais separadas. Já a Distribuição B tem uma maior sobreposição entre as classes, o que resulta em fronteiras de decisão menos definidas.

A Distribuição A tende a ser mais fácil para um modelo de classificação, enquanto a Distribuição B representa um cenário mais complexo, onde as classes são mais difíceis de separar.

- **O que é a normalização de atributos? Por que isso é importante?**  
  A normalização de atributos é o processo de ajustar os valores das variáveis em um conjunto de dados para que eles fiquem dentro de uma mesma escala (geralmente entre 0 e 1). Isso é importante para algoritmos como o KNN, pois ele se baseia em cálculos de distância. Se os atributos tiverem escalas muito diferentes, um atributo com valores maiores pode dominar o cálculo da distância e, consequentemente, influenciar a decisão final de forma desproporcional.

 ### Algoritmo KNN

 - **Defina o algoritmo KNN. Forneça um exemplo lúdico**
   
    O K-Nearest Neighbors (KNN) é um algoritmo de aprendizado supervisionado que classifica uma nova instância com base na classe mais comum entre seus "K" vizinhos mais próximos, usando uma     métrica de distância, como a distância Euclidiana. Em outras palavras, a classe da nova amostra será a classe predominante entre os K vizinhos mais próximos.
   
    ![image](https://github.com/user-attachments/assets/12c0fb58-ab31-4ac4-a1db-8598a141b814)

    Imagine que você está em uma festa e não conhece ninguém. Você quer descobrir se deve ficar no grupo de pessoas que estão discutindo tecnologia ou se deve se juntar ao grupo que está         conversando sobre esportes. Você decide usar o "algoritmo KNN" para tomar essa decisão.

    O **KNN** pede para você observar os **K** vizinhos mais próximos. Se escolher **K = 3**, você vai ouvir as três pessoas mais próximas e perceber que duas delas estão falando sobre           tecnologia e uma sobre esportes. Como a maioria está falando sobre tecnologia, você decide se juntar ao grupo tecnológico.
    
    Agora, se escolher **K = 7**, você vai observar sete pessoas e descobrir que quatro estão discutindo esportes e três estão falando sobre tecnologia. Neste caso, você provavelmente vai         decidir se juntar ao grupo esportivo.

- **O KNN funciona somente para 2 classes (binário)?**  
  Não, o KNN pode ser aplicado tanto para classificação binária quanto para multi-classes. O algoritmo simplesmente observa os K vizinhos mais próximos e atribui à amostra a classe que é mais comum entre eles, independentemente de quantas classes existam.
  
- **Qual a desvantagem do KNN em datasets grandes? Por exemplo, com 100 mil amostras e 2000 atributos?**  
  Uma grande desvantagem do KNN em datasets grandes é que ele é computacionalmente custoso. Como o algoritmo precisa calcular as distâncias entre a amostra de teste e todas as outras amostras do conjunto de dados, a complexidade computacional aumenta significativamente com o número de amostras e de atributos. Isso pode resultar em tempos de processamento lentos, especialmente para grandes datasets.
  
- **O KNN reduz o espaço de características? E o espaço de busca? Justifique.**  
  Não, o KNN não reduz o espaço de características ou de busca. Ele utiliza todas as características do conjunto de dados original para calcular as distâncias. O espaço de busca (quantidade de instâncias a serem comparadas) e o número de características permanecem os mesmos, o que aumenta a complexidade conforme o tamanho do dataset cresce.

- **O que é o parâmetro K do KNN? Como ele impacta na classificação? Justifique.**  
  O parâmetro "K" representa o número de vizinhos mais próximos que o algoritmo considera ao classificar uma nova amostra. Um valor menor de K (como 1) pode tornar o modelo mais sensível a ruídos, enquanto valores maiores de K podem tornar a classificação mais estável, pois ela será baseada em um maior número de vizinhos. No entanto, um valor de K muito alto pode incluir amostras de outras classes e reduzir a precisão do modelo. O valor de K ideal é geralmente encontrado por meio de experimentação.

- Analisando as seguintes distribuições, em qual o algoritmo KNN deve performar melhor? Por quê? 
  
  - Qual o impacto de um K maior e menor em cada uma das distribuições?

<img title="" src="./images/2023-04-18-17-34-51-image.png" alt="" data-align="center">

- Qual a classe da amostra de teste para K=3 e K=5, abaixo?

<img title="" src="./images/2023-04-18-17-59-41-image.png" alt="" width="339" data-align="center">

- Considere o seguinte dataset e a amostra de teste abaixo:

<img title="" src="./images/2023-04-18-17-37-15-image.png" alt="" width="520" data-align="inline">

      Utilizando a distância Euclidiana abaixo, qual o resultado da amostra para K=1 e K=3?

<img title="" src="./images/2023-04-18-17-40-35-image.png" alt="" data-align="center" width="245">

#### Algoritmo Naive Bayes

- Explique de maneira sucinta como funciona o Naive Bayes.
- O que é uma probabilidade a posteriori e a priori? Como isso é aplicado no Naive Bayes?
- Como aplicar o modelo Naive Bayes a datasets com atributos numéricos, tais como peso, altura, salário, etc.? Dê exemplos.

#### Algoritmo Decision Tree

- Explique com suas palavras o algoritmo de árvore de decisão. Ilustre um exemplo.
- O que é a entropia, probabilidade e ganho de informação? Como isso influência na construção da árvore?
- O que o ganho de informação impacta para este algoritmo?

#### Análise Crítica

- Analisando as fronteiras de decisão, o que se pode inferir quanto à generalização do modelo? Quais classes devem sofrer perdas de acurácia e por quê?

        **Modelo A**

<img title="" src="images/2023-04-19-09-44-06-image.png" alt="" data-align="center" width="250">

    **Modelo B**

<img title="" src="images/2023-04-19-09-42-33-image.png" alt="" width="190" data-align="center">

    **Modelo C**

<img title="" src="https://i.sstatic.net/taWXA.png" alt="python - SVM: plot decision surface when working with more than 2 features  - Stack Overflow" width="351" data-align="center">

- O que determinam as métricas de acurácia e recall?
- Por que a acurácia geral não é uma boa métrica? Dê um exemplo.
- Calcule a acurácia a partir da matriz de confusão abaixo:

<img title="" src="./images/cf_matrix_a.png" alt="asd" width="207" data-align="center">

- Dadas as matrizes de confusão abaixo, analise os casos individualmente quanto a:

  - Qual é a acurácia global?
  - O modelo está bem ajustado ou existe overfitting?
  - O dataset pode ser considerado balanceado?
    
    **Caso A:** 
    
    <img title="" src="https://user-images.githubusercontent.com/19996897/39518681-875e0048-4e21-11e8-938e-45a8661ad92e.PNG" alt="GitHub - SrikanthVelpuri/dogsvscats: Classification of Cats and Dogs" data-align="center" width="376">
    
    **Caso B:**

    <img title="" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqsf9EpkqDpXyEG96oaWn8A96wP7ekB96SxA&usqp=CAU" alt="Evaluating a Classification Model Machine Learning, Deep Learning, and Computer Vision" data-align="center" width="311">

    **Caso C:**

   <img title="" src="https://cdn-images-1.medium.com/max/1600/0*9dlgBM9YK_UQnUtN." alt="Avaliação do Modelo de Classificação BLOG DO ZOUZA" data-align="center" width="370">

    **Caso D:**

<img src="./images/imbalanced.png" title="" alt="sss" data-align="center">
