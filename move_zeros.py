#!/usr/bin/env python3

def move_zeros(lst):
    """
    This function moves all zeros in the list to the end while maintaining the order of non-zero elements.

    :param lst: list - The input list containing integers
    :return: list - The modified list with all zeros moved to the end
    """
    non_zeros = [x for x in lst if x != 0]
    zeros = [0] * (len(lst) - len(non_zeros))
    return non_zeros + zeros

#example usage:
if __name__ == "__main__":
    print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
    print(move_zeros([0, 0, 1]))          # Output: [1, 0, 0]
    print(move_zeros([1, 2, 3]))          # Output: [1, 2, 3]
    print(move_zeros([0]))                 # Output: [0]


