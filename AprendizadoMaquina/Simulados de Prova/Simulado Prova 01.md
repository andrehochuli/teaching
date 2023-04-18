# SIMULADO DE PROVA

## APRENDIZADO DE MÁQUINA SUPERVISIONADO

#### Conceitos Gerais

- O que é o aprendizado de máquina supervisionado?

- O que é aprendizado não-supervisionado?

- O que são atributos e classes?

- De um exemplo de uma instância (amostra) de um problema de classificação qualquer. Por exemplo, como você classificaria carros? E caes e gatos?

- O que significa a anotação dos dados?

- O que significa representativade em termos de características ?

- Dado o dataset abaixo, determine o que são atributos e o que são classes:

<img title="" src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-15-37-06-image.png" alt="" width="485" data-align="center">

-  Quais etapas possui um fluxo (pipeline) de aprendizado de máquina?   

- O que é classificação binária e multi-classes?

- Como abordar classificação multi-classes a partir de modelos binários?

#### Análise Exploratória

- O que significa análise explotória dos dados? O que desejamos verificar com isso

- O que são dados categóricos ou dados númericos?

- Como converto um dado categórico em númerico? De um exemplo

- Na questão 6 acima, converta o atributo 'Cor' em númerico

- O que é um dataset desbalanceado? O desbalanceamento é em termos de atributos ou classes?

- Que técnicas podem minimizar o impacto de dados desbalanceados? Quando utiliza-las? 

- Na técnica Oversampling, o que significa interpolar as amostras? Ilustre um exemplo

- Análisando as distribuições abaixo (A e B):
  
  - Qual aprensenta as fronteiras decisão mais definidas?
  
  - Qual apresenta desbalanceamento de classes e porque?

- ![](/home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-15-50-29-image.png)

        

- O que é a redução de atributos, e quando podemos aplica-la?

- O que significa a correlação de atributos? De exemplos

- O que faz o algoritmo PCA? 

- Como interpretar o grafico da variancia (PCA) abaixo ? 

<img title="" src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-15-54-45-image.png" alt="" width="321" data-align="center">

#### Algoritmo KNN

- Descreva em poucas linhas o algoritmo KNN. Se preferir, faça um desenho auxiliar e explique.

- O KNN funciona somente para 2 classes (binário) ? 

- Qual a desvantagem do KNN em datasets grandes ? Por exemplo, com 100 mil amostras?

- O KNN reduz o espaço de características? E o espaço de busca? Porque?

- O que é o parametro K, do KNN? Como ele impacta na classificação?

- Analisando as seguintes distribuições, qual o algoritmo KNN deve performar melhor? Porque? Qual o impacto de um K maior e menor? O que você indicaria ?    

<img src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-17-34-51-image.png" title="" alt="" data-align="center">

- Qual a classe da amostra de teste para K=3 e K=5, abaixo?
  
  <img title="" src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-17-59-41-image.png" alt="" width="339" data-align="center">

- Considere o seguinte dataset e a amostra de teste abaixo:<img title="" src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-17-37-15-image.png" alt="" width="480" data-align="center">

- Utilizando a distância Euclidiana abaixo, qual o resultado da amostra para K=1 e K=3?
  
  
  
  <img title="" src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-17-40-35-image.png" alt="" data-align="center" width="264">
  
  #### Algoritmo Naive Bayes

- Explique de maneira sucinta como funciona o Naive Bayes?

- Explique sucintamente o teorema de bayes. Cite exemplos

- O que é uma probabilidade a posteriori e a priori ? Como isso é aplicado no Naive Bayes?

- Análise as matrizes de confusão abaixo e discuta cada caso, quanto a:

- Dado dataset abaixo:<img title="" src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-18-09-08-image.png" alt="" data-align="center" width="542">
  
  - Aplique o algoritmo Naive Bayes para determinar a probalidade e classes das amostras abaixo
    
    
    
    <img title="" src="file:///home/aghochuli/.var/app/com.github.marktext.marktext/config/marktext/images/2023-04-18-18-10-13-image.png" alt="" data-align="center" width="543">

- Como aplicar o modelo Naive Bayes em datasets númericos, como atributos como peso, altura, salario, etc? De exemplos.
  
  





Caso C:



#### Algoritmo Decision Tree

Elaboração das questões ainda em andamento



#### Análise Crítica

- O que é acuracia, recall?

- Porque a acuracia geral não é uma boa métrica? Dê um exemplo

- Calcule a accurácia do modelo a partir da matriz de confusão abaixo:<img title="" src="https://datatron.com/wp-content/uploads/2021/03/actual-prediction.png" alt="What is a Confusion Matrix in Machine Learning?" width="261" data-align="center">

- A seguir analise os casos individualmente quanto:
  
  - Qual a acurácia global ?
    
    O modelo está bem ajustado ou existe overfitting?
    
    O dataset pode ser considerado balanceado?
    
    Caso A:
    
    <img title="" src="https://user-images.githubusercontent.com/19996897/39518681-875e0048-4e21-11e8-938e-45a8661ad92e.PNG" alt="GitHub - SrikanthVelpuri/dogsvscats: Classification of Cats and Dogs" data-align="center" width="294">
    
    Caso B
    
    <img title="" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqsf9EpkqDpXyEG96oaWn8A96wP7ekB96SxA&usqp=CAU" alt="Evaluating a Classification Model Machine Learning, Deep Learning, and Computer Vision" data-align="center" width="244">

            Caso C:

   <img title="" src="https://cdn-images-1.medium.com/max/1600/0*9dlgBM9YK_UQnUtN." alt="Avaliação do Modelo de Classificação BLOG DO ZOUZA" data-align="center" width="310">

            Caso D:



<img src="data:image/png;base64,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" title="" alt="What is balanced accuracy? | Statistical Odds & Ends" data-align="center">
