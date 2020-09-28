#import Dependencies
import os
import csv

#Open file path
csvpath = os.path.join( 'Resources','budget_data.csv')

#open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',') 

    #set header row
    csvheader = next(csvfile)

    #defining variables
    month_counter = 0
    profit_value = []

    change_start = 0
    change_value_list = []
    month_value_list = []
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
        #Calculate the change value, store that change 
        change_end = int(row[1])
        change_value_list.append(change_end - change_start)
        month_value_list.append(row[0])
        change_start = int(row[1])

        #Min of Profit/Losses, from month to month
        #Same loop from before, change method in calculations

    #Calculate after loop

    #Profit Sum
    profit_value = list(map(int, profit_value))
    profit_sum = sum(profit_value)

    #Average Change
    change_counter = month_counter - 1 #The number of changes is equal to the total in a list, minus 1
    average_change = (profit_value[-1] - profit_value[0]) / change_counter
    round_average_change = round(average_change, 2)

    #Max Profit Change
    #Identify change max
    change_max = max(change_value_list)
    #Identify index of change max
    change_max_index = change_value_list.index(change_max)
    #Pull value tied to the change_max_index
    month_max = month_value_list[change_max_index]

    #Min Profit Change
    #Identify change min
    change_min = min(change_value_list)
    #Identify index of change min
    change_min_index = change_value_list.index(change_min)
    #Pull value tied to the change_max_index
    month_min = month_value_list[change_min_index]
    
#Print Final Details to Terminal
print("Total Months: " + str(month_counter))
print("Total: $" + str(profit_sum))
print("Average Change: $" + str(round_average_change))
print("Greatest Change in Profits: " + str(month_max) + " " + "($" + str(change_max) + ")")
print("Greatest Decrease in Profits: " + str(month_min) + " " + "($" + str(change_min) + ")")

    