#%%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent":"Mozilla/5.0"
}

response = requests.get(url,headers=headers)
response.raise_for_status()

ufsBrazil = pd.read_html(response.text)[1]

ufsBrazil.head()

#%%

ufsBrazil.dtypes

def str_to_float(x:str):
    x = str(x)
    return float(x.replace(" ","")
                 .replace(",",".")
                 .replace("\xa0","")
                 .replace("anos",""))

def perc_to_dec(x:str):
    return round((float(
        x.replace("%","")
        .replace(",",".")
        .replace("‰",""))
        /100),3)

ufsBrazil["Área (km²)"] = ufsBrazil["Área (km²)"].apply(str_to_float)

ufsBrazil["População (Censo 2022)"] = ufsBrazil["População (Censo 2022)"].apply(str_to_float)

ufsBrazil["PIB (2015)"] = ufsBrazil["PIB (2015)"].apply(str_to_float)

ufsBrazil["PIB per capita (R$) (2015)"] = ufsBrazil["PIB per capita (R$) (2015)"].apply(str_to_float)

ufsBrazil["Expectativa de vida (2016)"] = ufsBrazil["Expectativa de vida (2016)"].apply(str_to_float)

ufsBrazil["Alfabetização (2016)"] = ufsBrazil["Alfabetização (2016)"].apply(perc_to_dec)

ufsBrazil["Mortalidade infantil (2016)"] = ufsBrazil["Mortalidade infantil (2016)"].apply(perc_to_dec)

ufsBrazil.head()

# %%

#if: PIB/Capita > 30.000
#*
#Mort infantil < 15/1000
#*
#IDH(2010) > 700
# -> looks like good

#else: looks like no good

df = ufsBrazil.copy()
def mortality_to_float(x:str):
    x = str(x)
    x = float(x
              .replace("‰","")
              .replace(",","."))
    
df["Mortalidade infantil (2016)"] = df["Mortalidade infantil (2016)"].apply(mortality_to_float)

def classify_good(linha):
    linha = pd.Series()
    return (
        (linha["PIB per capita (R$) (2015)"] > 30000) 
        *
        (linha["Mortalidade infantil (2016)"] < 15) 
        * 
        (linha["IDH (2010)"] > 700))

#The parameter axis indicate that the parameter is a row of my dataframe. OBS: The default is axis=0 that means column.
df.apply(classify_good,axis=1)