print ("Program to count Lines in CSV");

import csv

##Open and read bookings.csv and count no. of lines
print ("\nLines in bookings.csv")
with open('bookings.csv', 'r') as csv_bookings:
    count_bookings = sum(1 for line in csv_bookings)
print (count_bookings);

##Open and read searches.csv and count no. of lines
print ("\nLines in searches.csv")
with open('searches.csv', 'r') as csv_searches:
    count_searches = sum(1 for line in csv_searches)
print (count_searches);
