'''Created on 21 March, 2017
@author:   Robert Frusina
Pledge:    I pledge on my honor that I have abided by the stevens honor system

CS115 - Hw 7
'''

FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }


def numToBaseB(N, B):
    '''converts a number N to binary from its specific base B'''
    add = N%B
    if N <= 1:
        return str(N)
    else:
        return str(numToBaseB(N//B,B))+ str(add)

print (numToBaseB(4, 2))
print (numToBaseB(4, 3))


def baseBToNum(S, B):
    '''opposite function of numToBase... converts binary to the respective value of your choice of base'''
    if S == '':
        return 0 
    return int(S[0]) * (B **(len(S) - 1)) + baseBToNum(S[1:], B)
    
print (baseBToNum("11", 2))
print (baseBToNum("11", 3))


def baseToBase(B1, B2, SinB1):
    '''this function takes in a number in the first base and converts it to the same number in the second base'''
    if B1 == '' or B2 == '':
        return ''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

print (baseToBase(2, 10, "11"))
print (baseToBase(10, 2, "3"))


def add(S, T):
    '''converts numbers to binary and adds them up.'''
    if S == '' and T == '' :
        return str(0)
    M = numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)
    return M

print (add('11','01'))
print (add("110", "011"))

def addB(S, T):
    '''same thing as add...other thans the fact that there is no conversion '''
    def add(S, T, C):
        if S == "" and T == "" and C == "0":
            return ""
        elif S == "" and T == "" and C == "1":
            return "1"
        elif S == "":
            a = '0'
            b = T[-1]
            c = C[0]
            ans, co = FullAdder[(a,b,c)]
            return add(S, T[:-1], co) + ans
        elif T == "":
            a = S[-1]
            b = '0'
            c = C[0]
            ans, co = FullAdder[(a,b,c)]
            return add(S[:-1], T, co) + ans
    
        a = S[-1]
        b = T[-1]
        c = C[0]
        ans, co = FullAdder[(a,b,c)]
        return add(S[:-1], T[:-1], co) + ans
    return add(S, T, '0')\

print (addB("11", "1"))
print (addB("011", "100"))