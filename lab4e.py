# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py

# Follow the instructions from readme.md.

def compute(*, num1, num2, operation='+'):
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
    print(compute(num1=num1, num2=num2, operation=op))

    print(compute(num1=13, num2=45, operation='*'))
    print(compute(operation='/', num2=45, num1=13))  # out of order
    print(compute(num1=13, num2=45, operation='-'))
    print(compute(num1=13, num2=45))  # default '+'

if __name__ == "__main__":
    main()
