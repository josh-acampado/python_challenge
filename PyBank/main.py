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
    profit_value = []

    change_start = 0

    #start loop
    for row in csvreader:
        #Count total number of months
        if row[0] != " ":
            month_counter = month_counter + 1
        #Sum of Profit/Losses
        profit_value.append(row[1])
            
        #Average Change of Profit/Losses 
        #(calculated after loop)

        #Max of Profit/Losses, from month to month
        #Calculate the change value, store that change and corresponding date into dictionary
        #Be able to identify max change, and use that key to pull the associated value

        #Min of Profit/Losses, from month to month
        #Calculate the change value, store that change and corresponding date into dictionary
        #Be able to identify min change, and use that key to pull the associated value

    #Calculate after loop
    profit_value = list(map(int, profit_value))
    profit_sum = sum(profit_value)

    #Average Change
    change_counter = month_counter - 1 #The number of changes is equal to the total in a list, minus 1
    average_change = (profit_value[-1] - profit_value[0]) / change_counter
    round_average_change = round(average_change, 2)

    
    #Print Final Details
    print("Total Months: " + str(month_counter))
    print("Total: $" + str(profit_sum))
    print("Average Change: $" + str(round_average_change))
    