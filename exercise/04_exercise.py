#%%

import pandas as pd

# %%

#05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

df.head()

df["twitch_points"] = df["qtdePontos"] * df["flTwitch"]

df.head()

# %%

#05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova

import numpy as np

df["pontosLog"] = np.log(df["qtdePontos"])

df.head()

# %%

#05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
df["temUmaRede"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"]	+ df["flBlueSky"] + df["flInstagram"]

df

# %%

#05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
df.sort_values(by="qtdePontos", ascending=False).head(1)["idCliente"]
df.sort_values(by="qtdePontos").head(1)["idCliente"]

# %%

#05.05 - Selecione a primeira transação diária de cada cliente.

df = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")

df.head()

df = df.sort_values(by=["IdCliente","DtCriacao"])
df["Date"] = pd.to_datetime(df["DtCriacao"]).dt.date

df.drop_duplicates(subset=["IdCliente","Date"])

# %%

#EXTRA: descubra qual é o tempo entre as transações do cliente no mesmo dia.

df = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")

df["Date"] = pd.to_datetime(df["DtCriacao"]).dt.date
df = df.sort_values(by="DtCriacao")
first = df.drop_duplicates(subset=["Data","IdCliente"])
last = df.drop_duplicates(subset=["Data","IdCliente"],keep="last")

#Esperar para terminar quando aprender o concat



