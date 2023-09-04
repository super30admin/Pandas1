import pandas as pd

lst = [['Raghu', 36], ['Chaitanya', 77],
       ['Itachi', 18], ['Naruto', 7]]

df = pd.DataFrame(lst, columns=['Name', 'Roll number'])
print(df)