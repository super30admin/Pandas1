#Using pd.DataFrame() function to create the dataframe from the list
import pandas as pd
data={'category':['list','tuple','set','dict'],'values':[20,21,22,23]}
df=pd.DataFrame(data)
print(df)

#Using Pandas Dataframe with the index parameter
import pandas as pd
dat={'category':['cricket','badminton','swimming'],'rajesh':[10,7,10]}
df=pd.DataFrame(data,index=['outdoor','indoor/outdoor','indoor'])
print(df)

