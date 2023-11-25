import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # df = customers.merge(orders, left_on='id',  right_on='customerId', how='left', indicator=True)
    # df = df[df['customerId'].isna()][['name']]
    # df = df[['name']].rename(columns={'name': 'Customers'})
    # return df

    df = customers[~customers['id'].isin(orders['customerId'])][['name']]
    return df[['name']].rename(columns={'name': 'Customers'})