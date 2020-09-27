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

    #Define starting variable
    profit_sum = 0
    #Sum of Profit/Losses
    
    
    #Mean of Profit/Losses, sum/total months

    #Max of Profit/Losses from month to month

    #Min of Profit/Losses from month to month
    
    #Print final results
    print ("Total Number of Months: " + str(line))
    print("Total: $" + str(profit_sum))