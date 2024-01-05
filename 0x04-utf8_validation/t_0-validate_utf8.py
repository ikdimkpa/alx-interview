#!/usr/bin/python3
"""Defines a method that checks if an integer is UTF-8 valid"""


def validUTF8(data):
    """Checks for UTF-8 validity in dataset"""

    mask1 = 1 << 7
    mask2 = 1 << 6
    
    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

                if num_bytes == 0:
                    continue

                
                if num_bytes == 1 or num_bytes > 4:
                    return False
        else:
            if not (num & mask_1 and not (num & mask_2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
