# Demonstration of Variables, Data Types & Type Conversion

# Declaring variables
age = 24                # int
height = 5.1            # float
name = "Bhargavi"       # string
is_student = True       # boolean

# Printing data types
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Arithmetic operations
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Type casting from input
try:
    num = int(input("200 "))
    print("Number entered:", num)
except ValueError:
    print("Invalid input!")

# String and number concatenation
print("Age is " + str(age))
print(f"Height is {height}")

# Dynamic typing
x = 100
print(x, type(x))
x = "Hello"
print(x, type(x))
x = 2.5
print(x, type(x))
