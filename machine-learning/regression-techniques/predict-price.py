import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error

# -- Carregando e organizando os dados --

# Importando os dados de treinamento que obtivemos do kaggle
dataset = pd.read_csv("train.csv")

# Dados para teste, diretamente é o test_x pois este já vem sem a ultima coluna, que é o valor a ser preditado (y), o preço da casa
test_x = pd.read_csv("test.csv")

# Printar rapidamente as 5 primeiras linhas pra ver se o carregamento foi ok
print(dataset.head())

print("O teste possui uma coluna a menos pois iremos preditar os valores, que é a última coluna faltante.")
print(test_x.head())

# Como o aprendizado é supervisionado, precisamos tirar a ultima coluna (y, o valor que iremos validar a ser preditado)
X_train = dataset.iloc[:,:-1]
y_train = dataset.iloc[:, 1]

# Nao precisamos usar o train_test_split já que temos os dados separados pra treino/teste

# Usando o padrão 0.8/0.2 para treino/teste
# Mas seria realmente necessario dar esse split já que temos dados para teste separados?
#https://www.quora.com/If-I-have-my-training-and-testing-data-on-separate-CSV-files-how-do-I-make-one-of-them-training-data-and-the-other-testing-data-such-that-I-dont-use-train_test_split-as-train_test_split-splits-data-randomly-I-dont
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# -- Analise exploratória dos dados --

# Lembrando que describe só retorna variaveis numéricas
print(dataset.describe())

print("Valores nulos:\n")
print(dataset.isnull().sum())

print("\nValores únicos:\n")
print(dataset.nunique())

print("\nTipos de variáveis:\n")
print(dataframe.dtypes)
#valores faltantes
#plotar valores faltantes
#comparar os dados de saia com dist normal, caso nao bata, transf os dados de input


# Como na regressão linear é necessário normalizar os dados, iremos fazer este tratamento
# Lembrando que a regressão linear é válida SE houver correlação entre as variáveis, então
# Só poderiamos pegar as variáveis que possuem correlação.


# -- Treinamento --

def treinar():
# Ver se vamos de fato usar o mean_sqared_error
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    r2_train = reg.score(X_train, y_train)
    r2_test = reg.score(X_test, y_test)
