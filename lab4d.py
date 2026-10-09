# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: sepehr sabzevari
# Date: 10,9,2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.

def compute(num1, num2, operation='+'):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    return "Invalid operation"

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")
    print(compute(num1, num2, op))

    print(compute(13, 45, '*'))
    print(compute(13, 45, '/'))
    print(compute(13, 45, '-'))
    print(compute(13, 45, '+'))
    print(compute(13, 45))  # default '+'

if __name__ == "__main__":
    main()
