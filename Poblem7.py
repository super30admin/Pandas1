# Problem 7 :Big Countries	
#To determine whether a country is considered `big`, there are two conditions to verify, as stated in the description:
#The country must have an area of at least three million square kilometers, denoted as area >= 3,000,000.

#The population of the country should be a minimum of twenty-five million, expressed as population >= 25,000,000.


import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df=world[(world['area']>=3000000) |(world['population']>=25000000)]
    return df[['name','population','area']]



    