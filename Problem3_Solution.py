import pandas as pd
from pandas import DataFrame, Series

#Madarid = MAD, Barcelona = BCN, Malaga = AGP


#Resorted_data CSV into DataFrame [in chunks]
fixed_df = pd.read_csv('searches.csv', sep='^', chunksize=100000, low_memory=False, usecols=['Date','Destination'], parse_dates=["Date"])
# fixed_df.get_chunk(100000)['ms'] = pd.DatetimeIndex(fixed_df.get_chunk(100000)['Date']).month
# fixed_df.get_chunk()['Date'] = fixed_df.get_chunk()['Date'].map(lambda x: x.month)
# fixed_df = fixed_df

for chunk in fixed_df.get_chunk():
	chunk['ms'] = pd.DatetimeIndex(chunk['Date']).month
	print(chunk)

# fixed_df.get_chunk().join(pd.DatetimeIndex(fixed_df.get_chunk(100000)['Date']).month)

# print(fixed_df.get_chunk(100000))

# print(pd.DatetimeIndex(fixed_df.get_chunk(1000000)['Date']).month)
# dates = pd.DatetimeIndex(fixed_df.get_chunk(100000)['Date'])
# new = Series(dates).apply(lambda x: x.month)
# grouped = fixed_df.get_chunk().groupby(pd.DatetimeIndex(fixed_df.get_chunk(1000000)['Date']).month)
# print(grouped)grouped = fixed_df.get_chunk().groupby(pd.DatetimeIndex(fixed_df.get_chunk(1000000)['Date']).month)
# print(grouped)
# filter = [row for row in fixed_df.get_chunk(10000)['Destination'] if row == 'MAD']
# print(Series(filter))
# print(new)




#Aggregate and Sum
# aggregated_data = fixed_df.get_chunk().groupby('arr_port').sum()

#Sort in descending order by pax and select top 10
# sorted_data = aggregated_data.sort('pax', ascending=0).head(10)

#Choose desires output columns and print
# output = sorted_data[[3]]
# print(output)
