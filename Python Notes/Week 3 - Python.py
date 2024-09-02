# Week 15 / Python 3

# Main Focus of Python Workshop
# Automation
# API Projects
# 

'''
We will do the following today.
- Assignment discussion
- Additional topics to discuss:
- Lambda
- Recurssion
- List
- Web scraping using python
'''

# Sample Assignment Answers
# ASSIGNMENT #1
def meters_to_cm(meters):
    return meters * 100

def inches_to_mm(inches):
    return inches * 25.4

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

print("Choose the conversion option:")
print("1. Convert meters to centimeters")
print("2. Convert inches to millimeters")
print("3. Convert feet to meters")
print("4. Convert meters to kilometers")
print("5. Convert kilometers to miles")

option = int(input("Enter your choice: "))
def meters_to_cm(meters):
    return meters * 100

def inches_to_mm(inches):   
    if option == 1:
        meters = float(input("Enter the length in meters: "))
        result = meters_to_cm(meters)
        print(f"{meters} meters is equal to {result} centimeters.")
    elif option == 2:
        inches = float(input("Enter the length in inches: "))
        result = inches_to_mm(inches)
        print(f"{inches} inches is equal to {result} millimeters.")
    elif option == 3:
        feet = float(input("Enter the length in feet: "))
        result = feet_to_meters(feet)
        print(f"{feet} feet is equal to {result} meters.")
    elif option == 4:
        meters = float(input("Enter the length in meters: "))
        result = meters_to_kilometers(meters)
        print(f"{meters} meters is equal to {result} kilometers.")
    elif option == 5:
        kilometers = float(input("Enter the length in kilometers: "))
        result = kilometers_to_miles(kilometers)
        print(f"{kilometers} kilometers is equal to {result} miles.")
    else:
        print("Invalid option. Please choose a number between 1 and 5.")

# Adding a while loop
# Input must be an integer -- if not program will 


# Try catch error 
# If not digit 

# What if Exercise
# Main Page 


# REMEMBER: ALWAYS ASK FOR BUSINESS SPECIFICATIONS UNTIL THEY ARE FULLY UNDERSTOOD

# ASSIGNMENT #2
def meters_to_cm(meters):
    return meters * 100

def inches_to_mm(inches):
    return inches * 25.4

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371


def main():
    while True:
        print("1. Convert meters to cm")
        print("2. Convert inches to mm")
        print("3. Convert feet to meters")
        print("4. Convert meters to kilometers")
        print("5. Convert kilometers to miles")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            meters = float(input("Enter the number of meters: "))
            result = meters_to_cm(meters)
            print(f"{meters} meters is equal to {result} cm")
        elif choice == "2":
            inches = float(input("Enter the number of inches: "))
            result = inches_to_mm(inches)
            print(f"{inches} inches is equal to {result} mm")
        elif choice == "3":
            feet = float(input("Enter the number of feet: "))
            result = feet_to_meters(feet)
            print(f"{feet} feet is equal to {result} meters")
        elif choice == "4":
            meters = float(input("Enter the number of meters: "))
            result = meters_to_kilometers(meters)
            print(f"{meters} meters is equal to {result} kilometers")
        elif choice == "5":
            kilometers = float(input("Enter the number of kilometers: "))
            result = kilometers_to_miles(kilometers)
            print(f"{kilometers} kilometers is equal to {result} miles")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__": # THIS IS THE LINE 
# EQUATES TO WHILE TRUE
# REASON FOR PROGRAM CONTINUITY
    main()
    
if True: # Alternative
    main()

# Lambda
# - shortcut of a function
# - can have many arguments but with only one expression

# lambda function that squares its input
square = lambda x: x*x
print(square(5))

def square(x):
    return x*x

print(square(5))

# lambda function that adds two numbers 
add = lambda x,y: x+y
print(add(3,5))
# a function can have multiple expressions
# a lambda can have only one expression

def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x*x, 4)
print(result)

# Recursion
# - a function that calls to itselfs
# - breakingdown a problem into sub problems
# - each recursion call processes a smaller place of the original problem
#   until the case is reached / result is obtained

# note: case obtainable. infinite loop

# factorial 
# 3! = 1*2*3
# 7! = 1*2*3*4*5*6*7
# 0! = 1
# permutaitons and combinations
# CHANCES OF WINNING A LOTTERY - ASSIGNMENT LATER 

# Sample Recursion
def factorial(n):
    # base case: if n = 0, return 1
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(5)

