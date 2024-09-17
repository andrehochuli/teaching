
# SIMULADO DE PROVA

Este simulado de prova tem como objetivo orientar o aluno em seus estudos, além de desmistificar a forma como o conteúdo será cobrado durante a avaliação. As questões podem aparecer em diversos formatos, como discursivas, de múltipla escolha, verdadeiro ou falso, associações, resolução de problemas, ou até mesmo em forma de estudos de caso. É importante ressaltar que o simulado oferece uma base de validação do nível de conhecimento do aluno, ajudando a identificar pontos fortes e áreas que necessitam de maior atenção. No entanto, ele não deve ser utilizado como única fonte de estudo. 

## APRENDIZADO DE MÁQUINA SUPERVISIONADO

### Conceitos Gerais


- **O que é o aprendizado de máquina supervisionado?**  


- **O que significa a anotação dos dados?**  

- **O que são atributos e classes?**  

- **Dê um exemplo de uma instância (amostra) de um problema de classificação qualquer. Por exemplo, como você classificaria carros? E cães e gatos?**  

- **O que significa representatividade em termos de características?**  

- **Dado os datasets abaixo, determine o que são atributos e o que são classes (target):**

1. **Dataset de Cães e Gatos**:

| Tamanho (cm) | Peso (kg) | Comprimento do Pelo (cm) | Animal  |
|--------------|-----------|--------------------------|---------|
| 40           | 15        | 4                        | Cão     |
| 50           | 20        | 6                        | Cão     |
| 35           | 10        | 3                        | Gato    |
| 25           | 8         | 2                        | Gato    |
| 45           | 18        | 5                        | Cão     |


2. **Dataset de Veículos**:

| Marca  | Ano  | Preço (R$) | Quilometragem (km) | Tipo   |
|--------|------|------------|--------------------|--------|
| Ford   | 2018 | 45000      | 50000              | Sedan  |
| Honda  | 2020 | 60000      | 30000              | SUV    |
| Toyota | 2019 | 55000      | 40000              | Hatch  |
| Fiat   | 2021 | 40000      | 25000              | Sedan  |
| BMW    | 2017 | 75000      | 60000              | SUV    |



- **Quais etapas possui um fluxo (pipeline) de aprendizado de máquina?**

- **O que é classificação binária e multi-classes?**


- **Como abordar classificação multi-classes a partir de modelos binários?**

- **Diferencie a técnica One vs One e One vs All**

### Análise Inicial

- Porque é interessante visualizar a distribuição dos dados? O que desejamos verificar com isso?
  
- Analisando as distribuições abaixo (A e B), qual apresenta as fronteiras de decisão mais definidas? Justifique sua resposta.

- **O que é a normalização de atributos? Por que isso é importante?**  

 ### Algoritmo KNN

 - **Defina o algoritmo KNN. Forneça um exemplo lúdico**
   


- **O KNN funciona somente para 2 classes (binário)?**  
  
- **Qual a desvantagem do KNN em datasets grandes? Por exemplo, com 100 mil amostras e 2000 atributos?**  
  
- **O KNN reduz o espaço de características? E o espaço de busca? Justifique.**  

- **O que é o parâmetro K do KNN? Como ele impacta na classificação? Justifique.**  

- Analisando as seguintes distribuições, em qual o algoritmo KNN deve performar melhor? Por quê? 
  
  - Qual o impacto de um K maior e menor em cada uma das distribuições?

<img title="" src="./images/2023-04-18-17-34-51-image.png" alt="" data-align="center">

- **Considerando o dataset abaixo:**

| Característica 1 | Característica 2 | Característica 3 | Target           |
|------------------|------------------|------------------|------------------|
| 0                | 0                | 3                | B                |
| 1                | 1                | 0                | B                |
| 3                | 0                | 0                | A                |
| 2                | 2                | 2                | B                |
| 1                | 3                | 3                | B                |
| 2                | 1                | 1                | A                |
| 3                | 1                | 2                | A                |
-----------------------------------------------------------------------------


**Amostra de Teste**


| Característica 1  | Característica 2  | Característica 3  | Classificação   |
|------------------|------------------|------------------|-----------------|
| **2**            | **1**            | **1**            | ?????           |



e utilizando a distância euclidiana: qual o resultado da amostra para K=3 e K=5?

<img title="" src="./images/2023-04-18-17-40-35-image.png" alt="" data-align="center" width="245">


#### Algoritmo Naive Bayes

- **Explique de maneira sucinta como funciona o Naive Bayes:**  
 
- **O que seria atributos dependentes e indepentes ?
 
 
- **O que é uma probabilidade a posteriori e a priori? Como isso é aplicado no Naive Bayes?**  
 
#### Algoritmo Decision Tree

- **Explique com suas palavras o algoritmo de árvore de decisão. Ilustre um exemplo.**
 
- **O que é a entropia, probabilidade e ganho de informação? Como isso influência na construção da árvore?**  

- **O que o ganho de informação impacta para este algoritmo?**  

#### Análise Crítica

- **Analisando as fronteiras de decisão, o que se pode inferir quanto à generalização do modelo? Quais classes devem sofrer perdas de acurácia e por quê?**

        **Modelo A**

<img title="" src="images/2023-04-19-09-44-06-image.png" alt="" data-align="center" width="250">


    **Modelo B**

<img title="" src="images/2023-04-19-09-42-33-image.png" alt="" width="190" data-align="center">


    **Modelo C**

<img title="" src="https://i.sstatic.net/taWXA.png" alt="python - SVM: plot decision surface when working with more than 2 features  - Stack Overflow" width="351" data-align="center">


- **O que determinam as métricas de acurácia e recall?**


- **Por que a acurácia geral não é uma boa métrica? Dê um exemplo.**

- **Dadas as matrizes de confusão abaixo, analise os casos individualmente quanto a:**

  - Qual é a acurácia global?
  - O modelo está bem ajustado ou existe overfitting?
  - O dataset pode ser considerado balanceado?
    
    **Caso A:** 
    
    |               | Predito Cão | Predito Gato |
    |---------------|-------------|--------------|
    | **Real Cão**  | 40          | 10           |
    | **Real Gato** | 0           | 50           |
    
    
    
    **Caso B**
    
    |               | Predito Carro | Predito Moto |
    |---------------|---------------|--------------|
    | **Real Carro** | 90            | 0            |
    | **Real Moto**  | 8             | 2            |
    

