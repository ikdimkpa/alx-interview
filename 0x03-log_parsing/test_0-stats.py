#!/usr/bin/python3
"""Log Parsing"""
import sys


possible_status_codes = [100, 301, 400, 401, 403, 404, 405,500]
total_file_size = 0
number_of_lines = 0
map_status_codes = {}

def print_stats():
    """Prints the current status"""
    print("{}: {}".format(file_size, total_file_size))

    for status, count in sorted(map_status_codes.items()):
        print("{}: {}".format(status, count))

try:
    for line in sys.stdin:
        try:
            line = line.split()
            file_size = line[-1]
            total_file_size += int(file_size)
            status_code = line[-1]

            if status_code in possible_status_codes:
                if status_code in map_status_codes:
                    map_status_codes[status_code] += 1
                else:
                    map_status_code[status_code] = 1

            number_of_lines += 1

            if number_of_lines % 10 == 0:
                print("File size: {}".format(total_file_size))

        except ValueError:
            pass

        if (number_of_lines == 0) or (number_of_lines % 10 != 0):
            print_stats()

except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
