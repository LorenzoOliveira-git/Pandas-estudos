#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

df.head()
# %%

idClient = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"

def get_last_id(x:str):
    return x.split("-")[-1]

new_id = []

for i in df["idCliente"]:
    new_id.append( get_last_id(i) )

new_id
# %%

#instead to make what I do up there, we can use the method APPLY to apply a function in a series of your dataframe.
#The function don't receive parameter directly because the parameters are the values in series.
df["idCliente"].apply(get_last_id)

# %%
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent":"Mozilla/5.0"
}

response = requests.get(url,headers=headers)
response.raise_for_status()

ufsBrazil = pd.read_html(response.text)[1]

ufsBrazil.head()

# %%
