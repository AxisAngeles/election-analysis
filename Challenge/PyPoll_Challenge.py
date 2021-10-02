# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..","Election_Analysis", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1) Create a county list and county votes dictionary.
county = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2) Track the largest county and county voter turnout.
turnout_county_name = ""
turnout_county_votes = 0

# 3) Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader) # Read the header

    for row in reader: # For each row in the CSV file.

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a) Check if county is in the list, if not append it.
        if row[1] not in county:
            
            # 4b) Add the existing county to the list of counties.
            county.append(row[1])

            # 4c) Begin tracking the county's vote count.
            county_votes[row[1]] = 0

        # 5) Add a vote to that county's vote count.
        county_votes[row[1]] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a) Write a for loop to get the county from the county dictionary.
    for c in county_votes:
        
        # 6b) Retrieve the county vote count.
        votes_by_county = county_votes[c]

        # 6c) Calculate the percentage of votes for the county.
        county_percentage = votes_by_county/total_votes*100

        # 6d) Print the county results to the terminal.
        print(f'{c}: {county_percentage:.1f}% ({votes_by_county:,})')
        county_results = (f'{c}: {county_percentage:.1f}% ({votes_by_county:,})\n')

        # 6e) Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f) Write an if statement to determine the winning county and get its vote count.
        if votes_by_county > turnout_county_votes:
            turnout_county_votes = votes_by_county
            turnout_county_name = c
    
    # 7) Print the county with the largest turnout to the terminal.
    turnout_summary = (
        f'\n'
        f'{"-"*25}\n'
        f'Largest County Turnout: {turnout_county_name}\n'
        f'{"-"*25}\n')
    print(turnout_summary)
    print(f'Candidate Votes:')


    # 8) Save the county with the largest turnout to a text file.
    txt_file.write(turnout_summary)
    candidate_header = (f'\n'
    f'Candidate Votes:\n')
    txt_file.write(candidate_header)


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (f'\n'
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
