## Week 13 / 1 Python

## What is Python
## one of the most popular programming language
## General Purpose Programming language

print("Print something")

## Interpreted vs Compiled Language

## Interpreter Language (Python, etc.)
## code is interpreted line by line 

## Compiled Language
## code is not line by line, interpreted the code whole

'''
Week 1:
Python Basics
Flow control
Functions
Lists

Week 2:
Dictionaries and structuring data
Manipulation of strings
Pattern matching and regular expressions

Week 3:
Webscraping
Web scraping project

Week 4:
Introduction to Pandas
Manipulate csv file and excel file using python
API introduction
Using API

Week 5:
Continuation API
Automated Email Sender-- with attachment
Downloading file on gmail
Push notifications on smart phone using python script
Sample project using API

Week 6:
TBD


'''

## Math Operations
## + ADDITION
## - SUBTRACTION
## / DIVISION
## * MULTIPLICATION
## % MODULO/ REMAINDER
## ** EXPONENT

## VARIABLE = CONTAINER
marvin = 25
print(marvin + 10) # 35

# initializing a variable
spam = 40
egg = 110
rice = 15

print(spam + egg + rice)

spam = 'I love spam'
print(spam)

decimal_var = -3.43525
is_true = True
print(is_true)

# NOTE: 
# a good variable name always describes the data it contains
# variable name must have no space in between
# it can only use letters, numbers and underscore
# it can not begin with a number
# variables are case sensitive - spam != SPAM 
print(spam); print(SPAM)


## DATA TYPES 
# INTEGER, FLOATING POINT, STRINGS, BOOLEAN
# EVERY VALUE/VARIABLES HAS ONLY ONE DATA TYPE

## SYNTAX
## how you write things in programming; it is like grammar
# PEMDAS

print('Alice' + ' ' + 'Bob')
print('Alice' + 42)
print('Alice' * 5)

##### FIRST ACTIVITY
# CREATE AT LEAST 5 VARIABLES
# CREATE A PROGRAM WITH 5 MENUS WITH DIFFERENT PRICES
# PRINT ALL THE MENU WITH PRICE
# CREATE A VARIABLE NAMED DISCOUNT = .20
# GET FINAL PRICE OF 3 FOODS FROM THE MENU

sisig = 99
bulalo = 105
sinigang = 90
lechon = 200
bbq = 50
discount = .2

print((sisig + lechon + sinigang) - 
      ((sisig + lechon + sinigang) * discount))
# 311.2

total = sisig + lechon + sinigang
total_with_discount = total - (total * discount)
print("The total price: " + str(total_with_discount))

# USER INPUT
cornbeef = 57
cornbeef = sisig
print(cornbeef)

# A PROGRAM THAT WILL ASK FOR YOUR NAME
print('Hello! What is your name?')
my_name = input()
print(my_name)
print('My name is: ' + my_name)

# UPGRADED MENU PROGRAM 
# CREATE A PROGRAM THAT WILL PROMPT USER TO ENTER PRICE OF FOOD
# CALCULATE THE TOTAL PRICE OF FOOD

# USING 20% DISCOUNT CALCULATE THE TOTAL PRICE
print('Enter prices of 3 foods')
adobo = float(input())
hotdog = float(input())
calabasa = float(input())

print('Enter prices of 3 foods')
adobo = input('Enter adobo price: ')
hotdog = input('Enter hotdog price: ')
calabasa = input('Enter calabasa price: ')
total_price = int(adobo) + int(hotdog) + int(calabasa)
total_discounted_price = total_price - (total_price * discount)
print(total_discounted_price)
# SCRIPT RESULTS: ERROR DUE TO INPUTTED VALUES ARE IN STRING DATA TYPE
# SOLUTION: CONVERT TO DIFFERENT DATA TYPE (INT/FLOAT)

menudo = int(input('Enter the price of menudo: '))
lechon = int(input('Enter the price of lechon: '))
tuna = int(input('Enter the price of tuna: '))
discount = float(input('Enter the discount: '))
print((menudo + lechon + tuna) - ((menudo + lechon + tuna) * discount))

###### ACTIVTY 
# ENTER YOUR NAME, AGE AND ADDRESS
# AFTER THAT, PRINT THIS MESSAGE
# Hello! I am (NAME). I am (AGE) years old. I live at (ADDRESS).

name = input('Enter your name: ')
age = int(input('Enter your age: '))
address = input('Enter your address: ')
print('Hello! I am ' + name + '. I am ' + age + 
      ' years old. I live at ' + address + '.')

# FORMATING (f)
print(f"Hello! My name is: {name}, I am {age} years old and I live at {address}")

# FLOW CONTROL
# if a = 24 do this
# if b = 21 do this
# else / otherwise
# do this

