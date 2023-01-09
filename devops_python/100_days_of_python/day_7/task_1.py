#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list
#  and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign 
# their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of
#  the letters in the chosen_word.
import random

chosen_word = random.choice(word_list)
print(chosen_word)
display=[]
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess any letter: ").lower()
    for position in range(word_length):
       letter = chosen_word[position]
       if letter == guess:
          display[position] = letter 
    if "_" not in display:
       end_of_game = True      
print(display)
