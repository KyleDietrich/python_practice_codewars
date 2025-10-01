#!/usr/bin/env python3

def isSquare(n):
    """Check if a number is a perfect square."""
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n

