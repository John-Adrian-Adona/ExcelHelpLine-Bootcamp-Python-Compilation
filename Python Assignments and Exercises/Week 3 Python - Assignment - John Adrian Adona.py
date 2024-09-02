# Exercises | Week 3

# print out the following 
sample_list = [['batman', 'superman', 'flash'], ['iron man', 'cap america', 'thor']]

# Exercise
print(sample_list[0][0]) # print batman
print(sample_list[0][2]) # print flash
print(sample_list[1][1]) # print cap america

# Assignment

'''
Using recursion
Create a list of numbers then find the sum of all the numbers

'''
import random
list = []

def random_list_sum(list, n):
    random_number = random.randint(1, 100)
    list = list + [random_number]
    if n == 1:
        continue_program = True
        total = 0
        for values in list:
            if isinstance(values, str):
                print('Sorry, but your list contains string values')
                print('Closing the program...')
                continue_program = False
                break
            else:
                total = total + values

        while True:
            if continue_program == False:
                break
            print(f'The final list of numbers: {list}')
            print(f'The total sum of the list of values: {total}')
            break
    else:
        return random_list_sum(list, n-1)

random_list_sum(list, 3)

    
'''

Checking if a string is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. For example, "racecar" and "radar" are palindromes.
Use recursion
'''

word = 'redr'
def check_if_palindrome(word):
    reversed_word = ''
    def word_in_reverse(n, word, container):
        if n == 0:
            return container
        else:
            container = container + word[n-1]
            return word_in_reverse(n-1, word, container)
    mirrored_word = word_in_reverse(len(word), word, reversed_word)
    print(f'The word in reverse is: {mirrored_word}')

    if word == mirrored_word:
        print(f'Selected word is a palindrome.')
    else:
        return 'Selected word is not a palindrome.'

check_if_palindrome(word)

'''
Create a python program that will compute the possibility of winning the lottery.

Calculate the probability of winning the lottery.

    Parameters:
    - k: Number of numbers selected by the player.
    - n: Total number of numbers in the lottery.
    - m: Number of numbers drawn by the lottery.

    Returns:
    - The probability of winning the lottery.
'''

# n! / r! (n-r)! Combination formula for lottery winning

def lottery_odds(k, n, m):
    def factorial(number):
        if number == 0:
            return 1
        else:
            return number * factorial(number-1)
    
    def combination(total_no, chosen_no):
        return factorial(total_no) / (factorial(chosen_no) * factorial(total_no - chosen_no))

    while True:
        if m > n or k > n:
            print('Please enter k and m numbers that are less than n numbers.')
            print('- k: Number of numbers selected by the player.')
            print('- n: Total number of numbers in the lottery.')
            print('- m: Number of numbers drawn by the lottery.')
            break
        else:
            print(f'Total possible selections of the player: {k}')
            print(f'Total numbers in the lottery: {n}')
            print(f'Total numbers drawn by the lottery: {m}')
            print(f'Number of Winning Combinations: {combination(m, k) * combination(n-m, k-m)}')
            print(f'Total Number of Possible Combinations: {combination(n, k)}')
            print(f'Odds of Winning the Lottery: {combination(m, k) * combination(n-m, k-m) / combination(n, k)}')
            break


lottery_odds(6, 49, 6)

# Instructor Way

from math import comb

def lotty_prob(k,n,m):
    # calculate total number of ways to choose from k numbers from m numbers
    total_ways = comb(n,k)
    # calculate the number of favorable ways to choose k numbers from m numbers
    favorable_ways = comb(m,k)
    probability = favorable_ways / total_ways
    return probability

lotty_prob(6,49,6)