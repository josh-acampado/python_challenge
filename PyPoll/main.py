#import Dependencies
import os
import csv

#Open file path
csvpath = os.path.join( 'Resources','election_data.csv')

#defining variables
total_vote_counter = 0

#open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #set header row
    csvheader = next(csvfile)

    #start loop
    for row in csvreader:
        #Total Votes
        if row[0] != " ":
            total_vote_counter = total_vote_counter + 1
        #List of unique candidates

print("Total Votes: " + str(total_vote_counter))