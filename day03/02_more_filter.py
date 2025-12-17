# %%

import pandas as pd
 
df = pd.read_csv("../data/transacao_produto.csv",encoding="latin-1",sep=";")

# %%

#To get transacions where the "idProduto" is 5 ou 11
df[(df["IdProduto"] == "5") | (df["IdProduto"] == "11")]
# or
df[df['IdProduto'].isin(["5","11"])]

# %%

clients = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

clients.head()
# %%

#To get clients with registration date registered
clients[clients["DtCriacao"].notna()]
# or
clients[~clients['DtCriacao'].isna()]

# %%


