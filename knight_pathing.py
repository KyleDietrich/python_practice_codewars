#!/usr/bin/env python3

def algebraic_to_coords(pos):
    """
    Converts chess algebraic notation (e.g., 'a1', 'h8') to 0-based (x, y) coordinates.
    'a1' -> (0, 0), 'h8' -> (7, 7)
    """
    file = ord(pos[0].lower()) - ord('a')
    rank = int(pos[1]) - 1
    return (file, rank)

def knightPathAlgebraic(start, end):
    """
    Calculates the minimum number of moves a knight needs to go from start to end using chess algebraic notation.

    :param start: str - Starting position in algebraic notation (e.g., 'a1')
    :param end: str - Target position in algebraic notation (e.g., 'h8')
    :return: int - Minimum number of moves required
    """
    from collections import deque

    p1 = algebraic_to_coords(start)
    p2 = algebraic_to_coords(end)

    if p1 == p2:
        return 0

    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    queue = deque([(p1[0], p1[1], 0)])  # (x, y, moves)
    visited = set()
    visited.add(p1)

    while queue:
        x, y, moves = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) == p2:
                return moves + 1
            if (nx, ny) not in visited and 0 <= nx < 8 and 0 <= ny < 8:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))

    return -1  # Should never reach here for valid chessboard positions

# Example usage:
if __name__ == "__main__":
    print(knightPathAlgebraic('a1', 'c1'))  # Output: 2
    print(knightPathAlgebraic('a1', 'd4'))  # Output: 2
    print(knightPathAlgebraic('h8', 'a1'))  # Output: 6
    print(knightPathAlgebraic('e5', 'e5'))  # Output: 0



