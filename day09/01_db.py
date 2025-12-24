#%%

import pandas as pd
import sqlalchemy

# %%
engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")
#%%

clients = pd.read_sql_table(table_name="tb_customers",con=engine)

clients.head()

# %%

#It isn't a good ideia you get all items in your dataframe, so use a query to get some itemns of your dataframe:
query = "SELECT * FROM tb_customers LIMIT 100"

df_100 = pd.read_sql_query(query,con=engine)

df_100
# %%


