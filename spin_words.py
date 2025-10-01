#!/usr/bin/env python3

def spin_words(sentence):
    """
    This function takes a sentence as input and returns the sentence with words of five or more letters reversed.
    
    :param sentence: str - The input sentence
    :return: str - The modified sentence with long words reversed
    """
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())

