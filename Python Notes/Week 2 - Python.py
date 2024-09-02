# Functions
# it's a block of code that does something
# A mini program within a program

def hello():
    print('Hello Python!')
    print('I love Data Science!')

hello()

# parameters and arguments

# parameter
marvin = 'Hey!'
print(marvin)

def hello(name):
    print('Hello, ' + name)

hello('Adona')

# Return values and return statements
len('Hello')

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'Ask again later'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'No'
    elif answerNumber == 5:
        return 'Patience'
    
getAnswer(2)
r = random.randint(1,5) # number between 1 to 5 
fortune = getAnswer(r)
print(fortune)

# instructor copy
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'Ask again later'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'No'
    elif answerNumber == 5:
        return 'Patience'
r = random.randint(1,5) # output is number between 1 to 5
fortune= getAnswer(r)
print(fortune)

print(getAnswer(random.randint(1,5)))

print("Hello", end=' ')
print("World")
print("CAT", "DOG", "BIRD")

# create a function / program and define a function
# create a function that will accept the grade (number)
# function will evaluate the grade and will give an output of 
# 90 above == A+ Rating
# Between 85 and 90 == A Rating
# Between 80 and 85 == B Rating
# 79 Below == C Rating

def gradeRating(grade):
    if grade >= 90:
        grade_rating = "A+"
    elif grade >= 85:
        grade_rating = "A"
    elif grade >= 80:
        grade_rating = "B"
    elif grade <= 79:
        grade_rating = "C"
    return 'You have grade rating of ' + grade_rating + '.'

gradeRating(random.randint(70,100))

# Local  scope vs Global scope (Variable and parameters)

# Code in the global scope, outside of all functions, cannot use any local
# Code in the local scope can access local variables
# Code in a functions local scope cannot use variables in any other local scope
# You can use the same name for different variables if they have different scope

# Local variables cannot be used in the global scope
def spam():
    egg = 'spam local'
    bacon()
    return egg

def bacon():
    egg= 'bacon local'
    print(egg)
    spam()
    print(egg)

print(spam())
print(egg)

bacon()
print(egg)

'''
Assignment
1. Create a function
2. Create a function: Convert meters to cm
3. Create a function: Convert inches to mm
4. Create a function: Convert feet to meters 
5. Create a function: Convert meters to kilometers 
6. Create a function: Convert kilometers to miles
Then create a program --

'''

#Assignment
#Create a function
#Create a function Convert meters to cm
#Create a function convert inches to mm
#Create a function convert feet to meters
#Create a function convert meters to kilometers
#Create a function convert kilometers to miles
#Then create a program -- create an option based on the function that you created
#the calculation will happen on the body of the function
#just return the converted values