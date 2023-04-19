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

- No dataset de tipos de veículos acima, converta o atributo 'Cor' em númerico

- O que é um dataset desbalanceado? O desbalanceamento ocorre em termos de atributos ou classes?

- Que técnicas podem minimizar o impacto de dados desbalanceados? Quando utiliza-las? 

- Na técnica Oversampling, o que significa interpolar as amostras? Ilustre um exemplo

- Análisando as distribuições abaixo (A e B):
  
  - Qual aprensenta as fronteiras decisão mais definidas? Justifique sua resposta
  
  - Qual apresenta desbalanceamento de classes? Justifique sua resposta

- ![](/home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-15-50-29-image.png)

        

- O que é a normalização de atributos? Porque isso é importante? Normalize as features abaixo por minmax():
  
  <img title="" src="data:image/png;base64,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" alt="How to Scale data into the 0-1 range using Min-Max Normalization. -  Knowledge Transfer" data-align="center" width="293"><img title="" src="images/2023-04-19-09-21-16-image.png" alt="" data-align="center" width="212">

- O que é a redução de atributos, e quando podemos aplicá-la?

- O que significa a correlação de atributos? Dê exemplos

- O que faz o algoritmo PCA? 

- Como interpretar o grafico da variância (PCA) abaixo? 

<img title="" src="./images/2023-04-18-15-54-45-image.png" alt="" width="398" data-align="center">

#### Algoritmo KNN

- Descreva em poucas linhas o algoritmo KNN. Se preferir, faça um desenho auxiliar e explique.

- O KNN funciona somente para 2 classes (binário) ? 

- Qual a desvantagem do KNN em datasets grandes ? Por exemplo, com 100 mil amostras?

- O KNN reduz o espaço de características? E o espaço de busca? Porque?

- O que é o parametro K, do KNN? Como ele impacta na classificação?

- Analisando as seguintes distribuições, em qual o algoritmo KNN deve performar melhor? Porque? Qual o impacto de um K maior e menor?   

<img src="./images/2023-04-18-17-34-51-image.png" title="" alt="" data-align="center">

- Qual a classe da amostra de teste para K=3 e K=5, abaixo?
  
  <img title="" src="./images/2023-04-18-17-59-41-image.png" alt="" width="339" data-align="center">
  
  
  
  Considere o seguinte dataset e a amostra de teste abaixo:<img title="" src="./images/2023-04-18-17-37-15-image.png" alt="" width="520" data-align="center">
  
  
  
      Utilizando a distância Euclidiana abaixo, qual o resultado da amostra para K=1 e K=3?

<img title="" src="./images/2023-04-18-17-40-35-image.png" alt="" data-align="center" width="264">

#### Algoritmo Naive Bayes

- Explique de maneira sucinta como funciona o Naive Bayes?

- Explique sucintamente o teorema de bayes. Cite exemplos

- O que é uma probabilidade a posteriori e a priori ? Como isso é aplicado no Naive Bayes?

- Análise as matrizes de confusão abaixo e discuta cada caso, quanto a:

- Dado dataset de frutas abaixo:
  
  
  
  <img title="" src="./images/2023-04-18-18-09-08-image.png" alt="" data-align="center" width="542">
  
  
  
  Aplique o algoritmo Naive Bayes para determinar a probalidade e classes das amostras abaixo:
  
  
  
  <img title="" src="images/2023-04-19-09-31-12-2023-04-18-18-10-13-image.png" alt="" data-align="center">

- Como aplicar o modelo Naive Bayes em datasets númericos, como atributos como peso, altura, salario, etc? De exemplos.

#### Algoritmo Decision Tree

- Explique com suas palavras o algoritmo de árvore de decisão. Ilustre um exemplo

- O que é a entropia, probabilidade e ganho de informação?

- O que o ganho de informação representa para este algoritmo?

- Considerando o dataset de frutas acima, calcule a entropia e o ganho de informação para a característica 'Tamanho'.

#### Análise Crítica

- Analisando as fronteiras de decisão de um modelo, o que se pode infererir quanto a generalização do modelo? Quais classes devem sofrer perdas de acurácia?

        Modelo A

<img title="" src="images/2023-04-19-09-44-06-image.png" alt="" data-align="center">

        Modelo B

<img title="" src="images/2023-04-19-09-42-33-image.png" alt="" width="217" data-align="center">

       

Modelo C

<img title="" src="https://i.stack.imgur.com/taWXA.png" alt="python - SVM: plot decision surface when working with more than 2 features  - Stack Overflow" width="344" data-align="center">



- O que é acurácia, recall?

- Porque a acurácia geral não é uma boa métrica? Dê um exemplo

- Calcule a acurácia do modelo a partir da matriz de confusão abaixo:<img title="" src="https://datatron.com/wp-content/uploads/2021/03/actual-prediction.png" alt="What is a Confusion Matrix in Machine Learning?" width="230" data-align="center">

- Dados as matrizes de confusão abaixo, análise os casos individualmente quanto:
  
  - Qual a acurácia global ?
    
    O modelo está bem ajustado ou existe overfitting?
    
    O dataset pode ser considerado balanceado?
    
    Caso A:
    
    <img title="" src="https://user-images.githubusercontent.com/19996897/39518681-875e0048-4e21-11e8-938e-45a8661ad92e.PNG" alt="GitHub - SrikanthVelpuri/dogsvscats: Classification of Cats and Dogs" data-align="center" width="376">
    
    Caso B
    
    <img title="" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqsf9EpkqDpXyEG96oaWn8A96wP7ekB96SxA&usqp=CAU" alt="Evaluating a Classification Model Machine Learning, Deep Learning, and Computer Vision" data-align="center" width="311">

             Caso C:

   <img title="" src="https://cdn-images-1.medium.com/max/1600/0*9dlgBM9YK_UQnUtN." alt="Avaliação do Modelo de Classificação BLOG DO ZOUZA" data-align="center" width="370">

            Caso D:

<img title="" src="data:image/png;base64,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" alt="What is balanced accuracy? | Statistical Odds & Ends" data-align="center" width="386">
