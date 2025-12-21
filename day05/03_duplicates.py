#%%

import pandas as pd

test = pd.DataFrame(
    {
        "name":["teo","lara","nah","bia","mah","lara","mah","mah"],
        "last name": ["calvo","calvo","ataide","ataide","silva","silva","silva","silva"],
        "salary": [2132,1231,454,6543,6532,4322,987,2134]
    }
)

test
# %%

#To remove duplicates. OBS: The all row need to be equal with other row, and when you drop duplicates, it's mainteined only first duplicate row
test.drop_duplicates()

#%%

#or, if you need to mainteined the last duplicate row
test.drop_duplicates(keep="last")

# %%

#To drop row when the data of columns specified is equals.
test.drop_duplicates(subset=["name","last name"])

# %%
