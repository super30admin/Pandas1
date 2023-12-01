import pandas as pd  
     
# List1  
lst = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 
 
# creating df object with columns specified    
df = pd.DataFrame(lst, columns =['Tag', 'number']) 
print(df )