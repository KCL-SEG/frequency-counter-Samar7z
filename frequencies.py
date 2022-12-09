"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    str_Items = [str(item) for item in items]

    for i in str_Items:

        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies
