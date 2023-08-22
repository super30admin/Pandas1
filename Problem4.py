import pandas as pd

cast = [('Jessica', 40, 1),
        ('Louis', 35, 2),
        ('Harvey', 30, 3),
        ('Mike', 24, 4),
        ('Donna', 30, 5)]

# Method 1 : Using Constructor
df = pd.DataFrame(cast, columns=['Name', 'Age', 'ID'])

print(f'Using Dataframe Constructor \n {df} \n')

# Method 2: Using from_records

df = pd.DataFrame.from_records(cast, columns=['Name', 'Age', 'ID'])
print(f'Using from_records \n {df} \n')

# To Pivot the data
df = pd.DataFrame(cast, columns=['Name', 'Age', 'ID'])

pivoted_df = df.pivot(index='ID', columns=['Age'], values=['Name'])
print(f'Pivoted df \n {pivoted_df} \n')
