#import Dependencies
import os
import csv

#Open file path
csvpath = os.path.join('Resources','budget_data.csv')

#open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',') 

    #set header row
    csvheader = next(csvfile)

    #defining variables
    month_counter = 0

    #start loop
    for row in csvreader:
        #Count total number of months
        if row[0] != " ":
            month_counter = month_counter + 1
        #Sum of Profit/Losses

        #Mean of Profit/Losses

        #Max of Profit/Losses, from month to month

        #Min of Profit/Losses, from month to month
    print("Total Months: " + str(month_counter))