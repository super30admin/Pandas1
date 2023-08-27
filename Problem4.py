# Problem 4 : Creating a Pandas dataframe using list of tuples

import pandas as pd
data=[('Peter',10,45),
      ('John',67,5),
      ('Mery',87,8)]
df=pd.DataFrame(data,columns=['Name','Age','Height'])
df.pivot('Name','Age','Height')
print(df)