#!/usr/bin/env python3

def validate_battlefield(field):
    """
    Validates that a 10x10 battleship field has a valid disposition of ships.
    Rules:
    - 1 battleship (size 4)
    - 2 cruisers (size 3)
    - 3 destroyers (size 2)
    - 4 submarines (size 1)
    - Ships must be straight lines (no bends)
    - Ships cannot touch each other, not even diagonally
    """
    from collections import Counter, deque

    # Directions for 8 neighbors (including diagonals)
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),          (0, 1),
                 (1, -1),  (1, 0), (1, 1)]

    # To keep track of visited cells
    visited = [[False]*10 for _ in range(10)]
    ship_sizes = []

    def bfs(r, c):
        """Breadth-first search to find the full ship starting from (r, c)."""
        queue = deque()
        queue.append((r, c))
        visited[r][c] = True
        ship_cells = [(r, c)]

        # Determine orientation: horizontal or vertical
        orientation = None
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 10 and 0 <= nc < 10 and field[nr][nc] == 1:
                orientation = (dr, dc)
                break

        # If no orientation, it's a submarine (single cell)
        if not orientation:
            orientation = (0, 0)

        # Explore the ship in the determined direction
        dr, dc = orientation
        nr, nc = r + dr, c + dc
        while 0 <= nr < 10 and 0 <= nc < 10 and field[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            ship_cells.append((nr, nc))
            nr += dr
            nc += dc

        # Check for invalid bends (should not have both horizontal and vertical neighbors)
        for cell in ship_cells:
            cr, cc = cell
            # If both right and down neighbors are 1, it's a bend (invalid)
            if (cr + 1 < 10 and field[cr + 1][cc] == 1 and
                cc + 1 < 10 and field[cr][cc + 1] == 1):
                return None  # Invalid ship

        return ship_cells

    # Main loop: find all ships
    for r in range(10):
        for c in range(10):
            if field[r][c] == 1 and not visited[r][c]:
                ship = bfs(r, c)
                if not ship:
                    return False  # Invalid ship (bent)
                # Check for touching ships (including diagonals)
                for sr, sc in ship:
                    for dr, dc in neighbors:
                        nr, nc = sr + dr, sc + dc
                        if 0 <= nr < 10 and 0 <= nc < 10:
                            if field[nr][nc] == 1 and not visited[nr][nc]:
                                # If neighbor is a ship part and not visited, it's touching
                                return False
                ship_sizes.append(len(ship))

    # Count ships by size
    count = Counter(ship_sizes)
    # Required fleet composition
    required = {4: 1, 3: 2, 2: 3, 1: 4}
    return all(count.get(size, 0) == required[size] for size in required)

# Example usage and explanation:
if __name__ == "__main__":
    # A valid battlefield example (from the prompt)
    battleField = [
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(validate_battlefield(battleField))  # Should print True
