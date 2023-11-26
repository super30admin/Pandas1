import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on=['id'], right_on=['customerId'], how='left')
    
    return merged_df[merged_df['customerId'].isna()].loc[:,['name']].rename({'name':'Customers'}, axis=1)