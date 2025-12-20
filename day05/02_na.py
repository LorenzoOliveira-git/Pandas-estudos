#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

#%%

#To work with na datas we can use some methods depending your objective

#To drop all rows where has a na data in any column. OBS: it return a view of main dataframe
df.dropna()
#without view
df = df.dropna()
# %%

#Drop na only when the all row is na
df.dropna(how="all")
#Drop na if at least one na. Is default of method
df.dropna(how="any")

#%%

df = pd.DataFrame({
"names": ["Téo",None,"Nah","Marcio"],
"ages": [None,None,43,52],
"salary": [3453,4324,None,5423]
})

#To drop rows where a subset has one na value
df.dropna(how="all",subset=["ages"])

#To drop rows where the value of column "ages" or "names" are na.
df.dropna(how="any", subset=["ages","names"])

# %%
