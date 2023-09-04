import pandas as pd

# Solution 1

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
        df = customers[~customers['id'].isin(orders['customerId'])]
        return df[['name']].rename(columns={'name': 'Customers'})

#Solution 2

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
        df = customers.merge(orders, left_on = 'id', right_on = 'customerId', how = 'left')
        df = df[df['customerId'].isna()]
        return df[['name']].rename(columns = {'name': 'Customers'})
