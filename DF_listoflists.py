import pandas as pd

data = [['DS', 'Linked_list', 10], ['DS', 'Stack', 9], ['DS', 'Queue', 7],
        ['Algo', 'Greedy', 8], ['Algo', 'DP', 6], ['Algo', 'BackTrack', 5], ]

df = pd.DataFrame(data, columns=['Category', 'Name', 'Marks'])
print(df)