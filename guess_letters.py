#!/usr/bin/env python3
import random

def main():
    print(" Welcome to Hangman! ")
    print("_ _ _ _ _ _ _ _ _ ")
    print("Guess youre letter: ")

    word = "EVAPORATE"
    guessed_letters = []
    correct_letters = set()

    word_letters = set(word)

    while correct_letters != word_letters:
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Current word: " + " ".join(display))

        guess = input("Enter a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_letters:
            print("Good guess!")
            correct_letters.add(guess)
        else:
            print("Sorry, that letter is not in the word.")

    print("Congratulations! You've guessed the word: " + word)
    

if __name__ == "__main__":
    main()