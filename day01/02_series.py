# %%

#Before of update of pandas, was necessary to use lists for put values into its and make some methods of statistics.

ages = [34,56,43,23,54,23,57,8,54,3,2,34,6,4,32,45]

average = sum(ages) / len(ages)
print (average)

diffs = 0
for i in ages:
    diffs += (i-average) ** 2

varience = diffs / (len(ages)-1)

# %%

#With the use of Series, is possible to use methods of statistics of own library
import pandas as pd

series_ages = pd.Series(ages)
series_ages

#All values are of the same type

# %%

#Series has some methods

#Method of average of values
avg = series_ages.mean()
avg
#Method of variance of values
var = series_ages.var()
var
#Method of summary (same informations about values)
summary = series_ages.describe()
summary

# %%
