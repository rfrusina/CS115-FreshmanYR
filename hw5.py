'''Robert Frusina
I pledge my honor that I have abided by the Stevens Honor System 
CS115 - Hw 5
'''
import turtle  

# Ignore 'Undefined variable from import' errors in Eclipse.

def svTree(trunkLength, levels):
    '''svTree takes in a length, and a levels, both of which are integers. It will create
    a tree recursively, using the length inputted as the initial trunk length, and the levels as the amount of 
    "layers" deep that you wish to go. This program draws it out using the imported turtle file so that the user can see 
    the tree as it is drawn out.'''
    #turtle.left(90)
    if trunkLength>0 and levels>0:
        turtle.forward(trunkLength)
        turtle.left(45)
        svTree(trunkLength/2, levels-1)
        turtle.right(90)
        svTree(trunkLength/2, levels-1)
        turtle.left(45)
        turtle.backward(trunkLength)        


def fastLucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fastLucasHelper(n, memo):
        '''This is a helper function to fastLucas. The main point of the helper function here is to 
        define what the index in dictionary is defined as. '''
        if n in memo:
            return memo[n]
        if n==0:
            result = 2
        elif n==1:
            result = 1
        else: 
            result = fastLucasHelper(n-1, memo)+fastLucasHelper(n-2, memo)
        memo[n]=result
        return result
    return fastLucasHelper(n,{})

def fast_change(amount, coins):
    ''' Takes an amount and a list of coin denominations as a input. Returns the number of coins required to total the given amount.
    Use memoization to improve performance '''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        elif amount ==0:
            result = 0
        elif coins == ():
            result = float('inf')
        else:
            if coins[0] > amount:
                result = fast_change_helper(amount, coins[1:], memo)
            else:
                useIt = 1 + fast_change_helper(amount-coins[0], coins, memo)
                loseIt = fast_change_helper(amount, coins[1:], memo)
                result = min(useIt, loseIt)
        memo[(amount, coins)]= result
        return result
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fastLucas(3))  # 4
print(fastLucas(5))  # 11
print(fastLucas(9))  # 76
print(fastLucas(24))  # 103682
print(fastLucas(40))  # 228826127
print(fastLucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


# Should take a few seconds to draw a tree.
svTree(100, 4)
