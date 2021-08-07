# Previsao_De_Vendas
[![NPM](https://github.com/LuanFaria/Previsao_De_Vendas/blob/main/LICENSE)

# Sobre o projeto

Nosso desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios nas 3 grandes redes de comunicação: TV, Jornal e Rádio

Passo a Passo de um Projeto de Ciência de Dados

    Passo 1: Entendimento do Desafio
    Passo 2: Entendimento da Área/Empresa
    Passo 3: Extração/Obtenção de Dados
    Passo 4: Ajuste de Dados (Tratamento/Limpeza)
    Passo 5: Análise Exploratória
    Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
    Passo 7: Interpretação de Resultados

Importar a Base de dados

[advertising.csv](https://github.com/LuanFaria/Previsao_De_Vendas/files/6949114/advertising.csv)


Análise Exploratória

    Visualizar como as informações de cada item estão distribuídas.
    Correlação entre cada um dos itens.
    
    
![image](https://user-images.githubusercontent.com/85500922/128602702-4df7377f-02c6-447c-b7e0-5960b254a3ac.png)

![image](https://user-images.githubusercontent.com/85500922/128602707-de2cb33f-3eb4-455c-8238-d1fa634828fd.png)
    
    
Preparação dos dados para treinarmos o Modelo de Machine Learning

    Separando em dados de treino e dados de teste

Modelos de regressão

    Regressão Linear
    RandomForest (Árvore de Decisão)

Teste da AI e Avaliação do Melhor Modelo

    Usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece...
    Também vamos olhar o MSE (Erro Quadrático Médio) -> diz o quanto o nosso modelo "erra" quando tenta fazer uma previsão


# Visualização Gráfica das Previsões

![image](https://user-images.githubusercontent.com/85500922/128603036-18d1c4da-d70a-4467-b3fa-25f385d6ae1a.png)


# Qual a importância de cada variável para as vendas?


TV        29408.5  (87,12%)
Radio      4652.8  (11,53%)
Jornal     6110.8  (1,3%)


![image](https://user-images.githubusercontent.com/85500922/128602734-52070b5a-cf35-44a5-8b1c-84a0f843bf55.png)




# Tecnologias utilizadas
## Back end e Front end
- Python 3
- Jupyter Notebook
- IA
- Tratamento de dados


## Bibliotecas Python
- Pandas
- Seaborn
- matplotlib.pyplot
- sklearn
- sklearn.ensemble 
- sklearn.linear_model
- sklearn.model_selection

# Autor

By: Luan Donizete Faria
https://www.linkedin.com/in/luandonizetefaria/