def factorial_loop(a):
    #intialize result to 1(0! = 1 and 1!= 1)
    result = 1
    #loop through 1 to a
    for i in range(1,a+1): # sequence 1 to 6
    #starting point 1
    #a+1 is end point or max
        print(f"Iteration {i}:")
        print(f"Value of result before={result}")
        print(f"value of i = {i}")
        prev_result = result
        result = result * i
        print(f"Result = {prev_result}*{i}={result}")
        print("----------------------")
    return result
print(factorial_loop(5)) #24


'''
limit = 5

1st iteration:
i = 1
result = 1
result = result * i = 1*1

2nd iteration:
i = 2
result = 1
result = result * i = 1*2 = 2

3rd iteration:
i = 3
result = 2
result = result * i = 2 * 3 = 6

4th iteration:
i = 4
result = 6
result = result * i = 4 * 6 = 24


'''

# For Loop
# print number starting from 1 to 100
for i in range (5):
    print(i)

#doing the for loop on while loop
i = 0
while i < 5:
    print(i)
    i += 1

# List & Dictionaries

# Variable - is a container
# List - is a value that contains multiple values in an ordered seq.
# e.g. ['cat', 'bat', 'dog', 'man']

# Value inside of a list is called items
# e.g. [1, 2, 3]

sample_list = [1, 2, 3, 4, 5]
for item in sample_list:
    print(item)

print(sample_list[0])
print(f'Hello {sample_list[1]}')

# A list can contain another list
sample_list = [['batman', 'superman', 'flash'], ['iron man', 'cap america', 'thor']]
print(sample_list[1][0])

# Exercise
print(sample_list[0][0]) # print batman
print(sample_list[0][2]) # print flash
print(sample_list[1][1]) # print cap america

# Negative indexes
print(sample_list[0][-1])
print(sample_list[-1][-1])

# getting a list from another list with slices 
sample_list_1 = [['batman', 'superman', 'flash', 'cpt. barbell', 'darna']]
print(sample_list_1[0:1])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:-1])
print(spam[:2])
print(spam[:])

# to know length of list
print(len(spam))

# Changing values in a list with indexes
x = 'Marvin'
print(x)

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'Marvin'
print(spam)

#List Concatenation and list replication
list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
list_3 = list_1 + list_2
print(list_3[:])
print(list_2 * 3)

# removing values from lists with del statement 
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)

# both these methods are hard to maintain in long run
student_1 = 'James'
student_2 = 'Mark'
student_3 = 'Marv'

print('Enter student name: ')
student_1 = input()
print('Enter student name: ')
student_2 = input()
print('Enter student name: ')
student_3 = input()
print(student_1, student_2, student_3)

# using lists for this
student = [] # blank list
while True:
    print('Enter name of the student ' + str(len(student)) + 
          ' (or enter nothing to stop):')
    name = input()
    if name == '':
        break
    student = student + [name]
    print('The student names are: ')
    for nam in student:
        print(' ' + nam)

# Activity 
# Create list of numbers (10, 20, 30, 40, 50)
# Print all the item in the list
# Calculate the sum of all the numbers in the list
# Find the maximum number of the list
# Find the minimum number of the list

tens = lambda x: x*10

j = 1
list = []
while j <= 5:
    list = list + [tens(j)]
    print(tens(j))
    if j == 5:
        print(' ')
        print(f"The final list: {list}")
        minimum_value = list[0]
        maximum_value = list[0]
        total = 0
        for num in list:
            if num < minimum_value:
                minimum_value = num
            if num > maximum_value:
                maximum_value = num
            total = total + num
            
        print(f'Sum of all values in the list: {total}')
        print(f'Maximum number from the list: {maximum_value}')
        print(f'Maximum number from the list: {minimum_value}')
    j += 1

# in and not in operator
# - determine whether a value is or isn't in a list
myPets = ['sam', 'whitney', 'blackey']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I dont have a pet named ' + name)
else:
    print(name + ' is my pet name')

cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
behavior = cat[2]

size, color, behavior = cat
# number of variables and length of the list must be exact
# otherwise it will result to an error

# using the enumerate() function with the list
sample_list = [1, 2, 3, 4, 5]
print(range(len(sample_list)))

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index: ' + str(index) + ' supplies is: ' + item)

# Methofs , adding values to the list using append and insert methods
# Add values - apprend() and insert() method
supplies.append('submarine')
supplies.insert(1, 'missiles')
for index, item in enumerate(supplies):
    print('Index: ' + str(index) + ' supplies is: ' + item)

# if you know the value, we can use .remove method
print('Using remove method...')
supplies.remove('missiles')
for index, item in enumerate(supplies):
    print('Index: ' + str(index) + ' supplies is: ' + item)

# Web scraping
# - extracting info from online by retrieving relevant data 
