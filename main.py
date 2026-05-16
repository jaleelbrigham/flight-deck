import pandas as pd

# flight deck 🌴
# baseline delay metrics script
# analyzes airline on-time performance data

#load airline dataset
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("T_ONTIME_REPORTING.csv")
df = df.drop(columns=[
    'ORIGIN_CITY_MARKET_ID',
    'DEST_CITY_MARKET_ID'
])

#calculate baseline delay stats
total_flights = df.shape[0]
late_departures = df[df['DEP_DELAY'] > 0].shape[0]
delay_rate = (late_departures / total_flights) * 100

#print results
print("Total Flights: ", total_flights)
print("Late Departures: ", late_departures)
print("Delay Rate: ", round(delay_rate, 2), "%")
