# SIMULADO DE PROVA

## APRENDIZADO DE MÁQUINA SUPERVISIONADO

#### Conceitos Gerais

- O que é o aprendizado de máquina supervisionado?

- O que é aprendizado não-supervisionado?

- O que são atributos e classes?

- De um exemplo de uma instância (amostra) de um problema de classificação qualquer. Por exemplo, como você classificaria carros? E cães e gatos?

- O que significa a anotação dos dados?

- O que significa representativade em termos de características ?

- Dado o dataset abaixo, determine o que são atributos e o que são classes (target):

<img title="" src="./images/2023-04-18-15-37-06-image.png" alt="" width="485" data-align="center"> 

- Quais etapas possui um fluxo (pipeline) de aprendizado de máquina?   

- O que é classificação binária e multi-classes?

- Como abordar classificação multi-classes a partir de modelos binários?

- Diferencie a técnica One vs One e One vs All
  
  

#### Análise Exploratória

- O que significa a análise exploratória dos dados? O que desejamos verificar com isso

- O que são dados categóricos e dados númericos?

- Como converto um dado categórico em númerico? De um exemplo.

- Considerando o dataset de veículos acima, converta o atributo 'Cor' em númerico utilizando a técnica "one hot enconding".

- O que é um dataset desbalanceado? O desbalanceamento ocorre em termos de atributos ou classes?

- Que técnicas podem minimizar o impacto de dados desbalanceados? Quando utiliza-las? 

- Na técnica Oversampling, o que significa interpolar as amostras? Ilustre um exemplo

- Análisando as distribuições abaixo (A e B):
  
  - Qual aprensenta as fronteiras decisão mais definidas? Justifique sua resposta
  
  - Qual apresenta desbalanceamento de classes? Justifique sua resposta

- <img title="" src="./images/2023-04-18-15-50-29-image.png" alt="" data-align="center">

        

- O que é a normalização de atributos? Porque isso é importante? Normalize as features abaixo por minmax():
  
  <img title="" src="file:///run/user/1003/doc/b00ff372/euclidiana.png" alt="ss" data-align="center" width="134">
  
  <img title="" src="images/2023-04-19-09-21-16-image.png" alt="" data-align="center">

- O que é a redução de atributos e quando devemos aplicá-la?

- O que significa a correlação de atributos? Dê exemplos.

- O que faz o algoritmo PCA? 

- Como interpretar o grafico da variância (PCA) abaixo? 

<img title="" src="./images/2023-04-18-15-54-45-image.png" alt="" width="398" data-align="center">

#### Algoritmo KNN

- Descreva em poucas linhas o algoritmo KNN. Se preferir, faça um desenho auxiliar e explique.

- O KNN funciona somente para 2 classes (binário) ? 

- Qual a desvantagem do KNN em datasets grandes ? Por exemplo, com 100 mil amostras e 2000 atributos?

- O KNN reduz o espaço de características? E o espaço de busca? Justifique.

- O que é o parametro K, do KNN? Como ele impacta na classificação? Justifique.

- Analisando as seguintes distribuições, em qual o algoritmo KNN deve performar melhor? Porque? 
  
  - Qual o impacto de um K maior e menor em cada uma das distribuições?   

<img title="" src="./images/2023-04-18-17-34-51-image.png" alt="" data-align="center">

- Qual a classe da amostra de teste para K=3 e K=5, abaixo?
  
  <img title="" src="./images/2023-04-18-17-59-41-image.png" alt="" width="339" data-align="center">
  
  
  
  Considere o seguinte dataset e a amostra de teste abaixo:<img title="" src="./images/2023-04-18-17-37-15-image.png" alt="" width="520" data-align="center">
  
      Utilizando a distância Euclidiana abaixo, qual o resultado da amostra para K=1 e K=3?

<img title="" src="./images/2023-04-18-17-40-35-image.png" alt="" data-align="center" width="245">

#### Algoritmo Naive Bayes

- Explique de maneira sucinta como funciona o Naive Bayes?

- Explique sucintamente o teorema de bayes. Cite exemplos.

- O que é uma probabilidade a posteriori e a priori? Como isso é aplicado no Naive Bayes?

- Dado dataset de frutas abaixo:

<img title="" src="./images/2023-04-18-18-09-08-image.png" alt="" data-align="center" width="542">

  Aplique o algoritmo Naive Bayes para determinar a probalidade e classes das amostras abaixo:

<img title="" src="images/2023-04-19-09-31-12-2023-04-18-18-10-13-image.png" alt="" data-align="center">

- Como aplicar o modelo Naive Bayes datasets com  atributos númericos, tais como como peso, altura, salario, etc? De exemplos.

#### Algoritmo Decision Tree

- Explique com suas palavras o algoritmo de árvore de decisão. Ilustre um exemplo

- O que é a entropia, probabilidade e ganho de informação?

- O que o ganho de informação representa para este algoritmo?

- Considerando o dataset de frutas acima, calcule a entropia e o ganho de informação para a característica 'Tamanho'.

#### Análise Crítica

- Analisando as fronteiras de decisão, o que se pode infererir quanto a generalização do modelo? Quais classes devem sofrer perdas de acurácia e porque?

        **Modelo A**

<img title="" src="images/2023-04-19-09-44-06-image.png" alt="" data-align="center" width="250">

    **Modelo B**

<img title="" src="images/2023-04-19-09-42-33-image.png" alt="" width="190" data-align="center">

       

    **Modelo C**

<img title="" src="https://i.stack.imgur.com/taWXA.png" alt="python - SVM: plot decision surface when working with more than 2 features  - Stack Overflow" width="351" data-align="center">

- O que determinas as métricas de acurácia e recall?

- Porque a acurácia geral não é uma boa métrica? Dê um exemplo.

- Calcule a acurácia  a partir da matriz de confusão abaixo:
  
  <img title="" src="file:///run/user/1003/doc/b5c7835a/cf_matrix_a.png" alt="asd" width="207" data-align="center">

- Dados as matrizes de confusão abaixo, análise os casos individualmente quanto:
  
  - Qual a acurácia global ?
    
    O modelo está bem ajustado ou existe overfitting?
    
    O dataset pode ser considerado balanceado?
    
    **Caso A:** 
    
    <img title="" src="https://user-images.githubusercontent.com/19996897/39518681-875e0048-4e21-11e8-938e-45a8661ad92e.PNG" alt="GitHub - SrikanthVelpuri/dogsvscats: Classification of Cats and Dogs" data-align="center" width="376">
    
    **Caso B:**
    
    <img title="" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqsf9EpkqDpXyEG96oaWn8A96wP7ekB96SxA&usqp=CAU" alt="Evaluating a Classification Model Machine Learning, Deep Learning, and Computer Vision" data-align="center" width="311">

        **Caso C:**

   <img title="" src="https://cdn-images-1.medium.com/max/1600/0*9dlgBM9YK_UQnUtN." alt="Avaliação do Modelo de Classificação BLOG DO ZOUZA" data-align="center" width="370">

            **Caso D:**

<img title="" src="file:///run/user/1003/doc/ff8690d1/imbalanced.png" alt="   asd" data-align="center" width="396">
