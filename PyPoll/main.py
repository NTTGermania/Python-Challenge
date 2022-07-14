# Import the os module
from ast import In, Not
import os

# Module for reading CSV files
import csv

# Store the file path associated with the file
csvpath = os.path.join('Resources', 'election_data.csv')

# Open the file "read mode" and store contents in the variable
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')

    csv_header = next(csvreader)

    total_ballots = 0 
    candidates = dict()
    name = None
    # Make it a default dict
    d = dict()
    for row in csvreader:
        total_ballots = total_ballots + 1
        
        if (name != row[2]):
            name = row[2]
            if (name not in candidates):
                candidates[name] = 1
            else: 
                candidates[name] += 1
        else:
            candidates[name] += 1
        
           
print("Election Results")
print("-"*25)
print("Total Votes:", total_ballots)
print("-"*25)
for candidate, votes in candidates.items():
    percentage = votes / total_ballots * 100
    print("{}: {:.3f}% ({})".format(candidate, percentage, votes))
print("-"*25)
print(f'Winner: {max(candidates, key=candidates.get)}')
print("-"*25)

outfile = open('PyPoll Analysis', 'w')
outfile.write("Election Results" + '\n')
outfile.write("-"*25 + '\n')
outfile.write(f'Total Votes: {total_ballots}' + '\n')
outfile.write("-"*25 + '\n')
for candidate, votes in candidates.items():
    percentage = votes / total_ballots * 100
    outfile.write("{}: {:.3f}% ({})".format(candidate, percentage, votes)+ '\n')
outfile.write("-"*25 + '\n')
outfile.write(f'Winner: {max(candidates, key=candidates.get)}'+ '\n')
outfile.write("-"*25 +'\n')      