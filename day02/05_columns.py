# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv",sep=";")
# %%

df.shape[0]
# %%

df.info(memory_usage="deep")
# %%

df.dtypes

# %%

#Method to rename columns from a dataframe. OBS: the return of method is a dataframe, in other words, the change isn't in dataframe, the method makes a new dataframe.
df.rename(columns={"QtdePontos":"QtdPontos"})

df = df.rename(columns={
    "QtdePontos":"QtdPontos",
    "DescSistemaOrigem": "SistemaOrigem"
})

df.rename(columns={
    "QtdPontos": "QtdePontos",
    "SistemaOrigem" : "DescSistemaOrigem"
},inplace=True)

df
# %%

#It gets a column(s) of your dataframe
df["IdCliente"]

df[["IdCliente","QtdePontos"]]

df[["IdCliente"]]

df[[]]

# %%

#SELECT IdCliente FROM df
df[["IdCliente"]]

# %%

#SELECT IdCliente, QtdePontos FROM df LIMIT 5
df[["IdCliente","QtdePontos"]].sample(5)

# %%

#How do I reogarnize my columns own dataframe?

df = df[["IdCliente","QtdePontos","IdTransacao"]]

#or

columns = df.columns.tolist()
columns.sort()

df = df[columns]
