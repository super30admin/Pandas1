# Create DataFrame from list of lists
import pandas as pd 
	
# List1 
lst = [['Geek', 25], ['is', 30], 
	['for', 26], ['Geeksforgeeks', 22]] 

#creating df object with columns specified 
df = pd.DataFrame(lst, columns =['Tag', 'number']) 
print(df )
#############################################################3

#Create DataFrame from method from_records using list1 and list2
df_records = pd.DataFrame.from_records(lst,columns = ['Tag' , 'number'])

############################################################

#Create DataFrame from method from_dict
data = {'Class' : 's30', 'Pandas': 'by Raj'}

df_dict = pd.DataFrame.from_dict(data, orient = 'columns')