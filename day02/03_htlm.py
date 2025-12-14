# %%

import pandas as pd
import requests

#The default of wikipidia API is detected "bots" that access a page a lot of times. Than, you need to pretend that you are making a request with a User-Agent.
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent":"Mozilla/5.0"
}

response = requests.get(url,headers=headers)
response.raise_for_status()

#This method will get all tables of url passed and will put in a list of datasets
dfs = pd.read_html(response.text)

dfs

# %%

#To find the table that you need, search for one each one to find.
df = dfs[1]
df
# %%

df.to_csv("ufs.csv",sep=",")

# %%
