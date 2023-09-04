# with inbuilt replace()
import pandas as pd
df = pd.DataFrame({'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})

# replace the matching strings
df_updated = df.replace(to_replace ='[nN]ew', value = 'New_', regex = True)
# Print the updated dataframe
print(df_updated)


#with customized function with help of re package

import pandas as pd
df = pd.DataFrame({'City':['New York (City)', 'Parague', 'New Delhi (Delhi)', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})

import re
def Clean_names(City_name):
    # Search for opening bracket in the name followed by any characters repeated any number of times
    if re.search('\(.*', City_name):
        # Extract the position of beginning of pattern
        pos = re.search('\(.*', City_name).start()
        # return the cleaned name
        return City_name[:pos]

    else:
        # if clean up needed return the same name
        return City_name


# Updated the city columns
df['City'] = df['City'].apply(Clean_names)

# Print the updated dataframe
print(df)


