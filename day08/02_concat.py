#%%

import pandas as pd

df = pd.DataFrame(
    {
        "Clients":[1,2,3,4,5],
        "Name":["teo",'jose',"nah","mah","lah"]
    }
)

df_02 = pd.DataFrame(
    {
        "Clients":[6,7,8],
        "Name":["kozato","laura","dan"],
        "ages":[34,54,23]
    }
)

df_03 = pd.DataFrame(
    {
        "ages": [34,54,32,3,43]
    }
)


#%%

#Concat serve to join two dataframes, it's kind of the union in sql
dfs = [df,df_02]

pd.concat(dfs)


# %%

#To ignore the indexs of real dataframes
pd.concat(dfs,ignore_index=True)

#%%

#The default of concat is to join one down other
pd.concat([df,df_03])

# I can to change it with parameter:
pd.concat([df,df_03],axis=1)

#But, if you sort values, the index will mess my indexs;
df_03 = df_03.sort_values(by="ages")

#And, if you concat both dataframes, it will concat with index, instead position:
pd.concat([df,df_03],axis=1)

#To concert this:
df_03 = df_03.sort_values(by="ages").reset_index(drop=True)

pd.concat([df,df_03],axis=1)
# %%
