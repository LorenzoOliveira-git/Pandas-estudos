#%%
import pandas as pd

ages = [34,56,43,23,54,23,57,8,54,3,2,34,6,4,32,45]

series_ages = pd.Series(ages)

#%%

ages[-1]

# The index of series is the same of keys of dictionaries.
#Series access by index is wrong, because if you change position of values on the series, the index will be not the position, but a key of value
series_ages[0]

# %%

series_ages = series_ages.sort_values()

#With method iloc, you will get value by position and no by index(own key)
series_ages.iloc[-1]

# %%

series_ages[0:3]

# %%

series_ages[::-1]
# %%

ages = [34,56,43,23,54,23,57,8,54,3,2,34,6,4,32,45]

len(ages)

#%%

indexs = ["Téo","Maria","Jose","Luis","Ana","Nah","Dani","Mah","Fer","Nanda","Naty","Nih","Pedro","Kozato","Tito","Tito"]

series_ages = pd.Series(ages,index=indexs)
# %%

#The iloc serves to navigate in rows
series_ages["Tito"]
series_ages.iloc[0:2]
# %%

#The loc serves to navigate in indexs
series_ages.loc["Tito"]

# %%
