import pandas as pd
import re

print("PROBLEM 1 \n")
# Problem 1: You are given a dataframe that contains the details about various events in different cities.
# For those cities which start with the keyword ‘New’ or ‘new’, change it to ‘New_’.

# Using Dataframe.replace() Function
# Let's create a Dataframe
df = pd.DataFrame({'City': ['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
                   'Cost': [10000, 5000, 15000, 2000, 12000]})

# Let's create the index
index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
          pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]

# Set the index
df.index = index_

# Let's print the dataframe
print(df)


df = df.replace(to_replace='[nN]ew', value='New_', regex=True)
print(df, "\n")


print("PROBLEM 2")
# Problem 2: You are given a dataframe containing details about various events in different cities.
# The names of certain cities contain some additional details enclosed in a bracket. Search for such names and remove the additional details.


df = pd.DataFrame({'City': ['New York (City)', 'Parague', 'New Delhi (Delhi)', 'Venice', 'new Orleans'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
                   'Cost': [10000, 5000, 15000, 2000, 12000]})


# Let's create the index
index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
          pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]

# Set the index
df.index = index_

# Let's print the dataframe
print(df, "\n")

# Using apply function and a custom function that replaces the extra details in the bracket
def cleanExtras(cityname):

    # Search for opening brace
    if re.search('\(.*', cityname):

        start = re.search('\(.*', cityname).start()

        return cityname[:start]


df['City'] = df['City'].apply(cleanExtras)

print(f'Cleaned df \n {df}')
