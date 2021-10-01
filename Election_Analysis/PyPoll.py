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

    # 19) Declare winning count and winning candidate variables.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

# 22) Open text file with "w" to write on it.
with open(file_to_save, "w") as txt_file:

    # 23) Print the final vote count to the terminal.
    election_results = (
        f'\nElection Results\n'
        f'{"-"*25}\n'
        f'Total votes: {total_votes:,}\n'
        f'{"-"*25}\n'
    )
    print(election_results, end="") #The "end" parameter is added to ensure that nothing will be printed on the last line
    # Save the final vote count to the text file.
    txt_file.write(election_results)



    #-------------------------------------------------------------------------------
    ### GETTING EACH CANDIDATE VOTE PERCENTAGE

    # 17) Get each candidates votes and percentage from the dictionary
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        # ALEXIS: print(f'{candidate} has {votes:,} votes; equal to {vote_percentage:3.3}%.')


    #-------------------------------------------------------------------------------
    ### DETERMINE WHO WON

        # 18) Declare winning count and winning candidate variables.
        
        # 19) Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 20) If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 21) Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        
        #  To do: print out the winning candidate, vote count and percentage to terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # 24) Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  25) Save the candidate results to our text file.
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    # 26) # Save the winning candidate's name to the text file.
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    #-------------------------------------------------------------------------------
    ### WRITE TO A TEXT FILE
    # 22) Open text file with "w" to write on it.

