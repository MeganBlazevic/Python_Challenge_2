# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Import module for reading CSV
import csv

# File locaiton for CSV file
election_data = os.path.join('Resources', 'election_data.csv')

# Definitions
total = 0
candidates = []
votesPerCandidate ={}

#Delimites CSV file, reads and skips header file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvfile)
    
    #Reading budget data from file after the header 
    for row in csvreader:
        total += 1
        if row [2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1

    #Results of election analysis
    print("Election Results")
    print("----------------------------")

    print("Total Votes: " + str(total))
    print("----------------------------")

    for candidate, votes in votesPerCandidate.items():
        print(candidate + ": " + "{:.3%}".format(votes/total) + " (" + str(votes)+")")
        
    winner = max(votesPerCandidate,key=votesPerCandidate.get)

    print("----------------------------")
    print(f"Winner: {winner}") 
    print("----------------------------")
      
    # Results creating a text document for analysis results
    f = open("Analysis\Election_Results_Overview.txt" ,"w")

    f.write("Election Results")
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')

    f.write("Total Votes: " + str(total))
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')

    for candidate, votes in votesPerCandidate.items():
        f.write(candidate + ": " + "{:.3%}".format(votes/total) + " (" + str(votes)+")""\n")

    winner = max(votesPerCandidate,key=votesPerCandidate.get)
    #f.write('\n')

    f.write("----------------------------")
    f.write('\n')
    f.write(F"Winner: {winner}") 
    f.write('\n')
    f.write("----------------------------")