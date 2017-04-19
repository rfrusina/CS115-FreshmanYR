'''

@author:   Robert Frusina
Pledge:    I pledge my honor that I have abided by the Stevens Honor Code
CS115 - Hw 3
'''

def giveChange(amount, coins):
    if amount == 0:
        return [0,[]]
    if coins == []:
        return [float('inf'), []]
    else:
        if coins[0] > amount:
            return giveChange(amount, coins[1:])
        else:
            useIt = giveChange(amount - coins[1:])
            newSum = 1+ useIt[0]
            loseIt = giveChange(amount, coins[1:])
            if newSum < loseIt[0]:
                return [newSum, [coins[0]] + useIt[1]]
            return loseIt
    

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score. '''
    return map(lambda word: [word, wordScore(word, scores)], dct)

def wordScore(S, scorelist):
    ''' assigns word values '''
    if S == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def letterScore(letter, scoreList):
    ''' assigns each letter a value '''
    if scoreList == []:
        return 0
    elif letter == scoreList[0][0]:
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])
    


    




def take(n, L):
    '''Returns the list L[0:n].'''
    if L==[]:
        return []
    if n ==0:
        return []
    return [L[0]] + take((n-1), L[1:])

    




def drop(n, L):
    '''Returns the list L[n:].'''
    if L ==[]:
        return []
    if n ==0:
        return L 
    return drop((n-1), L[1:])

    
    


