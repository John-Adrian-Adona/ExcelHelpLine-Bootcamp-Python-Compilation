##### ASSIGNMENT
'''
1. Create a progam. Enter a year then that program will determine if
the year is leap year or not

-- https://www.mathsisfun.com/leap-years.html

Leap Years are any year that can be exactly divided by 4 (such as 2020, 2024, 2028, etc)
 	not	except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
 	 	yes	except if it can be exactly divided by 400, then it is (such as 2000, 2400)
'''
year = int(input('Enter Year: '))

if year < 1582:
    print('Please enter a Year from 1582 onwards.')
elif year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} IS a Leap Year')
        else:
            print(f'{year} IS NOT a Leap Year')
    else:
        print(f'{year} IS a Leap Year')
else:
    print(f'{year} IS NOT a Leap Year')

# Assignment example


# Adding Input Validation
# A function or a way to count the year (A year has 4 digit numbers)

try:
    year = (input("Enter a year: "))
    year_count = len(str(year))

    if not year.isdigit() or year_count != 4:
        print(f'{year} is not a valid year.')
    else:
        year = int(year)
        if (year%4==0 and year%100 !=0) or (year%400== 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
except ValueError as e:
    print(e)

# Instructor example
try:
    year=input("Enter a a valid year: ")  #entered year is string
    
    #Check the input year if a year has 4 digit number
    if not year.isdigit() or len(year) != 4:
          raise ValueError("The input is not a valid 4 digit number")
    # digit string 

    year_int = int(year)
    year_count = len(year)
    #Check if the year is a leap year
    if(year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
          print(f"{year_int} is a leap year")
    else:
          print(f"{year_int} is not a leap year")
except ValueError as e:
        print(e)

# Challenge: Input with Date Format (01/02/2023)

'''
2. Modify the lucky number program.
If you enter 3 incorrect numbers that loop will end-- Print game over 
if that is the case
'''

lucky_number = 20
guess_number = 0
no_of_attempts = 0

while lucky_number != guess_number and no_of_attempts != 3:
    no_of_attempts += 1

    guess_number = int(input('Guess the lucky number: '))
    if guess_number != lucky_number:
        if no_of_attempts != 3:
            print(f'Wrong! Incorrect. Try again. {3 - no_of_attempts} attempt/s remaining')
        else:
             print(f'Incorrect! GAME OVER!')
    else:
        print(f'Correct! You got the right answer!')

# Attempt 2: with Instructor Example
#Answering lucky number question
import random
lucky_number = random.randint(1,15) 
attempts = 3

while attempts > 0:
    guess = int(input("Guess the lucky number: "))
    if guess == lucky_number:
        print("Congratulations! You guess the lucky number")
        break 
    elif attempts == 1:
        attempts -= 1
        print("Game over!")
    else:
        attempts -= 1
        print(f"Incorrect! You have {attempts} attempts left")

# Try catch

'''
3. Modify the user name and password program.
If you entered wrong credentials(Either username or password or both)
exit the loop and print your account is locked.
use while loop
'''

username = ''
password = ''
correct_username = 'username'
correct_password = 'password'
no_of_attempts = 0

while no_of_attempts != 3 and not (username == correct_username and password == correct_password):
    no_of_attempts += 1
    
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == correct_username and password == correct_password:
        print(f'Welcome {username}')
    else:
        if no_of_attempts != 3:
            if username != correct_username and password != correct_password:
                print(f'Incorrent Login Credentials. Please try again. You have {3 - no_of_attempts} attempt/s remaining')
            elif password != correct_password:
                print(f'Incorrent Password. Please try again. You have {3 - no_of_attempts} attempt/s remaining')
            elif username != correct_username:
                print(f'Incorrent Username. Please try again. You have {3 - no_of_attempts} attempt/s remaining')
        else:
            print('Your account is locked. Try again later')

# Instructor Example
correct_username = 'user'
correct_password = 'pass123'

while True:
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Access granted")
        break
    else:
        if username != correct_username and password == correct_password:
            print("Invalid Username")
        elif username == correct_username and password != correct_password:
            print("Invalid Password")
        else: 
            print("Invalid Credentials")
        print("Your account is locked")
        break
'''
4. BMI calculator
-- Enter you weight and height and age
-- calculate the BMI and classify weight categories
'''

# This BMI calculation will use Metric Units (kilograms, cm, meters, etc..)
age = int(input('Enter your age: '))
weight_kg = int(input('Enter your weight (in kilograms): '))
height_cm = int(input('Enter your height (in centimeters): '))

bmi = round(weight_kg / ((height_cm / 100) ** 2), 2)

# BMI Criteria uses World Health Organization Asian-Population Criteria
if bmi < 18.5:
    bmi_status = 'Underweight'
elif bmi >= 18.5 and bmi < 23:
    bmi_status = 'Normal'
elif bmi >= 23 and bmi < 27.5:
    bmi_status = 'Overweight'
else:
    bmi_status = 'Obese'

   
print(f'At {age} years old, you are "{bmi_status}" with {bmi} kg/m^2 BMI.')
