#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

df.head()

#%%

#To covert series' type for other type

df["qtdePontos"].dtype

df["qtdePontos"].astype(float)
df["qtdePontos"].astype(str)
#The diference between int64 and int32 is in diference between size of number, if is int64 is 10^64 and int32 is 10^32
df['qtdePontos'].astype("Int64")

# %%

#To covert dates
df["DtCriacao"].replace({
    "0000-00-00 00:00:00.000": 
    "2024-02-01 09:00:00.000"
},inplace=True)
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])


# %%

#To access values into on dates
df["DtCriacao"].dt.year
df['DtCriacao'].dt.day
df['DtCriacao'].dt.date

# %%

#You cann't to tranfor this data for int64 because some values is NaN, that for pandas, are values type float, that cann't to be transformer for int64
df["DtCriacao"].dt.month.astype("int64")
