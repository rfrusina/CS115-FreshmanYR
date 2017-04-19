from cs115 import map, reduce, range 


def dbl(x):
    ''' returns double of  a number entered'''
    return 2*x

def add(x,y):
    ''' returns the sum of two numbers '''
    return x+y

def sqr(x):
    ''' returns the number squared '''
    return x*x


def span(lst):
    ''' returns the difference between the maximum and minimum numbers in the list '''
    return reduce(max,lst) - reduce(min,lst)

def gauss(n):
    ''' takes in a positive integer n and returns the sum of the first n integers '''
    return reduce(add, range(1, n+1)

def sum_of_squares(n):
    return reduce(add,map(sqr,range(1,n+1)))


    
    

lst=[3,4,5]
doubled =map(dbl,lst)
print(doubled)
    
    



