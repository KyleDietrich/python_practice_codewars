#!/usr/bin/env python3
import random

def pick_word():
    with open("sowpods.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def main():
    print("Welcome to Hangman!")

    word = pick_word()
    guessed_letters = set()
    correct_letters = set(word)
    attempts = 6  # Number of allowed incorrect guesses

    print("Guess the word: " + display_word(word, guessed_letters))

    while correct_letters != guessed_letters and attempts > 0:
        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            attempts -= 1
            print(f"Sorry, that letter is not in the word. You have {attempts} attempts left.")
        
        print("Current word: " + display_word(word, guessed_letters))

        if correct_letters == guessed_letters:
            print("Congratulations! You've guessed the word: " + word)
        elif attempts == 0:
            print("Game over! The word was: " + word)

    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    main()