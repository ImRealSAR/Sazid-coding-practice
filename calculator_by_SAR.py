# This is a calculator made by me (Sazid/SAR) to practice my coding and programming skills.

# Import necessary modules/libraries from Python
import math
import random
import tkinter 
from fractions import Fraction

# Functions for each mathematical operation
def is_number(value):
    try:
        float(Fraction(value))  # Validate as integer, float, or fraction
        return True
    except ValueError:
        return False

def add(x, y):
    return int(x + y)

def subtract(x, y):
    return int(x - y)

def multiply(x, y):
    return int(x * y)

def divide(x, y):
    return int(x / y)

def modulo(x , y):  # Find remainder of the division problem only
    return int(x % y)

def exponent(x, y):
    return int(x ** y)

print("Welcome to Calculator--By SAR!")

# Get first number from the user
num_1 = input("Enter the first number: ")
while not is_number(num_1):
    print("Invalid input! Try again!")
    num_1 = input("Enter the first number: ")  # Keep asking until valid
num_1 = float(Fraction(num_1))  # Convert to number once valid

# Get second number from the user
num_2 = input("Enter the second number: ")
while not is_number(num_2):
    print("Invalid input! Try again!")
    num_2 = input("Enter the second number: ")  # Keep asking until valid
num_2 = float(Fraction(num_2))  # Convert to number once valid

# Menu to decide how to move forward
menu = '''1) Add 
2) Subtract
3) Multiply
4) Divide
5) Find remainder 
6) Convert to Binary (stay tuned!)
7) Convert from Binary (stay tuned!)
8) Exponent (First number is base, second number is power to raise to!)
9) Logarithm(stay tuned!)
10) Compute expression(stay tuned!)
11) Exit
12) More coming soon maybe... stay tuned!'''

# Print menu
print(menu)

# Get user's menu choice
Menu_pick = int(input('''Enter JUST the number from the menu to proceed! Example: To add, just type "1"!: '''))

# Process menu choice
if Menu_pick == 1:
    result = add(num_1, num_2)
    print(f"Result: {result}")
elif Menu_pick == 2:
    result = subtract(num_1, num_2)
    print(f"Result: {result}")
elif Menu_pick == 3:
    result = multiply(num_1, num_2)
    print(f"Result: {result}")
elif Menu_pick == 4:
    result = divide(num_1, num_2) 
    print(f"Result: {result}")
elif Menu_pick == 5:
    result = modulo(num_1, num_2)
    print(f"Result: {result}")
elif Menu_pick == 7:
    result = exponent(num_1, num_2)
    print(f"Result: {result}")
elif Menu_pick == 10:
    print("Exiting program. Thank you for using the calculator!")
    exit()  # Ends the program
else:
    print("Option not yet implemented. Stay tuned!")
