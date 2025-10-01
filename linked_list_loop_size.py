#!/usr/bin/env python3

def loop_size(node):
    """
    This function calculates the size of a loop in a linked list.

    :param node: Node - The starting node of the linked list
    :return: int - The size of the loop, or 0 if there is no loop
    """
    slow = node
    fast = node

    # Detect loop using Floyd's Tortoise and Hare algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Loop detected, now calculate the size of the loop
            loop_size = 1
            current = slow.next
            while current != slow:
                loop_size += 1
                current = current.next
            return loop_size

    return 0  # No loop detected


