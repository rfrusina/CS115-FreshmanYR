'''
Created on Mar 23, 2017

@author: frusi_000
'''
def divide(x,y):
    if not isinstance(x, int) and not isinstance(x, float):
        raise TypeError('x is not a number')
    if y == 0:
        raise ZeroDivisionError("Cannot divide " + str(x) + " by 0")
    return x / y

def get_string(prompt):
    s = input(prompt)
    if len(s)> 10:
        raise ValueError('String exceeds max length of 10 characters')
    return s

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print(" You did not enter a valid integer")

age = get_int("Enter your age:")
print("You are %d years old." % age)
try:
    name = get_string("Enter your name:")
except ValueError as error:
    print('Error', error)
try:
    print(divide('hi',0))
except (ZeroDivisionError, TypeError) as error:
    print('Error:', error)
    
