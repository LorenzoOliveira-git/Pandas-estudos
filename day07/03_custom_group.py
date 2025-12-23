#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")

df.head()
# %%
import numpy as np
def crazy_method(x):
    x = pd.Series(x)
    return np.sqrt(((x.max() - x.min()) - x.mean()) ** 2)

def life_time(x):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

summary = (df.groupby(by=["IdCliente"]).agg(
    {
        "IdTransacao":["count"],
        "QtdePontos":["sum","mean",crazy_method],
        "DtCriacao":[life_time]
    }
).reset_index())

summary.columns = ["IdCliente","QtdeTransacoes","Sum_Pontos","Média_pontos","Crazy_Method","Life_time"]
summary


# %%
