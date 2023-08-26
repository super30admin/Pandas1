#1st problem
import pandas as pd

df = pd.DataFrame({'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})

index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
		pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]
df.index = index_
print(df)

#Dataframe.replace()
df_updated = df.replace(to_replace ='[nN]ew', value = 'New_', regex = True)
print(df_updated)

#2nd problem
import pandas as pd

df = pd.DataFrame({'City':['New York(city)', 'Parague', 'New Delhi(Delhi)', 'Venice', 'new Orleans'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
					'Cost':[10000, 5000, 15000, 2000, 12000]})

index_ = [pd.Period('02-2018'), pd.Period('04-2018'),
		pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]
df.index = index_
print(df)

import re
def Clean_names(City_name):
	# Search for opening bracket in the name followed by any characters repeated any number of times
	if re.search('\(.*', City_name):
		# Extract the position of beginning of pattern
		pos = re.search('\(.*', City_name).start()

		return City_name[:pos]

	else:
		return City_name
df['City'] = df['City'].apply(Clean_names)
print(df)

