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
    sumCharles = sumDiana = sumRaymon = 0
    candidates = dict()
    candidates_list = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
    candidates["names"] = candidates_list
    votes_list = [sumCharles , sumDiana , sumRaymon]
    candidates["votes"] = votes_list

    for row in csvreader:
        total_ballots = total_ballots + 1
        if (row[2] == "Charles Casper Stockham"):
            sumCharles = sumCharles + 1
        if (row[2] == "Diana DeGette"):
            sumDiana = sumDiana + 1
        if (row[2] == "Raymon Anthony Doane"):
            sumRaymon = sumRaymon + 1
    
    print(candidates)
    print(total_ballots)