# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: sepehr sabzevari
# Date: 10,9,2026
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.


def sum(a, b):
    return a + b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = sum(num1, num2)
    print(f"The sum is {total}")

if __name__ == "__main__":
    main()
