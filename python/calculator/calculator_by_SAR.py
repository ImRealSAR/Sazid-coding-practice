# # This is a calculator made by me (Sazid/SAR) to practice my coding and programming skills.
# # Import necessary modules/libraries from Python
import math
import random
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction

# Functions for each mathematical operation
def is_number(value):
    try:
        float(Fraction(value))  # Check if it's valid input for the calculator to work properly
        return True
    except ValueError:
        return False

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def modulo(x, y):
    return x % y

def exponent(x, y):
    return x ** y

# Function to handle button click
def calculate(operation):
    num1 = entry1.get()
    num2 = entry2.get()
    if not is_number(num1) or not is_number(num2):
        messagebox.showerror("Invalid input", "Please enter valid numbers")
        return
    num1 = float(Fraction(num1))
    num2 = float(Fraction(num2))
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "modulo":
            result = modulo(num1, num2)
        elif operation == "exponent":
            result = exponent(num1, num2)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Calculator--By SAR")

# Create input fields
tk.Label(root, text="Enter the first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Create buttons for operations
tk.Button(root, text="Add", command=lambda: calculate("add")).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).grid(row=3, column=0)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).grid(row=3, column=1)
tk.Button(root, text="Modulo", command=lambda: calculate("modulo")).grid(row=4, column=0)
tk.Button(root, text="Exponent", command=lambda: calculate("exponent")).grid(row=4, column=1)

# Create label to display result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()
# # This is a calculator made by me (Sazid/SAR) to practice my coding and programming skills.



# # Functions for each mathematical operation
# def is_number(value):
#     try:
#         float(Fraction(value))  # Validate as integer, float, or fraction
#         return True
#     except ValueError:
#         return False

# def add(x, y):
#     return int(x + y)

# def subtract(x, y):
#     return int(x - y)

# def multiply(x, y):
#     return int(x * y)

# def divide(x, y):
#     return int(x / y)

# def modulo(x , y):  # Find remainder of the division problem only
#     return int(x % y)

# def exponent(x, y):
#     return int(x ** y)

# print("Welcome to Calculator--By SAR!")

# # Get first number from the user
# num_1 = input("Enter the first number: ")
# while not is_number(num_1):
#     print("Invalid input! Try again!")
#     num_1 = input("Enter the first number: ")  # Keep asking until valid
# num_1 = float(Fraction(num_1))  # Convert to number once valid

# # Get second number from the user
# num_2 = input("Enter the second number: ")
# while not is_number(num_2):
#     print("Invalid input! Try again!")
#     num_2 = input("Enter the second number: ")  # Keep asking until valid
# num_2 = float(Fraction(num_2))  # Convert to number once valid

# # Menu to decide how to move forward
# menu = '''1) Add 
# 2) Subtract
# 3) Multiply
# 4) Divide
# 5) Find remainder 
# 6) Convert to Binary (stay tuned!)
# 7) Convert from Binary (stay tuned!)
# 8) Exponent (First number is base, second number is power to raise to!)
# 9) Logarithm(stay tuned!)
# 10) Compute expression(stay tuned!)
# 11) Exit
# 12) More coming soon maybe... stay tuned!'''

# # Print menu
# print(menu)

# # Get user's menu choice
# Menu_pick = int(input('''Enter JUST the number from the menu to proceed! Example: To add, just type "1"!: '''))

# # Process menu choice
# if Menu_pick == 1:
#     result = add(num_1, num_2)
#     print(f"Result: {result}")
# elif Menu_pick == 2:
#     result = subtract(num_1, num_2)
#     print(f"Result: {result}")
# elif Menu_pick == 3:
#     result = multiply(num_1, num_2)
#     print(f"Result: {result}")
# elif Menu_pick == 4:
#     result = divide(num_1, num_2) 
#     print(f"Result: {result}")
# elif Menu_pick == 5:
#     result = modulo(num_1, num_2)
#     print(f"Result: {result}")
# elif Menu_pick == 7:
#     result = exponent(num_1, num_2)
#     print(f"Result: {result}")
# elif Menu_pick == 10:
#     print("Exiting program. Thank you for using the calculator!")
#     exit()  # Ends the program
# else:
#     print("Option not yet implemented. Stay tuned!")
