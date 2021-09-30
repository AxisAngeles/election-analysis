### PSEUDO CODING
#The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recevived votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#-------------------------------------------------------------------------------

# 1) # Add csv and os modules.
import csv
import os

# 2) Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# 3) Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

    # 8) Add an accumulator variable
total_votes=0

    # 11) Adding a candidate variable (lists)
candidate_options = []

    # 15) Creating a DICTIONARY with Candidates (Key) and Votes (Values)
candidate_votes = {}

# 4) Open the election results and read the file.
with open(file_to_load) as election_data:

    # 5) Read the file object with the reader function.

    file_reader = csv.reader(election_data)
    
    # 6) Print header row.
    headers = next(file_reader)
    #print(headers)

    # 7) Print each row in te csv file.
    #for row in file_reader:
        #print(row)

#-------------------------------------------------------------------------------
### COUNTING VOTES
    # 8) Add an accumulator variable - before oppening the file.
    
    # 9) Increase accumulator variable +1 for each row.
    for row in file_reader:
        # 9.1) Add to the total vote count.
        total_votes += 1
     
    # 10) Print total votes.
    #print(f'Total votes: {total_votes:,}.')

#-------------------------------------------------------------------------------
### GETTING CANDIDATES NAMES
    # 11) Adding a candidate variable (lists) - before oppening the file.
    
    # 12) Print the candidate name from each row
        candidate_name = row[2]
    # 13) Add candidate name to the candidate options list.
    # 14) Only adding unique names with an if statment using not in.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

#print(candidate_options)

#-------------------------------------------------------------------------------
### GETTING EACH CANDIDATE'S VOTES

    # 15) Creating a DICTIONARY with Candidates (Key) and Votes (Values) - before oppening the file.

    # 16) Initialize vote count for each Candidate (Key)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

#print(candidate_votes)

#-------------------------------------------------------------------------------
### GETTING EACH CANDIDATE VOTE PERCENTAGE

# 17) Get each candidates name
for candidate in candidate_options:
    # 18) For each candidate get their respective votes
    print(f'{candidate} has {candidate_votes[candidate]:,} votes; equal to {candidate_votes[candidate]/total_votes*100:3.3}%.')

