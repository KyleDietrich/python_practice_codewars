#!/usr/bin/env python3

def escape(carpark):
    """
    Given a 2D carpark array, returns a list of moves to reach the exit using only staircases.
    Moves are in the format: 'Lx' (left), 'Rx' (right), 'Dx' (down).
    """
    moves = []
    n_floors = len(carpark)
    n_spaces = len(carpark[0])

    # Find the starting position (where the 2 is)
    for floor_idx, floor in enumerate(carpark):
        if 2 in floor:
            curr_floor = floor_idx
            curr_pos = floor.index(2)
            break

    while curr_floor < n_floors - 1:
        # Find staircase on current floor
        stair_pos = carpark[curr_floor].index(1)
        # Move left or right to staircase if needed
        if curr_pos != stair_pos:
            direction = 'R' if stair_pos > curr_pos else 'L'
            steps = abs(stair_pos - curr_pos)
            if steps > 0:
                moves.append(f"{direction}{steps}")
            curr_pos = stair_pos

        # Count how many floors you can go down at this staircase
        down_steps = 0
        next_floor = curr_floor + 1
        while next_floor < n_floors and carpark[next_floor][curr_pos] == 1:
            down_steps += 1
            next_floor += 1
        # Always go down at least one floor
        down_steps += 1
        moves.append(f"D{down_steps}")
        curr_floor += down_steps

    # On ground floor, move right to exit if needed
    if curr_pos != n_spaces - 1:
        direction = 'R' if curr_pos < n_spaces - 1 else 'L'
        steps = abs((n_spaces - 1) - curr_pos)
        if steps > 0:
            moves.append(f"{direction}{steps}")

    return moves

# Example usage:
if __name__ == "__main__":
    # Test case 1
    carpark1 = [
        [1, 0, 0, 0, 2],
        [0, 0, 0, 0, 0]
    ]
    print(escape(carpark1))  # Output: ['L4', 'D1', 'R4']

    # Test case 2
    carpark2 = [
        [2, 0, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    print(escape(carpark2))  # Output: ['R3', 'D2', 'R1']


