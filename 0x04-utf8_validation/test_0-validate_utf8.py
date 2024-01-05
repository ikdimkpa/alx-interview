#!/usr/bin/python3
"""Defines a method that checks if an integer is UTF-8 valid"""


def validUTF8(data):
    """Checks for UTF-8 validity in dataset"""

    for byte in data:
        bin_char = format(byte, '08b')

        if bin_char.startswith('0'):
            continue
        elif bin_char.startswith('110'):
            continue
        elif bin_char.startswith('1110'):
            continue
        elif bin_char.startswith('11110'):
            continue
        else:
            return False
    return True
