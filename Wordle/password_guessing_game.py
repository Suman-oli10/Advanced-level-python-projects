
import random

print("----Welcome to the password guessing game----")
print("1. Guess a word.\n2. Guess it in as few attempts as possible.")

Easy = ['Sat', 'Run', 'Net', 'Bot', 'Lit']
Medium = ['Copy', 'Shoes', 'Load', 'Goat', 'Farm']
Hard = ['Education', 'Random', 'Bedroom', 'Window', 'Carpenter']

user_input = input("Enter the level: ").lower()  

if user_input == "easy":
    guessing_word = random.choice(Easy)           
elif user_input == "medium":
    guessing_word = random.choice(Medium)         
elif user_input == "hard":
    guessing_word = random.choice(Hard)           
else:
    print("Invalid choice")
    guessing_word = None                          

attempt = 0                                       

if guessing_word is not None:                     
    while True:
        user_guess = input("Guess the word: ")    
        attempt += 1                              

        if user_guess.lower() == guessing_word.lower():
            print("Correct word!")                
            print("Total attempts:", attempt)     
            break                                 

        hint = ""                                 # Stores the hint

        for i in range(len(guessing_word)):       # Checks each character
            if i < len(user_guess) and user_guess[i].lower() == guessing_word[i].lower():
                hint += user_guess[i]             # Keeps correct character
            else:
                hint += "_"                        # Hides incorrect character

        print("Hint:", hint)                      # Displays the hint
