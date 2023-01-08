#!/usr/bin/python3
"""determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Return: True or False
    """
    unlocked_boxes = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in \
                    unlocked_boxes and key != box_id:
                unlocked_boxes.append(key)
    if len(unlocked_boxes) == len(boxes):
        return True
    return False
