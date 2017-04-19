#Robert Frusina
#I pledge my honor that I have abided by the Stevens Honor System

def dot(L,K):
    '''Returns the dot product of two lists of equal length'''
    if L==[] or K==[]:
        return 0.0
    return L[0]*K[0]+dot(K[1:],L[1:])

print(dot([4,2,3],[3,2,1]))

def explode(s):
    '''converts a string into a list of characters that combine to create the original string'''
    if s=="":
        return []
    return [s[0]]+explode(s[1:])

print(explode("hi"))

def ind(e,L):
    '''returns the first index at which e is found in the list L, or if it is not found, returns an integer greater than the last index of L.'''
    if L==[]:
        return 0
    elif L=="":
        return 0
    elif L[0]==e:
        return 0
    return 1+ind(e,L[1:])

print(ind(3,[1,2,3,4]))

def removeAll(e,L):
    '''returns a list identical to L, except that all instances of the value e have been removed'''
    if L==[]:
        return []
    elif L[0]==e:
        return removeAll(e,L[1:])
    return [L[0]]+removeAll(e,L[1:])

print(removeAll(2,[1,2,3,2,5,6,2,7,2,8]))

def even(X):
    if X % 2 == 0 :
        return True
    return False

def myFilter(x,L):
    '''Filters out whether a value is true or false after a function acts upon it'''
    if L==[]:
        return []
    elif x(L[0])==False:
        return myFilter(x,L[1:])
    return [L[0]]+myFilter(x,L[1:])


print(myFilter(even,[1,2,3,4,5,6,7]))

def deepReverse(L):
    '''Reverses a list, and any lists within a list'''
    if L==[]:
        return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    return deepReverse(L[1:])+[L[0]]