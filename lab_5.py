'''
Robert Frusina
I pledge my honor that I have abided by the Stevens Honor System

'''

from cs115 import map
import time

words = []
HITS = 10
D={}

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    if (first, second) in D:
        return D[(first, second)]
    
    if first =='':
        w = len(second)
    elif second =='':
        w = len(first)
    elif first[0] == second[0]:
        w = fastED(first[1:], second[1:])
    else:
        substitution = 1 + fastED(first[1:], second[1:])
        deletion = 1 + fastED(first[1:], second)
        insertion = 1 + fastED(first, second[1:])
        w = min(substitution, deletion, insertion)
    D[(first, second)] = w
    return w
   


def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
   '''
    return map(lambda x: (fastED(user_input,x),x),words)


def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    '''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()