#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

df.head()

#%%

#Every filter in pandas ISN'T a copy of dataset, instead it is going to point to rows when condition is TRUE. This is important because if you copy dataframe, the memory of dataframe also will double. If you change any row, you are changing the real dataframe too.
df[df["qtdePontos"] == 0]

df_0 = df[df["qtdePontos"] == 0]

df_0["flag_1"] = 1

# %%

#It's the same for lists in python
A = [1,2]
B = A
print("A: ",A)
print("B: ",B)

B.append("Hello")
print("A: ",A)
print("B: ",B)

#For solving this "problem", You can use this method:
B = A.copy()

#%%
#It's the same for pandas:
df_1 = df[df["qtdePontos"] == 0].copy()

df_1["flag_1"] = 1
# %%
