import pandas as pd
data=[['Boston',100],['is',50],['beautiful',80],['city',75]]
df=pd.DataFrame(data, columns=['Name','Marks'])
print(df)

#Defining column names using Dataframe.columns() function 
import pandas as pd
data=[[1,2,3],[4,5,6],[7,8,9]]
df=pd.DataFrame(data)
df.columns=['column_1','column_2','column_3']
print(df,"\n") #It creates additional new line afte the end of dataframe
Transpose_data=df.transpose()