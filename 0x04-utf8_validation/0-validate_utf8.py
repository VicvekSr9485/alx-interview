#!/usr/bin/python3
""" utf-8 validation functions exercise """


def validUTF8(data):
    """ valid UTF-8 """
    #Initialize a counter to keep track of the number
    # of bytes in a multi-byte character
    bytes_in_char = 0

    for byte in data:
        # Get the value of the byte by taking the least significant 8 bits
        byte = byte & 0b11111111

        # Check if the byte is a continuation byte (starts with 10)
        if bytes_in_char > 0:
            if (byte >> 6) != 0b10:
                return False
            bytes_in_char -= 1
        # Check if the byte is a single-byte character (starts with 0)
        elif (byte >> 7) == 0:
            bytes_in_char = 0
        # Check if the byte is the start of a multi-byte character
        elif (byte >> 5) == 0b110:
            bytes_in_char = 1
        elif (byte >> 4) == 0b1110:
            bytes_in_char = 2
        elif (byte >> 3) == 0b11110:
            bytes_in_char = 3
        else:
            return False

    # If there are any remaining bytes in a character, the encoding is invalid
    if bytes_in_char > 0:
        return False
    return True
