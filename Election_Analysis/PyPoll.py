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

# 4) Open the election results and read the file.
with open(file_to_load) as election_data:

    # 5) Read the file object with the reader function.
    # 6) Print each row in te csv file.
    file_reader = csv.reader(election_data)
    #for row in file_reader:
     #       print(row)

    # 6.5) Print header row.
    headers = next(file_reader)
    print(headers)

    #
    
    


# To do: read and analyze the data here.