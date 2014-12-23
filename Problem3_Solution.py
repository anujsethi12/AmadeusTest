# Graph using Pandas
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('searches.csv', 'r') as f:
	reader = csv.reader(f, delimiter='^')
	i=0
	next(reader)	#skip headers
	data = []
	for i in range(0,1000000):			#processing limited rows because personal notebook computer is not able to process such a huge data
		data.append(next(reader))		#append data
		i=i+1

# Filter Data based on destination and populate new data structure with format: Month, Destination, integer value 1(will be later added up to count number of searches)

MAD = []	#Madarid = MAD
BCN = []	#Barcelona = BCN
AGP = []	#Malaga = AGP

for row in data:
	if row[6] == "MAD":
		row[0] = row[0][5:7]	#Fetch only month by selecting sub-string
		MAD.append([row[0],row[6],1])
	if row[6] == "BCN":
		row[0] = row[0][5:7]
		BCN.append([row[0],row[6],1])
	if row[6] == "AGP":
		row[0] = row[0][5:7]
		AGP.append([row[0],row[6],1])

# Group by months, add up search values and plot graph

df_MAD = pd.DataFrame(MAD,columns=['Month', 'Destination', 'SearchCount'])
aggregated_MAD = df_MAD.groupby('Month').sum()	# Aggregate and Sum
plt.plot(aggregated_MAD, label='Madarid')		# Plot graph
print("\nMonthly Search for Madarid-MAD:\n")
print(aggregated_MAD)							# Print values to console output

df_BCN = pd.DataFrame(BCN,columns=['Month', 'Destination', 'SearchCount'])
aggregated_BCN = df_BCN.groupby('Month').sum()
plt.plot(aggregated_BCN, label='Barcelona')
print("\nMonthly Search for Barcelona-BCN:\n")
print(aggregated_BCN)

df_AGP = pd.DataFrame(AGP,columns=['Month', 'Destination', 'SearchCount'])
aggregated_AGP = df_AGP.groupby('Month').sum()
plt.plot(aggregated_AGP, label='Malaga')
print("\nMonthly Search for Malaga-AGP:\n")
print(aggregated_AGP)

# Set graph properties
bar_width = 0
n_groups = 12
index = np.arange(n_groups)
plt.xticks(index + bar_width, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
plt.legend(loc='upper right')
plt.title('Number of Searches per month')
plt.show()
