# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals

# Results with rock
if user_choice == computer_choice:
    print(f'Computer chooses <{computer_choice}> \n'
    f'It´s a tie')
elif user_choice == 'r' and computer_choice == '´p':
    print(f'Computer chooses <{computer_choice}> \n'
    f'You lost!')
elif user_choice == 'r' and computer_choice == '´s':
    print(f'Computer chooses <{computer_choice}> \n'
    f'You won!')

# Results with paper
elif user_choice == 'p' and computer_choice == 's':
    print(f'Computer chooses <{computer_choice}> \n'
    f'You lost!')
elif user_choice == 'p' and computer_choice == 'r':
    print(f'Computer chooses <{computer_choice}> \n'
    f'You won!')

# Results with scissors
elif user_choice == 's' and computer_choice == 'r':
    print(f'Computer chooses <{computer_choice}> \n'
    f'You lost!')
elif user_choice == 's' and computer_choice == 'p':
    print(f'Computer chooses <{computer_choice}> \n'
    f'You won!')
else:
    print("This shouldn't happen.")