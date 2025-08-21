# Simple Python code to swap two numbers and add them

# input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# swap numbers
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")

# add the swapped numbers
sum_result = a + b
print(f"Sum of swapped numbers: {sum_result}")
