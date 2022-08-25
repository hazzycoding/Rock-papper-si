import random

user_wins = 0
computer_wins = 0 

options = ["rock", 'paper', 'scissors']

while True:
    user_input = input("type Rock/Papper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in['rock', 'papper', 'scissors']:
        continue

    random_number = random.randint(0, 2)\
    # rock: 0, paper: 1, scossors: 2
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + "." )


# if elif else 
    if user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1 
        continue

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1 
    
    elif user_input == "sicssors" and computer_pick == "papper":
        print("You won!")
        user_wins += 1 
        
    else: 
        print('You lost')
        computer_wins += 1 

print("You won", user_wins, 'times.')
print("the computer won ", computer_wins, 'times.')
print("Goodbye")
