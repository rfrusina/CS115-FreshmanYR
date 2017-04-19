'''
Robert Frusina
Julie Greco

I pledge my honor that I have abided by the Stevens Honor System '''


import sys
from cs115 import map, reduce, filter

# Allows up to 10000 recursive calls.
sys.setrecursionlimit(10000)

''' defines the letters to a point system '''
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], 
     ['g', 2], ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], 
     ['m', 3], ['n', 1], ['o', 1], ['p', 3], ['q', 10], ['r', 1], 
     ['s', 1], ['t', 1], ['u', 1], ['v', 4], ['w', 4], ['x', 8], 
     ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam', 'spammy', 'zzyzva']
''' assigns each letter a value '''
def letterScore(letter, scoreList):
    if scoreList == []:
        return 0
    elif letter == scoreList[0][0]:
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])
''' assigns word values '''
def wordScore(S, scorelist):
    if S == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)
''' checks if the word exists in the dictionary '''
def possibleWord(Rack, word):
    if word == "":
        return True
    elif Rack == []:
        return False
    elif word[0] not in Rack:
        return False
    elif word[0] in Rack:
        i = Rack.index(word[0])
        return possibleWord(Rack[:i] + Rack[i+1:], word[1:])
    return False
''' uses possible word to show all words that can be created from a list of characters '''
def allWords(Rack, Dictionary):
    return filter(lambda x: possibleWord(Rack, x), Dictionary)
''' returns a list of words with corresponding words '''
def scoreList(Rack):
    if Rack== []:
        return []
    return map(lambda x: [x, wordScore(x, scrabbleScores)], allWords(Rack, Dictionary))
''' compares values in order to find best possible word '''
def betterWord(x, y):
    if x[1] < y[1]:
        return y
    return x
''' finds the best scoring word '''
def bestWord(Rack):
    if Rack == "":
        return ["", 0]
    x = scoreList(Rack)
    if x != []:
        return reduce(betterWord, x)
    return ["", 0]