#!/usr/bin/env python3

def alphabet_position(text):

    text = text.lower()
    positions = []
    for char in text:
        if char.isalpha():
            position = ord(char) - ord('a') + 1
            positions.append(str(position))
    return ' '.join(positions)

