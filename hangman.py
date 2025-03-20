import random
# Word selection
word_list = ["python", "developer", "hangman", "challenge", "programming"]
word = random.choice(word_list).lower()
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6
# Display Interface
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])
# Game loop
while incorrect_guesses < max_attempts:
    print("\nWord:", display_word(word, guessed_letters))
    print(f"Incorrect guesses: {incorrect_guesses}/{max_attempts}")
    # User Input
    guess = input("Guess a letter: ").lower()
    # Check Guess
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!")
    else:
        print("Incorrect!")
        incorrect_guesses += 1
    # Win/Loss Conditions
    if set(word) <= set(guessed_letters):
        print("\nCongratulations! You guessed the word:", word)
        break
else:
    print("\nYou've been hanged! The word was:", word)
# Play Again
play_again = input("\nDo you want to play again? (yes/no): ").lower()
if play_again == "yes":
    exec(open(_file_).read())