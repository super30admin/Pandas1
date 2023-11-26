import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    world_df = world[(world['area']>=3000000) | (world['population']>=25000000)].loc[:,['name','population','area']]
    return world_df