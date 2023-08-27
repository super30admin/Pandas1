# Customer Who Never Order

# By performing a left join and selecting the records where the customerId is null, we can identify customers who do not make an order.

# We use a left join on customers because we want to include all customers from it, regardless of whether they place an order or not.
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df=customers.merge(orders, left_on='id',right_on='customerId',how='left')
    df=df[df['customerId'].isna()]
    df=df[['name']].rename(columns={'name':'Customers'})
    return df