import pandas as pd 
#Problem 1 :
list = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 

df = pd.DataFrame(list,coulmns = ['tag' , 'number'])

#Problem 2 :

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world["population"] >= 25000000) | (world["area"] >= 3000000)]
    return df[['name','area','population']]

#Problem 3 :

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    p_df = products[(products["low_fats"]=="Y") & (products["recyclable"] == "Y")]
    return(pd.DataFrame(p_df,columns = ["product_id"]))

#Problem 4:

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on = 'id',right_on = 'customerId',how = 'left')
    df1 = df['customerId'].isna()
    df = df[df1]

    return pd.DataFrame(df['name']).rename(columns = {'name' : 'Customers'})

 
