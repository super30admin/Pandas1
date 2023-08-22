'''
1. A Dataframe can be created from a list using the Dataframe's constructor
2. Add the columns which indicate what each row contains
3. We have 5 records which are a list of lists  
'''

import pandas as pd

myLOL = [['PA', 'Pittsburgh', 1], ['AZ', 'Arizona', 2], ['CA', 'California', 3],
        ['MD', 'Maryland', 4], ['TX', 'Texas', 5]]
 
df = pd.DataFrame(myLOL, columns = ['State_Code', 'Name', 'State_ID'])
 
print(df,"\n")

df = df.transpose()
print("Transpose of above dataframe is \n", df)