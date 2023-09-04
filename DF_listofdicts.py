import pandas as pd

data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks': 10, 'For': 20, 'geeks': 30}]

df1 = pd.DataFrame(data, index=['ind1', 'ind2'],
                   columns=['Geeks', 'For'])
#prints only 2 columns with ind1 and ind2 as indices
print(df1)

df2 = pd.DataFrame(data, index=['indx', 'indy'])
#print all the 3 columns with indx and indy as indices
print(df2)