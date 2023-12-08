#!/usr/bin/python3
"""Lockboxes
Determines whether each box can be opened from n boxes.
Each is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Returns True if all the boxes can be opened, else returns False.
    args:
    boxes: A list of lists, where each inner list represents a box and the
    elements of the inner list represent the keys to the other boxes.
    returns:
    True if all the boxes can be opened, else False.
    """

    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True
    next_box = [0]

    # perform depth-first search
    while next_box:
        current_box = next_box.pop()
        for key in boxes[current_box]:
            if key >= 0 and key < len(boxes) and not opened_boxes[key]:
                next_box.append(key)
                opened_boxes[key] = True

    # check if all boxes have been visited
    return all(opened_boxes)
