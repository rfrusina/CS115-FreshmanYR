'''
Created on Mar 27, 2017

@author: Robert Frusina
I pledge my honor I have abided by the Stevens Honor System
'''



def binaryToNum(s):
    '''returns string back to n'''
    if s == '':
        return 0
    elif int(s[0]) == 1:
        return binaryToNum(s[1:]) + 2 ** len(s[:-1]) 
    return binaryToNum(s[1:]) + 0
    

def TcToNum(s):
    '''takes as input a string of 8 bits representing an integer 
    in two's-complement, and returns the corresponding integer'''
    if s=='':
        return 0
    elif s[0]=='1':
        return binaryToNum(s[1:])-128
    else:
        return binaryToNum(s[1:])


def isOdd(n):
    ''' determines if n is odd'''
    if n % 2 == 0:
        return False
    return True

def numToBinary(n):
    '''take a number n and converts it to binary'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) +'1'
    return numToBinary(n//2) + '0'

def padder(S):
    '''zeros added to string'''
    padded=7-len(S)
    return padded*'0'+ S

def NumToTc(n):
    '''takes as input an integer N, and returns a string representing 
    the two's-complement representation of that integer'''
    if n>=128 or n<=-129:
        return 'Error'
    if n==0:
        return 8*'0'
    if n<0:
        return '1'+padder(numToBinary(128-abs(n)))
    else:
        return '0' + padder(numToBinary(n))