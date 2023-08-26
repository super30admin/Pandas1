#simple passing the tuple to the dataframe constructor/using from_records/pivot the table
import pandas as pd
data=[('rajesh',23,8),('kiran',23,7),('vipin',24,9),('srineet',25,10),('dinesh',26,11)]
df=pd.DataFrame(data,columns=['Name','Age','Score'])
print(df)
records=df.pd.DataFrame.from_records('data',columns=['Name','Age','Score'])
print(records)
pivoting_data=df.pivot()
print(pivoting_data)