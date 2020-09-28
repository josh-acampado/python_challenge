#import Dependencies
import os
import csv

#Open file path
csvpath = os.path.join( 'Resources','election_data.csv')

#defining variables
total_vote_counter = 0

candidates = []

khan_counter = 0
correy_counter = 0
li_counter = 0
otooley_counter = 0

candidates_percentages = []

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
        if row[2] not in candidates:
            candidates.append(row[2])
        #Votes for each candidate
        if row[2] == "Khan":
            khan_counter = khan_counter + 1
        if row[2] == "Correy":
            correy_counter = correy_counter + 1
        if row[2] == "Li":
            li_counter = li_counter + 1
        if row[2] == "O'Tooley":
            otooley_counter = otooley_counter + 1
    
    #calculate after loop
    khan_percent = round(((khan_counter / total_vote_counter) * 100), 3)
    correy_percent = round(((correy_counter / total_vote_counter) * 100), 3)
    li_percent = round(((li_counter / total_vote_counter) * 100), 3)
    otooley_percent = round(((otooley_counter / total_vote_counter) * 100), 3)

print("Total Votes: " + str(total_vote_counter))