#%%

import pandas as pd

# %%

#04.01 - Quantos clientes tem vínculo com a Twitch?
df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

df.head()

df["flTwitch"].sum()

# %%

#04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
df[df["qtdePontos"] > 1000].shape[0]

# %%

#04.03 - Quantas transações ocorreram no dia 2025-02-01?
df[(df["DtCriacao"].dt.year == 2025) & (df["DtCriacao"].dt.month == 2) & (df["DtCriacao"].dt.day == 1) ].shape[0]


# %%
