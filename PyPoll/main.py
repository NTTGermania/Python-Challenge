# Import the os module
import os

# Module for reading CSV files
import csv

# Store the file path associated with the file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the file "read mode" and store contents in the variable
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')

    print(csvreader)

    csv_header = next(csvreader)

    total_ballots = 0 
    candidates = dict()

    for row in csvreader:
        total_ballots += total_ballots 
       # candidates[row[2]] 
print(candidates[row[2]])
print("Election Results")
print("-"*25)
print("Total Votes:", total_ballots)
print("-"*25)
#for candidate, votes in candidates.items():
    #percentage = votes / total_ballots * 100
    #print("{}: {:.3f}% ({})".format(candidate, percentage, votes)
    