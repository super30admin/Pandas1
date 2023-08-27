# Problem 1 : Make a Pandas DataFrame with two-dimensional list

import pandas as pd
data=[['northeastern',25],['is',8],['great',45]]
df=pd.DataFrame(data,columns=['key','value'])
print(df)