'''
Created on March 7, 2017
@author:   Robert Frusina and Julie Greco
Pledge:    I pledge on my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n%2==1:
        return numToBinary(int(n/2))+'1'
    return numToBinary(n/2)+'0'


def counter(S,num):
    '''This function takes in a 64 bit binary statement, S, and a number, num, and checks to see how many times the number 
    occurs in the 64 bit statement.'''
    if S=="":
        return 0
    if S[0]!= num:
        return 0
    return 1+ counter(S[1:],num)
    

def zeros(x):
    '''This function makes sure that the bit has zeros up until the 5 mark'''
    return (COMPRESSED_BLOCK_SIZE-len(x))*"0"+x 
    

def helpMeCompress(S,num):
    '''Takes in two numbers, and recurses through 0 and 1.'''
    if S=="":
        return "" 
    x=counter(S,num)
    if x>MAX_RUN_LENGTH:
        x=MAX_RUN_LENGTH
    return zeros(numToBinary(x))+helpMeCompress(S[x:],str(1-(int(num))))

def compress(S):
    '''Uses the help me compress function in order to compress the bit into the compressed
    version of itself. The way it works is that it uses helpmecompress, but has automatically defined
    num as zero. '''
    return helpMeCompress(S,"0")

print (compress(16*'1'+16*"0"+16*"1"+16*"0" ))


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif len(s)==1:
        return int(s)
    return 2*binaryToNum(s[:-1])+ int(s[-1])


def helpMeUncompress(a,c):
    '''Does the heavy lifting in the form of recursion in order to uncompress a block into 
    its original 64 bit form.'''
    if a=='':
        return ''
    return binaryToNum(a[:COMPRESSED_BLOCK_SIZE])*c+helpMeUncompress(a[COMPRESSED_BLOCK_SIZE:], str(1-int(c)))
'''
uses the help me uncompress function and uncompresses the 5 bit binary back to 64
'''
def uncompress(a):
    return helpMeUncompress(a,'0')

def compression(a):
    '''This function is used to find the ratio of the output to input of compress and uncompress.'''
    return len(compress(a))/(len(a)*1.0)



'''Such a program does NOT exist because in order to compress a 64 bit intake, it must spew out a minimum number of digits, sometimes that number is longer 
than the actual amounts of digits being imported. '''
