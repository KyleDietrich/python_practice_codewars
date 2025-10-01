#!/usr/bin/env python3

def rgb(r, g, b):
    """
    This function takes three integers representing RGB values and returns a hexadecimal color code.

    :param r: int - Red component (0-255)
    :param g: int - Green component (0-255)
    :param b: int - Blue component (0-255)
    :return: str - Hexadecimal color code in the format '#RRGGBB'
    """
    def clamp(x):
        """Clamp the value to be within the range 0-255."""
        return max(0, min(255, x))
    
    return f'#{clamp(r):02X}{clamp(g):02X}{clamp(b):02X}'

# Example usage:
if __name__ == "__main__":
    print(rgb(255, 0, 0))  # Output: '#FF0000'
    print(rgb(0, 255, 0))  # Output: '#00FF00'
    print(rgb(0, 0, 255))  # Output: '#0000FF'
    print(rgb(255, 255, 255))  # Output: '#FFFFFF'
    print(rgb(0, 0, 0))  # Output: '#000000'



