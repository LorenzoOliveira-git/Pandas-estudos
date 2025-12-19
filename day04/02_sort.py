#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

# %%

#To get person with greater amount of points
df[df["qtdePontos"].max() == df["qtdePontos"]]
#or
df.sort_values(by="qtdePontos").tail(n=1)
#or
df.sort_values(by="qtdePontos",ascending=False).head(n=1)

# %%

#To get the 5 Id's people with greater amount of points.
filter = (df["idCliente"].isin(df.sort_values(by="qtdePontos",ascending=False)
 .head(5)["idCliente"].tolist()))
df[filter]

# %%

df_test = pd.DataFrame(
    {
        "names:": ["teo","ana","nah","jose"],
        "ages": [32,43,35,42],
        "salary": [2345,4533,3245,4533]
    }
)

df_test.head()

# %%

#This case, the sort serve to sort the values with 2 variables
df_test.sort_values(by=["salario","ages"], ascending=False)

#%%

#In this case, I can sort the values with salary in descending order and the ages in ascending order.
df_test.sort_values(by=["salary","ages"], ascending=[False,True])