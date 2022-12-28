<h1 align="center">
  <img alt="rossmann" title="#logo" src="./img/rossmann_logo.png" />
</h1>



## 1.0. Introdução ao problema de negócio

A Rossmann é uma rede de drogarias com mais de 3.000 lojas ativas em 7 países europeus. O CFO da empresa planeja fazer uma reforma em cada loja, e em reunião com todos os gerentes indivíduais solicitou uma previsão diaria das próximas 6 semanas de vendas de cada loja, pois com base nessas informações seria definido o total destinado a cada uma.

Como Cientistas de Dados da Rossmann, fomos acionados para trabalhar em uma solução.

### 1.1. Questões do negócio

- Fazer uma predição das vendas diarias de cada loja pelas próximas 6 semanas


## 2.0. Premissas do negócio

- A coluna "Costumers" foi dropada pois é uma informação que não podemos ter no momento em que estivermos fazendo o treinamento do nosso modelo, já que não sabemos quantos clientes teremos nas nossas lojas ao longo das próximas 6 semanas

- Os valores vazios da coluna "competition_distance" foram substituídos por 3 vezes o valor maximo do competidor mais distante. Estamos assumindo que se não temos essa informação, não temos competidores mais próximos e então estamos extrapolando no valor dos dados faltantes.


## 3.0. Planejamento da Solução

### 3.1. Entrega Final

- A entrega será de um Bot no Telegram, que opere 24/7 e seja capaz de devolver a soma total da predição das próximas 6 semanas de vendas da loja requisitada

### 3.2. Ferramentas

- Python 3.8.15
- Jupyter Notebook
- Matplotlib and Seaborn
- Scikit Learn
- XGBoost
- Boruta 
- Random Search
- Git and Github
- Render
- Telegram Bot

### 3.3. Processo até a solução

- **Business Understand:** Entender mais sobre a motivação do CFO por trás da solicitação da predição de vendas.

- **Data Description:** Entender o quão desafiador é o problema que temos em mãos, conseguiremos responder se temos recursos para trabalhar, quais sãos os tipos de variaveis que temos e a porcentagem de cada uma, a quantidade de dados faltantes e a estatistica descritiva dos dados.

- **Feature Engineering:** Derivação de novas features através das originais, que irão nos ajudar na melhoria do modelo de ML, alem de ser parte importante para a validação das hipoteses levantadas e insights para o negócio.

- **EDA:** Entendimento de como as variáveis impactam no fenomeno de vendas, e qual a força desse impacto. Aqui ganhamos experiência do negócio, validaremos as hipoteses levantadas anteriormente e com isso iremos conseguir ter a percebepção de quais variáveis são importantes para descrever nosso fenomeno.

- **Data Preparation:** Parte onde os dados são preparados para que possam ser recebidos pelo modelo de ML, dados categóricos e numéricos recebem diferentes tratamentos para que posssam ficar em uma escala numérica.

- **Feature Selection:** Selecionando as melhores features para o modelo, utilizando o Boruta.  

- **Machine Learning Modeling:** Treinamento dos principais algoritmos de regressão e validação usando o cross-validation time series. 

- **Hyperparameter Fine Tunning:** Utilizado a tecnica de Random Search para escolher os melhores parametros para performance do algoritmo escolhido.

- **Avaliação do modelo:** Utilizado as metricas de MAE, MAPE e RMSE para checar a performance do algoritmo.

- **Resultados financeiros:** Tradução do resultado do modelo para um resultado financeiro, tornando fácil o entendimento dos resultados.

-  **Deploy para produção:** Criação de um Bot do Telegram que seja capaz de me dar o resultado da predição a partir do numero da loja escolhida. 


## 4.0. Os 5 principais insights do negócio

- ### **H1:** Lojas com sortimentos menores vendem mais 
<h1 align="center"><img alt="rossmann" title="#logo" src="./img/h1.png" /></h1>

- ### **H2:** Lojas com competidores próximos vendem mais
<h1 align="center"><img alt="rossmann" title="#logo" src="./img/h2.png" /></h1>

- ### **H3:** Lojas com promoções muito longas tem queda nas vendas ao longo do tempo
<h1 align="center"><img alt="rossmann" title="#logo" src="./img/h3.png" /></h1>

- ### **H4:** As lojas vendem mais depois do dia 10 de cada mês
<h1 align="center"><img alt="rossmann" title="#logo" src="./img/h4.png" /></h1>

- ### **H5:** As lojas vendem mais no primeiro semestre do ano
<h1 align="center"><img alt="rossmann" title="#logo" src="./img/h5.png" /></h1>


## 5.0. Preparação dos Dados

### 5.1. Dados numericos

- RobustScaler 
- MinMaxScaler

### 5.2. Dados Categoricos

- One Hot Encoder
- Label Encoder
- Ordinal Encoder
- Nature Transformation

## 6.0. Seleção das Variáveis

- Boruta
- Seleção manual 

## 7.0. Modelo de Machine Learning

- Average Model
- Linear Regression
- Linear Regression Regularized Model
- Random Forest Regressor
- XGBoost Regressor

## 8.0. Hyperparameter Fine Tunning

- Random Search

## 9.0. Bussiness Results