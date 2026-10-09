# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: sepehr sabzevari
# Date: 10,9,2026
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.


def get_initials(*args):
    initials = []
    for name in args:
        initials.append(name[0])
    return initials

def main():
    result = get_initials("Alice", "Bob", "Charlie", "David")
    print(result)

if __name__ == "__main__":
    main()
