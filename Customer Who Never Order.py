import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how='left', left_on='id', right_on='customerId')
    result_df = df[df['customerId'].isnull()][['name']]
    return result_df.rename(columns={'name': 'Customers'})
