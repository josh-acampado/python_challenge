#import Dependencies
import os
import csv

#Open file path
csvpath = os.path.join( 'Resources','budget_data.csv')

#open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')