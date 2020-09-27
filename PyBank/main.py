#import Dependencies
import os
import csv

#Open file path
csvpath = os.path.join('Resources','budget_data.csv')

#open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
   
    #set header row
    csvheader = next(csvfile)
   
    #Count total number of months
    line = len(list(csvreader))
    print ("Total Number of Months: " + str(line))

    #Total of Profit/Losses
    for row in csvreader:
        print (row)