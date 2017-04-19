# Robert Frusina 
# I pledge my honor that I have abided the Stevens Honor System

from cs115 import map, reduce, range
from math import factorial
import math

def inverse(n):
    ''' returns the inverse of any number given '''
    return float(1/n)

def e(n):
    ''' returns the mathematical value of e using a Taylor Expansion ''' 
    return (1+sum(map(inverse,map(factorial,range(1,n+1)))))

def error(n):
    ''' Returns the absolute value of the difference between the actual value of e and the approximation in the e(n) '''
    return abs(math.e-e(n))













