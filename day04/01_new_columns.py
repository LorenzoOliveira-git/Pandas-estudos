#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")
df.head()
# %%

#To make a new column to sum 100 points for each client
df["pontos100"] = df["qtdePontos"] + 100

df.head()

# %%

#To make a new column with a verification if the client has email or twitch 
df["Email_ou_Twitch"] = df["flEmail"] + df["flTwitch"]

df.head()
# %%

#To make a new column with a verification if the client has email and twitch
df["Email_e_twitch"] = df["flEmail"] * df["flTwitch"]

#%%

#To make a new column with the verification to know how many social midia the client has.
df["Quantidade_Redes_sociais"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flBlueSky"]

df.head()

# %%

#To make a new column to know if the people has at least one social midia.
df["Todas_Rede_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flBlueSky"]

df.head()

# %%

import numpy as np

#To make a new column to tranform points in log.
df["pontosLog"] = np.log(df["qtdePontos"] + 1)

import matplotlib.pyplot as plt

plt.hist(df["pontosLog"])
plt.grid()
plt.show()

# %%
