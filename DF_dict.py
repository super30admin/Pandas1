import pandas as pd

data = {'Category': ['Array', 'Stack', 'Queue'],
        'Marks': [20, 21, 19]}
df = pd.DataFrame(data)
print(df)

data1 = {'Category': ['Array', 'Stack', 'Queue'],
        'Student_1': [20, 21, 19], 'Student_2': [15, 20, 14]}

df2 = pd.DataFrame(data1)
print(df2.transpose())