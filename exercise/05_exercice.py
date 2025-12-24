#%%

import pandas as pd

clients = pd.read_csv("../data/clientes.csv",encoding="latin-1",sep=";")

clients.head()

# %%
#06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?

def mean_social_media(line:pd.Series):
    return (line["flEmail"]) + (line["flTwitch"]) + (line["flYouTube"]) + (line["flBlueSky"]) + (line["flInstagram"])

social_media_clients = pd.DataFrame()
social_media_clients["values"] = clients.apply(mean_social_media,axis=1)

social_media_clients.agg(
    {
        "values": ["mean","std","max"]
    }
)


# %%

#06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

transactions = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")

transactions

#%%

clients_transactions = clients.merge(right=transactions, left_on="idCliente",right_on="IdCliente",how="left",suffixes=["Clients","Transactions"] )

clients_transactions = clients_transactions.groupby(["idCliente"])[["IdCliente"]].count().reset_index().sort_values(by="IdCliente",ascending=False)

clients_transactions.head(n=10)

# %%

#06.03 - Qual usuário teve maior quantidade de pontos debitados?
clients.sort_values(ascending=False,by="qtdePontos").head(1)

# %%

#06.04 - Quem teve mais transações de Streak?

transactions = pd.read_csv("../data/transacoes.csv",encoding="latin-1",sep=";")
transactions_products = pd.read_csv("../data/transacao_produto.csv",encoding="latin-1",sep=";")
transactions_products

products = pd.read_csv("../data/produtos.csv",encoding="latin-1",sep=";")

#%%

transactions = transactions.merge(right=transactions_products,on="IdTransacao", 
suffixes=["transacao","transacao_produto"])


transactions = transactions[pd.to_numeric(transactions["IdProduto"],errors="coerce").notna()]

transactions["IdProduto"] = transactions["IdProduto"].astype("int64")

transactions = transactions.merge(right=products,on="IdProduto") 

transactions = transactions[transactions['DescNomeProduto'] == "PresenÃ§a Streak"]

transactions.groupby(["IdCliente"])["IdTransacao"].count().sort_values(ascending=False).head(1)

#%%
#or - this is more fasty to pandas because I filter the values before merge of dataframes.
products = products[products["DescNomeProduto"] == "PresenÃ§a Streak"]

transactions_products = transactions_products[pd.to_numeric(transactions_products["IdProduto"],errors="coerce").notna()]

transactions_products["IdProduto"] = transactions_products["IdProduto"].astype("int64")

transactions.merge(transactions_products,on=["IdTransacao"],how="left").merge(products,on=["IdProduto"],how="right").groupby(by=["IdCliente"])["IdTransacao"].count().sort_values(ascending=False).head(1)
 

# %%
