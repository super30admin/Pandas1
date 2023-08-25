import pandas as pd


# Method 1: Using pd.DataFrame.from_records()
data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
		{'Geeks':10, 'For': 20, 'geeks': 30}]

df = pd.DataFrame.from_records(data,index=['1', '2'])
print(f'Using from_records \n {df} \n')



# Method 2 : Using pd.DataFrame.from_dict()
df = pd.DataFrame.from_dict(data)
print(f'Using from_dict\n {df} \n')




# Method 3 : Using pd.json_normalize
df = pd.json_normalize(data)
print(f'Using from_normalize\n {df} \n')




# Method 4
data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list', 'Portal': 10000},
        {'Geeks':10, 'For': 20, 'geeks': 30}]

# With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['ind1', 'ind2'], columns=['Geeks', 'For'])

# With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['indx', 'indy'])

print(f'Using the index values for rows \n {df1} \n')

# We get Nan values as entries that have no matching values and columns in the dictionary
print(df2)