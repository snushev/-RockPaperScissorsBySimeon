from random import randint

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
ORANGE = '\033[48m'
RESET = '\033[0m'

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input(f"{GREEN}Choose {BLUE}[r]{RESET}ock, {BLUE}[p]{RESET}aper, {BLUE}[s]{RESET}cissors: ")

if player_move == "r":
    player_choice = rock
elif player_move == "p":
    player_choice = paper
elif player_move == "s":
    player_choice = scissors

else:
    raise SystemExit("Invalid Input. Try again...")
print(f"You chose {YELLOW}{player_choice}{RESET}")

computer_choice = randint(1, 3)

if computer_choice == 1:
    computer_choice = rock
elif computer_choice == 2:
    computer_choice = paper
else:
    computer_choice = scissors
print(f'The computer chose {YELLOW}{computer_choice}{RESET}')

if (player_choice == rock and computer_choice == scissors) or \
        (player_choice == scissors and computer_choice == paper) or \
        (player_choice == paper and computer_choice == rock):
    print(f"{GREEN}You win!{RESET}")
elif player_choice == computer_choice:
    print(f"{GREEN}Draw!{RESET}")
else:
    print(f"{GREEN}You lose!")
