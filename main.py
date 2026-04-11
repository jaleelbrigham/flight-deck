import pandas as pd

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("T_ONTIME_REPORTING.csv")
df = df.drop(columns=[
    'ORIGIN_CITY_MARKET_ID',
    'DEST_CITY_MARKET_ID'
])

df['OP_UNIQUE_CARRIER'].unique()

print(df.sample(25))
print(df.shape)
