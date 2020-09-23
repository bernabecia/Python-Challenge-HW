import os
import csv

#List to store data
# Voter_ID = []
# County =  []
# Candidate = []

# Read in the CSV file
with open(PyPoll_Resources_election_data.csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(next(csvreader))

with open(PyPoll_Resources_election_data.csv,"w") as csvfile:
    for row in csvreader:
        row_num  = row_num +1
total_votes = row_num-1
print(f"Total Votes: {total_votes}")






