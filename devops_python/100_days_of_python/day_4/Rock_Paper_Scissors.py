rock = "Rock"
paper = "Paper"
scissors = "Scissors"
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

gamer = int(input())
import random
computer = random.randint(0,2)
all_symbols = [rock,paper,scissors]
gamers_choice = all_symbols[gamer]
computers_choice = all_symbols[computer]
print(gamers_choice)
print(f"Computer chose: {computer}")
print(computers_choice)
if computer == 1 and gamer == 0 or computer == 0 and gamer == 2 or computer == 2 and gamer ==1:
    print("You lose")
elif computer == gamer:
    print("It's a draw")
else:
    print("You win")