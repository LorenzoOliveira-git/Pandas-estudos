#%%
import pandas as pd

ages = [34,56,43,23,54,23,57,8,54,3,2,34,6,4,32,45]

names = ["Téo","Maria","Jose","Luis","Ana","Nah","Dani","Mah","Fer","Nanda","Naty","Nih","Pedro","Kozato","Tito","Tito"]

series_ages = pd.Series(ages)
series_names = pd.Series(names)

# %%

#DataFrame is a group of series
df = pd.DataFrame()

df["Ages"] = series_ages
df["Names"] = series_names

df

# %%

#How do you access columns(Series) in a dataframe?
df["Names"]

# %%

#How do you access rows in a dataframe?
df.iloc[2]

# %%

#How do you access the size of dataframe?
df.index

# %%

#How do you access a column with a position?
df.iloc[0]["Names"]
df.iloc[-1]["Ages"]

# %%


