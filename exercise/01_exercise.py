#%%

import pandas as pd


#%%

#1.1 - Leia o arquivo transacoes.csv com a formatação correta;
df = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")

df.head()
# %%

#1.2 - Adicione uma coluna com valores 1;
df["values"] = 1
df.head()

# %%

#1.3 - Salve o dataframe com nome: transacoes_1.csv
df.to_csv("../data/transacoes_1.csv")

