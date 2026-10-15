# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: sepehr sabzevari
# Date: 10,9,2026
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(map(lambda x: x ** 2, numbers))
print(numbers)

divisible_by_2 = list(filter(lambda x: x % 2 == 0, numbers))
print(divisible_by_2)
