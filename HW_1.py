#Robert Frusina
# I pledge my honor that I have abided by the Stevens Honor System

from cs115 import map, reduce, add

def factorial(n):
   # Takes in a positive number n and returns its factorial 
   return reduce(lambda x, y: x * y, range(1, n+1))
def mean(L):
     #Takes in a list of numbers and finds the average of those numbers 
    return sum(L)/float(len(L))

def divides(n):
    def div(k):
        return n % k ==0
    return div

def prime(n):       #returns True if number is prime and False if its composite                
        return reduce(add,map(divides(n),range(2,n)))==0
    
print(prime(1))
    
    

















      