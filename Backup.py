## By: Luan Faria

# obter dados
import pandas as pd

dados = pd.read_csv(r'/home/luan/Documentos/Python/inten 3/Aula 3-20210428T232017Z-001/advertising.csv')
print(dados) # VsCode Ou Pycharm
# display(dados) #Jupyter Notebook

# tratamento de dados
print(dados.info())
#display(dados.info())

# análise exploratoria (distribuição e correlação entre itens)
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(dados)  # cria grafico 1
plt.show()  # exibe grafico 1

sns.heatmap(dados.corr(), cmap='Wistia', annot=True)  # cria grafico 2
plt.show()  # exibe grafico 2

# modelagem (IA)
from sklearn.model_selection import train_test_split

x = dados.drop('Vendas', axis=1)
y = dados['Vendas']

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Regressão (linear, arvore de decisão)
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

linear = LinearRegression()  # cria regressão linear
randomforest = RandomForestRegressor()  # cria modelo de arvore de decisão

linear.fit(x_treino, y_treino)  # treina
randomforest.fit(x_treino, y_treino)  # treina

# testando a IA com R² e erro quadratico médio
from sklearn import metrics

teste_linear = linear.predict(x_teste)
teste_random = randomforest.predict(x_teste)

r2_linear = metrics.r2_score(y_teste, teste_linear)  # R²
r2_random = metrics.r2_score(y_teste, teste_random)  # R²
print(r2_linear, r2_random)

erro_linear = metrics.mean_squared_error(y_teste, teste_linear)  # erro
erro_random = metrics.mean_squared_error(y_teste, teste_random)  # erro
print(erro_linear, erro_random)

# visualização gráfica
tabela_comparacao = pd.DataFrame()
tabela_comparacao['Vendas Reais'] = y_teste
tabela_comparacao['Previsão Random'] = teste_random
tabela_comparacao['Previsão Linear'] = teste_linear
tabela_comparacao = tabela_comparacao.reset_index(drop=True)
print(tabela_comparacao)

sns.lineplot(data=tabela_comparacao)
plt.show()

# qual a importancia de cada variavel para vendas
print()
print('Tv,   Radio,   Jornal')
print(randomforest.feature_importances_)
print()


# resultados
resultado = (dados[['TV', 'Radio', 'Jornal']].sum())
print(resultado)
informa = randomforest.feature_importances_
plt.rcParams.update({'font.size': 15})
nome = ['Tv', 'Radio', 'Jornal']
plt.bar(nome, informa )
