'''
1. We do not have to specify the column names as the dictionary keys will be assigned as the column names
'''
import pandas as pd

myDict = {
    'State' : ['CA','AZ','PA','MD'], 'Revenue(B$)' : [10,20,15,5]
}
df = pd.DataFrame(myDict)

print(df,"\n")

#Columns are named 0,1,2,.. if not provided any value
print(df.transpose(),"\n")

#Providing indices to df
myDict = {
    'State' : ['CA','AZ','PA','MD'], 'Revenue(B$)' : [10,20,15,5]
}
df = pd.DataFrame(myDict, index =['California','Arizona','Pennsylvania','Maryland'])
print(df)