# is it raining? bring umbrella
# if not bring a cap and water
# BOOLEAN - True or False
# if else

is_graduate = True

if is_graduate == True:
    print('Very good')
else: # if not / otherwise
    print('Not good')

# difference between = and ==
# = assigns a value to a variable
# == checks / comparison two values, e.g. a == b ?

Is_raining = True
if Is_raining==True:
    print("Bring umbrella")
else: #if not or otherwise
    print("Bring a cap")

# COMPARISON OPERATORS
# == equal to
# != not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

lucky_number = 17
if lucky_number > 20:
    print('Good!')
elif lucky_number >= 15:
    print('Slightly Good!')
else:
    print('Higher number!')

##### ACTIVTY 
# CREATE A PROGRAM, ENTER YOUR GRADE
# IF GREATER THAN OR EQUAL TO 90 -> PRINT ELIGIBLE FOR SCHOLARSHIP
# IF GREATER THAN OR EQUAL TO 85 -> ELIGIBLE FOR 30% DISCOUNT
# IF GREATER THAN OR EQUAL TO 75 -> REGULAR STUDENT
# BELOW 75 -> FAILED

your_grade = 91
age = 12
if your_grade >= 90 and not age >= 18:
    print('You passed! - Eligible for 100% Scholarship')
elif not your_grade >= 85:
    print('You passed! - Eligible for 30% Discount')
elif your_grade >= 75:
    print('You passed!')
else:
    print('You failed!')

# AND / OR
# AND -> BOTH CONDITIONS MUST BE TRUE (SAME TRUE)
# OR -> AT LEAST ONE MUST BE TRUE 
# NOT -> NEGATE THE CONDITION
# NOT OPERATOR: IF TRUE (NOT) == FALSE, IF FALSE (NOT) == TRUE


##### ACTIVITY 
# CREATE A VARIABLE THAT CONTAINS USERNAME AND PASSWORD
# USING INPUT() -> ENTER THAT USERNAME AND PASSWORD
#if username is incorrect and passwowrd is correct ---> print incorrect username
#if username is correct password is incorrect ---> print incorrect password
#if both are incorrect --> incorrect login credentials
#if both username and password is correct ---> print welcome {username}

username = input('Enter your username: ')
password = input('Enter your password: ')
correct_username = 'username'
correct_password = 'password'

if username != correct_username and password != correct_password:
    print('Incorrent Login Credentials. Please try again')
elif password != correct_password:
    print('Incorrent Password. Please try again')
elif username != correct_username:
    print('Incorrent Username. Please try again')
elif username == correct_username and password == correct_password:
    print(f'Welcome {username}')
else:
    print('Please try again')

# ACTIVITY 
# ENTER A NUMBER 
# DETERMINE IF THAT NUMBER IS ODD OR EVEN
# IF DIVISIBLE BY 2 == NO REMAINDER = EVEN
# IF NOT THEN = ODD

number = int(input('Enter any number: '))

if number % 2 == 0:
    print('This number is EVEN!')
else:
    print('This number is ODD!')

# 
name = "uwu"
age = 25

if name == 'Adona':
    if age == 26:
        print("You are Adona, 26")
    else: 
        print("You are Adona, but not 26")
else:
    print('Yay!')

# LOOP

# WHILE LOOP

spam = 0
if spam < 5:
    print('Hello spam')
    print(spam)

while spam <=5:
    print('Hello!')
    print(f'The value of spam is {spam}')
    spam += 1

##### ACTIVITY
# CREATE A VARIABLE THAT CONTAINS ZERO
# USE WHILE LOOP: LOOP UNTIL THAT VARIABLE IS == 100
# FOR EVERY ITERATION PRINT VALUIE OF THE VARIABLE YOU CREATED

number = 0
while number <= 100:
    print(f'Current Value: {number}')
    number = number + 1

# CREATE A VARIABLE NAMED lucky_number
# GUESS THE NUMBER (USER INPUT -- INPUT FUNCITON)
# if the entered number is correct--- 
# end the loop, otherwise continue  the loop

lucky_number = 20
guess_number = 0

while lucky_number != guess_number:
    guess_number = int(input('Guess the lucky number: '))
    if guess_number != lucky_number:
        print(f'Not Nice')
    else:
        print(f'Nice')

##### ASSIGNMENT
'''
1. Create a progam. Enter a year then that program will determine if
the year is leap year or not

-- https://www.mathsisfun.com/leap-years.html

2. Modify the lucky number program.
If you enter 3 incorrect numbers that loop will end-- Print game over 
if that is the case

3. Modify the user name and password program.
If you entered wrong credentials(Either username or password or both)
exit the loop and print your account is locked.
use while loop

4. BMI calculator
-- Enter you weight and height and age
-- calculate the BMI and classify weight categories

'''