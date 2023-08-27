# Problem 2 : Creating DataFrame from dict of narray/lists
import pandas as pd
lst={'key':['Dog','cat','fish'],
     'values':[10,20,20]}
df=pd.DataFrame(lst)
print(df)