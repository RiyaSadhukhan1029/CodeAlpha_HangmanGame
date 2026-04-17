import random

# Predefined word list (5 words)
words = ["apple", "tiger", "chair", "table", "plant"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""

    # Display current progress
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validation (optional but good)
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("✅ Correct guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)

# Lose condition
if attempts == 0:
    print("💀 Game Over! The word was:", word)