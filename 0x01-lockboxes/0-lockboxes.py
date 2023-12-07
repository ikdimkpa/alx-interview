#!/usr/bin/python3

def canUnlockAll(boxes):
    if type(boxes) is not list or len(boxes) == 0:
        return False

    boxLength = len(boxes)
    freeKeys = [0]
    usedKeys = set()

    while freeKeys:
        openedBoxIndex = freeKeys.pop()
        usedKeys.add(openedBoxIndex)
        openedBox = boxes[openedBoxIndex]

        if type(openedBox) is not list:
            return False

        for key in openedBox:
            if (key < boxLength) and (key not in freeKeys)
            and (key not in usedKeys):
                freeKeys.append(key)

    return len(usedKeys) == boxLength
