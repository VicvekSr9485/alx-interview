#!/usr/bin/python3
"""
Module 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1,
    and each box may contain keys to the other boxes.
    Determine if all the boxes can be opened.
    """
    if boxes is None:
        return False
    if len(boxes) == 1:
        return True
    # Track the visited boxes
    visited = set()
    # The first box is unlocked
    visited.add(0)

    # Using a stack to do a Depth First Search
    stack = []
    stack.append(0)

    while stack:
        keys = boxes[stack.pop()]
        for key in keys:
            if key not in visited:
                visited.add(key)
                stack.append(key)
    # Checking if all boxes have been visited
    return len(boxes) == len(visited)
