#!/usr/bin/env python3
import random

def main():
    with open("sowpods.txt", "r") as file:
        words = file.read().splitlines()
    
    word = random.choice(words)
    print(word)    


if __name__ == "__main__":
    main()