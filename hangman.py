import random

# Expanded word bank with more words for variety
word_bank = [
    'breakfast', 'entrepreneur', 'beautiful', 'throughout', 'impeccable',
    'porcupine', 'gorgeous', 'aubergine', 'pineapple', 'umbrella',
    'tremendous', 'hedgehog', 'algorithm', 'debugging', 'innovation',
    'prototype', 'hacker', 'circuit', 'quantum', 'galaxy'
]

# ASCII art for Hangman stages (improves visual design)
HANGMAN_PICS = [
    '''
      +---+
          |
          |
          |
         ===
    ''',
    '''
      +---+
      O   |
          |
          |
         ===
    ''',
    '''
      +---+
      O   |
      |   |
          |
         ===
    ''',
    '''
      +---+
      O   |
     /|   |
          |
         ===
    ''',
    '''
      +---+
      O   |
     /|\\  |
          |
         ===
    ''',
    '''
      +---+
      O   |
     /|\\  |
     /    |
         ===
    ''',
    '''
      +---+
      O   |
     /|\\  |
     / \\  |
         ===
    '''
]

def play_hangman():
    word = random.choice(word_bank).lower()  # Ensure lowercase for consistency
    guessed_word = ['_'] * len(word)
    guessed_letters = set()  # Track guessed letters to prevent duplicates
    attempts = 6  # Fixed the typo from '6a'
    
    print("Welcome to Enhanced Hangman!")
    print("Theme: Fun and Tech Words")
    print(f"You have {attempts} attempts to guess the word.")
    
    while attempts > 0:
        # Display Hangman art based on remaining attempts (reversed index)
        print(HANGMAN_PICS[6 - attempts])
        
        print('\nCurrent word: ' + ' '.join(guessed_word))
        print('Guessed letters: ' + ', '.join(sorted(guessed_letters)) if guessed_letters else 'None yet')
        
        guess = input('Guess a letter (or type "quit" to exit): ').lower().strip()
        
        if guess == 'quit':
            print(f'\nGame quit! The word was: {word}')
            return False  # Return False to not play again immediately
        
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid input! Please guess a single letter.')
            continue
        
        if guess in guessed_letters:
            print('You already guessed that letter! Try another.')
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print('Great guess!')
        else:
            attempts -= 1
            print(f'Wrong guess! Attempts left: {attempts}')
        
        if '_' not in guessed_word:
            print(HANGMAN_PICS[6 - attempts])  # Show final art
            print('\nCurrent word: ' + ' '.join(guessed_word))
            print(f'Congratulations! You guessed the word: {word}')
            return True  # Return True to ask if play again
    
    # Game over
    print(HANGMAN_PICS[6])  # Full hangman
    print(f'\nYou\'ve run out of attempts! The word was: {word}')
    return False

# Main game loop for playing multiple times
if __name__ == "__main__":
    while True:
        play_again = play_hangman()
        if not play_again:
            retry = input('Play again? (y/n): ').lower().strip()
            if retry != 'y':
                print('Thanks for playing!')
                break