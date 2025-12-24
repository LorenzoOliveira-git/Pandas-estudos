#%%

import pandas as pd

transactions = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")
clients = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

transactions.head()
# %%

transactions.head()
clients.rename(columns={"idCliente":"IdCliente"},inplace=True)

#You need to merge two dataframes to analyse both data in the same time.
transactions.merge(
    right=clients, 
    how="left",
    on="IdCliente",
    suffixes=["Transacao","Cliente"])
#how - it's the type of join (it's the same anything in SQL)
#on - PK and FK
#suffixes - it serves to indicate what is the label of each table, if both has a column in comumn, is easier to indentify what column is for each dataframe.

# %%

#When the PK and FK have different names, use this sintaxe:
transactions.merge(right=clients,left_on=["IdCliente"], right_on=["idCliente"],how="left",suffixes=["transacoes","clientes"])

# %%
