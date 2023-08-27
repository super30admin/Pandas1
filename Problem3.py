# Problem 3 : Creating Pandas dataframe using list of lists 
import pandas as pd
lst=[['Peacock',23,'fly'],['cat',10,'run'],['duck',7,'swim']]
df=pd.DataFrame(lst,columns=['Category','Age','Action'])
print(df)
