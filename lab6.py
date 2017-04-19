'''
Created on 3-2-2017
@author:   Robert Frusina
Pledge:    I pledge on my honor that I have abided by the Stevens Honor System. 

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

print(isOdd(42))
print(isOdd(43))

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n%2==1:
        return numToBinary(int(n/2))+'1'
    return numToBinary(n/2)+'0'
    
print(numToBinary(45))        

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif len(s)==1:
        return int(s)
    return 2*binaryToNum(s[:-1])+ int(s[-1])


print(binaryToNum(''))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s[-1]=='0':
        return s[:-1]+'1'
    elif s=='11111111':
        return '00000000'
    return increment(s[:-1])+'0'

print(increment('00111010'))
print(increment('00000111'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n==0:
        print(s)
    else:
        print(s)
        s=increment(s)
        count(s,n-1)
print(count('00000000',4))

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n%3==1:
        return numToTernary(int(n/3))+'1'
    elif n%3==2:
        return numToTernary(int(n/3))+'2'
    return numToTernary(n/3)+'0'

print(numToTernary(42))
print(numToTernary(4242))


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    if len(s)==1:
        return int(s)
    return 3*ternaryToNum(s[:-1])+int(s[-1])

print(ternaryToNum('1120'))\