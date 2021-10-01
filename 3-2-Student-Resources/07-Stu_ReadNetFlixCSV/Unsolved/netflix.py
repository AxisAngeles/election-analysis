# 1) Modules
import os
import csv

repeat = 'y'
while repeat == 'y':

    # 2) Prompt user for video lookup
    video = input("What show or movie are you looking for? ")

    # 3) Set counting and looking variables
    DBrow = 0
    Finder = True

    # 4) Set path for file
    file_path = os.path.join("..","Resources","netflix_ratings.csv")

    # 5) Open the CSV
    with open(file_path) as DB:
        # 5.1) Read the file and assign it to a variable
        NetflixDB = csv.reader(DB)
        # 5.2) Get Header row
        Header = next(NetflixDB)
        
        # 6) Loop through looking for the video
        for r in NetflixDB:
            DBrow += 1 #Counting register number
            if video in r:
                print(
                    f'\n'
                    f'Title Found \n'
                    f'\n----------------------------\n'
                    f'Title: {r[0]}\n'
                    f'Rated: {r[1]}\n'
                    f'User Rating: {r[5]}\n'
                    f'----------------------------\n'
                )
                Finder = True
                break #Breaks the loop
            else:
                Finder = False #If video not found variable is set to False
        
        # 7) Show results
        print(f'Loop ended at {DBrow} register.\n')
        if Finder == False:
            print(f'We´re sorry, we couln´t find your video.')
    
    repeat = input("Want to look for anything else? (y) or (n)")
        

