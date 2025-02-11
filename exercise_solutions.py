# We recommend to open after trying string_exercises.md file


# 1. Write a Python program that includes
# single-line comments
# Explain what the program does in the comments?

# this program calculates the sum oof two numbers

num1 = 12
num2 = 50
num3 = num1 + num2

# let's print the sum of two numbers
print(num3)

#2. Create a program that declares variables
# of different types (integer, float, string)
# and prints their values and types?

# let's this above question

age = 25   #Integer
height = 5.9 #float
name = "Habi"

# let's print
print(age, type(age))
print(height, type(height))
print(name, type(name))

# 3. Write a program that:
# Declares a few integer variables.
# Prints their values.
# Prints the sum of two of the integers.

# Declare integer variables
num1 = 10
num2 = 20
num3 = 30

#print the values of the integers
print("Number 1: ", num1)
print("Number 2: ", num2)
print("Number 3: ", num3)

#print the sum of num1 and num2
sum_result = num1 + num2
print("The sum of two numbers is:", sum_result)

# 4. Write a program that takes a string
# input from the user and prints the following:
# 	1. The length of the string
# 	2. The string in uppercase
# 	3. The string in lowercase
# 	4. The first character of the string

user_input = input("Enter String: ")

# print length of the string
print("Length: ", len(user_input))
# print as uppercase
print("Uppercase:", user_input.upper())
# print as lowercase
print("Lower case:", user_input.lower())
# print first char of the string
print('First char is:', user_input[0])