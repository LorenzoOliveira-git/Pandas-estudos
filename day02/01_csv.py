#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv",sep=";")
df.head()
# %%

#To save a CSV file with indexs
df.to_csv("clientes.csv")

# %%

#To save a CSV indexless file
df.to_csv("clientes.csv",index=False)

# %%

#To save a Parquet File, a file type much used by data analyst
df.to_parquet("clientes.parquet",index=False)

# %%

#To save a Xlsx File
df.to_excel("clientes.xlsx",index=False)

# %%

#To read a Xlsx File
df2 = pd.read_excel("Clientes.xlsx")
df2.head()

# %%


