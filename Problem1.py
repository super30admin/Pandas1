'''
1. A Dataframe can be created from a list using the constructor Dataframe
2. Add the columns which indicate what each row contains 
'''

import pandas as pd

mylist = [["Adam",1,24],["Maggie",2,30],["Meghan",3,40]]
df = pd.DataFrame(mylist,columns=["Name","ID","Age"])
print(df)

