import os
import csv

# Intialize the variables
poll = []
candidate_votes = {}
previous_votes = 0

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.DictReader(csvfile)
    
    # Create a list of candidates who got votes during the election    
    for row in csvreader:
        poll.append(row["Candidate"])
        
    # Calculate total number of votes cast
    total_votes=len(poll)
    
    for i in poll:
    
        # Create a new dictionary 'candidate_votes' where name of the candidates is the key and vote count is the value
        if i not in candidate_votes:
            candidate_votes[i]=1
        # If the name of the candidate is already in the dictionary just increment its count by 1
        else: 
            candidate_votes[i] = candidate_votes[i] + 1
            
    # Define the path for output text file
    output_path = os.path.join('Resources', 'election results.txt')
    
    # Print and write the election results 
    with open(output_path, 'w') as text_file:
        print ('''Election Results
----------------------------''')
        text_file.write('''Election Results
----------------------------\n''')
        print (f'Total Votes: {total_votes}')    
        text_file.write(f'Total Votes: {total_votes}\n')
        print ('''----------------------------''')
        text_file.write ('''----------------------------\n''')
        for i in candidate_votes:
        
            # Calculate percentage of votes each candidate won
            percent_vote = (candidate_votes[i]/total_votes)*100
            print(f'{i}: {("%.2f" % percent_vote)}% {candidate_votes[i]}')
            text_file.write(f'{i}: {("%.2f" % percent_vote)}% {candidate_votes[i]}\n')
            
            # Find name of the election winner 
            if candidate_votes[i]>previous_votes and i!="":
                winner_name= i
            previous_votes= candidate_votes[i]
            
        print ('''----------------------------''')
        text_file.write ('''----------------------------\n''')
        print(f'Winner: {winner_name}')
        text_file.write(f'Winner: {winner_name}\n')
        print ('''----------------------------''')
        text_file.write ('''----------------------------''')