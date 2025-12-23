#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")

df.head()
# %%

#To group all columns by one value
df.groupby(by=["IdCliente"]).count().reset_index()

# %%

#To group some columns by one value. The result is a series if you put one pair of [], if you put two pais of [], you have a dataframe.
df.groupby(by=["IdCliente"])[["IdTransacao"]].count().reset_index()


# %%

#qtde_transactions
#sum_points
#points / transactions
summary = df.groupby(by=["IdCliente"]).agg(
    {
    "IdTransacao":["count"],
    "QtdePontos":["sum","mean"]
    }
).reset_index()

#To access one column in summary
summary["IdTransacao"]

#To access one columns and a subcolumn onw column
summary["QtdePontos"]["sum"]
#or
summary[("QtdePontos","sum")]
#or you can attribute columns from summary
summary.columns = ["idCliente","qtdeTransacao","totalPontos","avgPontos"]
summary
# %%
