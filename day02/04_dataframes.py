# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

# %%

#Method to view items from the beginning of your dataframe
df_clientes.head(n=10)

# %%

#Method to view end items of your dataframe
df_clientes.tail(n=10)
# %%

#Method to get random items in your dataframe
df_clientes.sample(10)

# %%

#Attribute of dataframe to get the amount of rows and columns. Your result is a tuple.  
df_clientes.shape

# %%

#Attribute of dataframe to view all columns in your dataset.
df_clientes.columns

# %%

#Attribute of dataframe to view indexes of dataframe.
df_clientes.index

# %%

#Method to view some characteristics of dataframe. OBS: memory_usage with "deep" serve to show the real memory used by data of dataframe.
df_clientes.info(memory_usage="deep")

# %%

#Attribute to view types from columns in your dataframe
df_clientes.dtypes.loc["idCliente"]

# %%
