import pandas as pd   
      

lst = [['Apple', 5], ['Orange', 3],  
       ['guava', 4], ['rambutan', 6]]  
  
   
df = pd.DataFrame(lst, columns =['Fruit', 'Price'])  
print(df )