# Import the os module
import os

# Module for reading CSV files
import csv

# Store the file path associated with the file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the file "read mode" and store contents in the variable

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter =',')

    csv_header = next(csvreader)
    
    # Variables Declaration 
    # List of changes
    changes_list =[]
    months_changes_list= []

    #setting previous to have a null value, Nonetype
    previous = None

    # initialising counters
    sumMonths = 0
    sumProfit = 0
    for row in csvreader:
        # Sum the total number of months in the dataset
        sumMonths = sumMonths + 1
        
        # Sum the total number of profits/losses in the dataset
        sumProfit += float(row[1])
       
        # Calculate the difference in changes in profit/losses and put them in a list
        if (previous is not None):
            months_changes_list.append(row[0])
            changes_list.append(float(row[1])-float(previous))
        previous = float(row[1])
        
    # Calculating the greatest increase and greatest decrease in profits
    greatesti=max(changes_list)
    greatestd=min(changes_list)
    
    # Capturing the indices of the greatest increase and decrease in profits and use them to find the corresponding months of greatest increase and decrease
    month_greatest_increase = months_changes_list[changes_list.index(max(changes_list))]   
    month_greatest_decrease = months_changes_list[changes_list.index(min(changes_list))]
    
    # Finding the average of the changes in profits/losses
    avg = sum(changes_list)/len(changes_list)       
    
    # Printing out results to terminal
    print("Financial Analysis")
    print("-"*25)
    print(f'Total Months: {sumMonths}')
    print(f'Total: ${sumProfit}')
    print(f'Average change: ${(avg)}')
    print(f"Greatest Increase in Profits: {month_greatest_increase} $({greatesti})")
    print(f"Greatest Decrease in Profits: {month_greatest_decrease} $({greatestd})")        

# Writing the results to the text file        
outfile = open('PyBank Analysis', 'w')
outfile.write(("Financial Analysis" +'\n'))
outfile.write("-"*25 +'\n')
outfile.write(f'Total Months: {sumMonths}'+'\n')
outfile.write(f'Total: ${sumProfit}'+'\n')
outfile.write(f'Average change: ${(avg)}'+'\n')
outfile.write(f"Greatest Increase in Profits: {month_greatest_increase} $({greatesti})"+'\n')
outfile.write(f"Greatest Decrease in Profits: {month_greatest_decrease} $({greatestd})"+'\n')  
outfile.close()
