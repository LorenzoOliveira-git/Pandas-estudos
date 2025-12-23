#%%

import pandas as pd

ages = [34,5,43,23,23,54,5,6,78,65,43,32,34,62]

ages = pd.Series(ages)

ages
# %%

#Sum
ages.sum()

# %%

#Minimum
ages.min()

# %%

#Maximum
ages.max()

# %%

#Mean
ages.mean()

# %%

#Some statistics
ages.describe()

# %%

df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")
df.head()
# %%

df["flTwitch"].sum()
df["flTwitch"].mean()

# %%
#If you put a dataframe in a statistic method, you get the number of each column.
social_medias = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]

df[social_medias].mean()
# %%

num_columns = df.dtypes[~(df.dtypes == "object")].index.tolist()

df[num_columns].mean()
df[num_columns].describe()
# %%
