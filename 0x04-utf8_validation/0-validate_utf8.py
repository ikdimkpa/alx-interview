#!/usr/bin/python3
"""Defines a method that checks if an integer is UTF-8 valid"""


def validUTF8(data):
    """Checks for UTF-8 validity in dataset"""
    
    num_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            return False

        n_bytes -= 1

    return n_bytes == 0
