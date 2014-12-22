# ** Using Pandas **
import pandas as pd

#Resorted_data CSV into DataFrame [in chunks]
fixed_df = pd.read_csv('bookings.csv', sep='^', chunksize=1000000, low_memory=False, usecols=["arr_port","pax","year"])

#Aggregate and Sum
aggregated_data = fixed_df.get_chunk().groupby('arr_port').sum()

#Sort in descending order by pax and select top 10
sorted_data = aggregated_data.sort('pax', ascending=0).head(10)

#Choose desires output columns and print
output = sorted_data[[0]]
print(output)
