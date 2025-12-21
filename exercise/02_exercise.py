#%%

import pandas as pd

# %%

#03.01 - Quantas linhas há no arquivo clientes.csv ?
df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")
df.shape[0]

# %%

#03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
df = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")
df.dtypes[df.dtypes == int].count()

# %%

#03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
df = pd.read_csv("../data/produtos.csv",encoding="latin-1",sep=";")
df.dtypes[df.dtypes == object].count()

# %%

#03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")
df.head()
df["idCliente"].loc[4]

# %%

#03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?
df.head()
df['qtdePontos'].iloc[9]

# %%
