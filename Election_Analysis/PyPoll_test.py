### PSEUDO CODING
#The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recevived votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#-----------------------------------------------------------------------------
### DIRECT OPPENING
#Import csv module
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

#To do: perform analysis.

# Close the file.
election_data.close()

#Open 2nd option
#with open(file_to_load) as election_data:
 #   print(election_data)

#-----------------------------------------------------------------------------
### INDIRECT OPPENING
#1. importe csv and os modules
#import csv
#import os

#2. Add filename variable that references the path
file_to_load = os.path.join('Resources','election_results.csv' )

#3. Open the csv file using the with statement.
with open(file_to_load) as election_data:
    #4. Code:
    print(election_data)


#-----------------------------------------------------------------------------
### WRITING A FILE

#1. Create a variable to a direct/indirect path.
file_to_save = "Analysis/election_analysis.txt"

#2. Use the open() in the "w" mode.
#outfile = open(file_to_save,"w")
with open(file_to_save,"w") as txt_file:

#3. Write something 
    txt_file.write("Counties in the election")
    txt_file.write("\n------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

#outfile.close()


