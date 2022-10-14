# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Import module for reading CSV
import csv

#Added to help with math functionality
import statistics

# File locaiton for CSV file
budget_data= os.path.join('Resources','budget_data.csv')

# Definitions
monthCount = 0
total = 0
averageChange = 0
greatestIncrease = 0
monthBest = ''
greatestDecrease = 0
monthWorst = ''
change = []
monthlyChangeByMonth = []
month = []

#Delimites CSV file, reads and skips header file
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)

    #Reading budget data from file after the header 
    for row in csvreader:
        monthCount +=1
        total += int(row[1])
        change.append(int(row[1]))
        month.append(row[0])
 
    #Tracking the changes by month
    for x in range(len(change)-1):
        monthlyChange = (change[x+1] - change[x])
        monthlyChangeByMonth.append(monthlyChange)
        if monthlyChange > greatestIncrease:
            monthBest = month[x+1]
            greatestIncrease = monthlyChange
        elif monthlyChange < greatestDecrease:
            monthWorst = month [x+1]
            greatestDecrease = monthlyChange

    #Formula for the math
    averageChange = statistics.mean(monthlyChangeByMonth)

    #Results of financial analysis
    print("Financial Analysis")
    print("----------------------------")

    print("Total Months: " + str(monthCount)) 
    print("Total: $" + str(total))

    print("Average Change: $" +str(round(averageChange,2)))
    print("Greatest Increase in Profits: " + str(monthBest) + " ($" + str(greatestIncrease) + ")")
    print("Greatest Decrease in Profits: " + str(monthWorst) + " ($" + str(greatestDecrease) + ")")


    # Results creating a text document for analysis results
    f = open("Analysis\Financial_Analysis_Overview.txt" , "w")
       
    f.write("Financial Analysis")
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')

    f.write("Total Months:  " + str(monthCount))
    f.write('\n')
    f.write("Total: $ " + str(total))
    f.write('\n')
    f.write("Average Change: $" +str(round(averageChange,2)))
    f.write('\n')
    f.write("Greatest Increase in Profits: " + str(monthBest) + " ($ "+ str(greatestIncrease) + ")")
    f.write('\n')
    f.write("Greatest Decrease in Profits: " + str(monthWorst) +  "($ "+ str(greatestDecrease) + ")")