# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you’ll get a ValueError.
# Write a program that prompts for two numbers.
# Add them together and print the result.
# Catch the TypeError if either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number.

#not a loop
num_1 = input("Number 1: ")
num_2 = input("Number 2: ")

try:
    xnum_1 = int(num_1)
    xnum_2 = int(num_2)
except ValueError:
    print("Need a number, not a string.")
else:
    answer = xnum_1 + xnum_2
    print(f"The sum of {num_1} + {num_2} = {answer}.")