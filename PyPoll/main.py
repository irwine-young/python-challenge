import os
import csv

election_data_csv = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')  # Specify path to collect election_data.csv file from Resources folder of PyPoll

votes = []                                                                          # Create 'votes' list to store votes
candidate = []                                                                      # Create 'candidate' list to store candidates

with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')                                  # Read csv including the header row, split the data by commas
    header = next(csvreader)                                                        # Set variable to store header row
    total_votes = int(len(list(csvreader)))                                         # Calculate the total number of votes in the csv file
    
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')                              # Read csv without the header row, split the data by commas    
    for row in csvreader:                                                           # Use 'for loops' to go through rows to add values into the 'candidate' list               
        candidate.append(row['Candidate'])                                          # Add each candidate to 'candidate' list
    unique_candidate = sorted(list(set(candidate)))                                 # Set variable to determine unique candidate sorted alphabetically, [0] = Charles, [1] = Diane, [2] = Raymon

charles_counter = 0                                                                 # Set counters to 0
diana_counter = 0                                                                   # Set counters to 0
raymon_counter = 0                                                                  # Set counters to 0

with open(election_data_csv, 'r') as csvfile:                                       # Read csv without the header row, split the data by commas    
    results = csv.DictReader(csvfile)

    for row in results:                                                             # Add each candidate to 'candidate' list
        candidate.append(row['Candidate'])
        
        if row['Candidate'] == unique_candidate[0]:                                 # If the row contains a vote for unique_candidate[0] = Charles, add to the charles vote counter
            charles_counter = charles_counter + 1

        elif row['Candidate'] == unique_candidate[1]:                               # If the row contains a vote for unique_candidate[1] = Diana, add to the diana vote counter
            diana_counter = diana_counter + 1

        elif row['Candidate'] == unique_candidate[2]:                               # If the row contains a vote for unique_candidate[2] = Raymon, add to the raymon vote counter
            raymon_counter = raymon_counter + 1

    percent_charles= round((charles_counter/total_votes)*100,3)                     # Calculate the percentage of votes for charles
    percent_diana = round((diana_counter/total_votes)*100,3)                        # Calculate the percentage of votes for diana
    percent_raymon = round((raymon_counter/total_votes)*100,3)                      # Calculate the percentage of votes for raymon

print(f'Election Results' + "\n")                                                   # Print results, "/n" for extra spacing
print(f'-------------------------------' + "\n")
print(f'Total Votes: {total_votes}' + "\n")
print(f'-------------------------------' + "\n")
print(f'{unique_candidate[0]}: {percent_charles}% ({charles_counter})' + "\n")
print(f'{unique_candidate[1]}: {percent_diana}% ({diana_counter})' + "\n")
print(f'{unique_candidate[2]}: {percent_raymon}% ({raymon_counter})' + "\n")
print(f'-------------------------------' + "\n")

if charles_counter > diana_counter and charles_counter> raymon_counter:             # Define if statement to declare the winner by popular vote, comparing charles_counter, diana_counter and raymon_counter and print the winner
    print(f'Winner: ' + unique_candidate[0] + "\n")

elif diana_counter > charles_counter and diana_counter > raymon_counter:
    print(f'Winner: ' + unique_candidate[1] + "\n")

elif raymon_counter > charles_counter and raymon_counter > charles_counter:
    print(f'Winner: ' + unique_candidate[2] + "\n") 

print(f'-------------------------------')

ed_txt = os.path.join('..', 'PyPoll', 'analysis', 'election_data.txt')              # Print results into a new textfile in the analysis folder under PyBank Folder

with open(ed_txt, 'w') as txt:
    txt.write(f'Election Results' + "\n" + "\n")
    txt.write(f'-------------------------------' + "\n" + "\n")
    txt.write(f'Total Votes: {total_votes}'+ "\n" + "\n") 
    txt.write(f'-------------------------------' + "\n" + "\n")
    txt.write(f'{unique_candidate[0]}: {percent_charles}% ({charles_counter})' + "\n" + "\n")
    txt.write(f'{unique_candidate[1]}: {percent_diana}% ({diana_counter})' + "\n" + "\n")
    txt.write(f'{unique_candidate[2]}: {percent_raymon}% ({raymon_counter})' + "\n" + "\n")
    txt.write(f'-------------------------------' + "\n" + "\n")
    if charles_counter > diana_counter and charles_counter> raymon_counter:         # Define if statement to declare the winner by popular vote, comparing charles_counter, diana_counter and raymon_counter and print the winner
        txt.write(f'Winner: ' + unique_candidate[0] + "\n" + "\n")

    elif diana_counter > charles_counter and diana_counter > raymon_counter:
        txt.write(f'Winner: ' + unique_candidate[1] + "\n" + "\n")

    elif raymon_counter > charles_counter and raymon_counter > charles_counter:
        txt.write(f'Winner: ' + unique_candidate[2] + "\n" + "\n")
        
    txt.write(f'-------------------------------')