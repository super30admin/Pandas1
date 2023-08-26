import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  df=customers.merge(orders,left_on='id',right_on='customerId',how='left')
  Null_values= df[df['customerId'].isnull()]
  return Null_values[['name']].rename(columns={'name':'Customers'})



