
#string_utils.py
def reverse_string(text: str):
    return text[::-1]

def count_vowels(words: str):
    vowels = "aeouiAEOUI"
    cnt = 0
    for syb in words:
        if syb in vowels:
            cnt += 1
    return cnt
#math_operations.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero! "
    return a / b


#circle.py
import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    return 2 * math.pi *radius


#file_writer.py
def write_file(file_path, content):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return "File written successfully!"
    except Exception as e:
        return f"Error written file: {e}"



#file_reader.py
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found!"
    except Exception as e:
        return f"Error reading file: {e}"



#main.py
from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file
print("1. Math Operations")
print("2. Sring Operations")
print("3. Geometry Operations")
print("4. File Operations")


choice = input("Choose an option (1-4): ")
if choice == '1':
        
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(f"Add: {add(a, b)}")
    print(f"Subtract: {subtract(a, b)}")
    print(f"Multiply: {multiply(a, b)}")
    print(f"Divide: {divide(a, b)}")
elif choice == '2':

    text = input("Enter the text: ")
    print(f"Reverse text: {reverse_string(text)}")
    print(f"Vowels count: {count_vowels(text)}")
elif choice == '3':
    radius = int("Enter circle's radius: ")
    print(f"Circle's area: {calculate_area(radius)}.")
    print(f"Circumference: {calculate_circumference(radius)}")
elif choice == '4':
    file_path = "test.txt"
    content = "Hello, this folder written in file_operations package"
    print(write_file(file_path, content))

    print("File content: ")
    print(read_file(file_path))
else:
    print("Invalid choice.")
