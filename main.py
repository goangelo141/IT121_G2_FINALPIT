import random

def play_game():
    
    words = ['python', 'programming', 'adventure', 'algorithm', 'developer', 'keyboard']

    #
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("--- Welcome to the Word Guessing Game! ---")
    print(f"The word has {len(secret_word)} letters.")

    while attempts > 0:

        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")