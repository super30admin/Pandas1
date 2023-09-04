import pandas as pd

data = [('Peter', 18, 7), ('Riff', 15, 6), ('John', 17, 8), ('Michel', 18, 7), ('Sheli', 17, 5)]
df = pd.DataFrame(data, columns=['Name', 'Age', 'Score'])
print(df)