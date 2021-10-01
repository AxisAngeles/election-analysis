# Initial variable to track game play
user_play = "y"
acc_number = 0

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    Number = input("How many number?")
    
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range(int(Number)):
        
        # Print each number in the range
        print(acc_number+1)
        acc_number += 1

    # Once complete...
    print(f'Acc number: {acc_number}')
    user_play = input("Continue: (y)es or (n)o? ")