#%%

import pandas as pd
# %%

points = [10,1,1,1,1,50,50,50,10,130,25,50]

values_greater_50 = [value for value in points if value >= 50]
print(values_greater_50)
   
# %%

filter = []

for i in points:
    filter.append(i>=50)

values_greater_50 = []

for i in range(len(points)):
    if filter[i]:
        values_greater_50.append(points[i])

values_greater_50

# %%

test = pd.DataFrame({
    "name": ["teo","nah","mah"],
    "age": [32,35,14],
    "uf": ["sp","pr","rj"]
})

test

# %%

filter = test["age"] > 18
test[filter]

# %%

df = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")

df.head()

# %%

#To get values greater or equal than 50:
df[df["QtdePontos"] >= 50]

# %%

#To get values greater or equal than 50 AND values less or equal than 100
df[(df["QtdePontos"] >= 50) & (df["QtdePontos"] <= 100)]
#You can use the character "&" or "*". it's correct because every values booleans are values of 1 or 0.

# %%

#To get values equal 1 OR values less than 100.
df[(df["QtdePontos"] == 1) + (df["QtdePontos"] <= 100)]
#You can use | or +.

# %%

#To get values between 1 and 50 or transactions in 2025
df[(df["QtdePontos"] >= 1) & (df["QtdePontos"] <= 50) | (df["DtCriacao"] >= '2025-01-01')]

# %%
