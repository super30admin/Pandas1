#Problem 1 Make a Pandas DataFrame with two-dimensional list
import pandas as pd  
       
lst = [[1, 'Taylor', 'Female'], [2,'John','Male'], 
       [3,'Harry','Male'], [4, 'Taylor','Male']] 
      
df = pd.DataFrame(lst, columns =['Id', 'Name','Gender']) 
print(df)

#Problem 2 Creating DataFrame from dict of narray/lists
import pandas as pd  
       
dict={'Id':[1,2,3,4,5],'Name':['Taylor','Dua','Ariana','Selena','Lana']}
      
df = pd.DataFrame(dict) 
print(df)

#Problem 3 : Creating Pandas dataframe using list of lists
import pandas as pd  
       
lst=[[1,'Taylor'],[2,'Selena'],[3,'Ariana']]
      
df = pd.DataFrame(lst,columns=['Id','Name']) 
print(df)

#Problem 4 : Creating a Pandas dataframe using list of tuples
import pandas as pd  
       
tuple=[(1,'Taylor'),(2,'Selena'),(3,'Ariana')]
      
df = pd.DataFrame(tuple,columns=['Id','Name']) 
print(df)

#Problem 5 : Create a Pandas DataFrame from List of Dicts
import pandas as pd  
       
data = [{'Id': 1, 'Name': 'Taylor', 'Age': 32},
        {'Id': 2, 'Name': 'Selena', 'Age': 22}]
      
df = pd.DataFrame.from_records(data,index=['0','1'])
print(df)

#Problem 6 : Replace values in Pandas dataframe using regex
import pandas as pd

data = {'Column1': ['apple123', 'banana456', 'cherry789', 'grape101'],
        'Column2': ['abc123', 'def456', 'ghi789', 'jkl101']}
df = pd.DataFrame(data)
df.replace(r'\d+', '', regex=True, inplace=True)

print(df)