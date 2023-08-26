#1st method:
import pandas as pd

first=[['knowledge',25],['is',30],['power',50]]
df=pd.DataFrame(first,columns=['Tag','score'])
print(df)


#2nd method:
import pandas as pd
second=[['rajesh','kaireddy',23],['kiran','konda',24],['vipin','mamidi',25],['dinesh','potalapati',26],['nithin','dornipadu',27],['srineet','srigiri',28]]
df=pd.DataFrame(second,columns=['first_name','last_name','marks'],dtype=float)
print(df)