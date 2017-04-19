from cs115 import reduce, filter, map

def factorial (n):
    '''returns the factorial of a number n'''
    if n==0:
        return 1
    return n* factorial(n-1)

def tower(n):
    '''Computes 2^(2^(2)) with n twos, using recursion.'''
    if n==0:
        return 1
    return 2**tower(n-1)

def tower_reduce(n):
    '''Computes 2^(2^(2)) with n twos, using reduce.'''
    def power(x,y):
        return y**x
    return reduce(power,[2]*n)


def length(lst):
    '''Returns the length of the list.'''
    if lst==[]:
        return 0
    return 1+length(lst[1:])

def reverse(lst):
    '''Takes as input a list of elements and returns the list in reverse order.'''
    if lst==[]:
        return []
    return reverse(lst[1:]) + [lst[0]]


def mystery(n):
    
    return m_help(n,0)

def m_help(n,r):                                 
    if n==0:
        return r
    return m_help(n//10, r* 10 + n % 10)


def member(x,lst): 
     '''Returns True if x is contained in the list and False otherwise.'''
    if lst==[]:
        return False
    if x== lst[0]:
        return True
    return member(x,lst[1:])

def my_map(f,lst):
     '''Returns a new list where the function f has been applied to every element in the original list.'''
    if lst== []:
        return []
    return [f(lst[0])] + my_map(f,lst[1:])

def my_reduce(f,lst):
    if lst==[]:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    if lst[:-1]==[]:
        return lst[-1]
    return f(my_reduce(f,lst[:-1]), lst[-1])

def sieve(L):
    '''Returns a list of primes in the range [2, n] computed via the sieve of Eratosthenes.'''
    if L== []: return []
    else: return [L[0]] + sieve(filter(lambda X: X % L[0] !=-0, L[1:]))
    

def fib(n):
    if n==0: return 0
    elif n==1: return 1
    else: return fib(n-1) + fib(n-2)

def powerset(lst):
    if lst==[]:
        return [[]]
    lose_it= powerset(lst[1:])
    use_it= map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

def subset(target,lst):
    if target ==0:
        return True
    if lst==[]:
        return False
    return subset(target-lst[0], lst[1:]) or subset(target, lst[1:])

def subset_with_values(target,lst):
    if target ==0:
        return (True, [])
    if lst==[]:
        return (False, [])
    use_it = subset_with_values(target-lst[0], lst[1:])
    if use_it[0]:
        return (use_it[0], [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])


def max_sum(lst):
    if lst==[]:
        return 0
    return max(lst[0] + max_sum(lst[2:]), max_sum(lst[1:]))

def max_nc_values(lst):
    if lst== []:
        return (0, [])
    use_it = max_nc_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = max_nc_values(lst[1:])
    if new_sum > lose_it[0]:
        return (new_sum, [lst[0]] + use_it[1])
    return lose_it

def LCS(S1, S2):
    if S1== '' or S2== '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:] , S2[1:])
    return max(LCS(S1, S2[2:]), LCS(S1[1:], S2))

def LCS_with_values(S1,S2):
    if S2==''  or S2 =='':
        return(0,'')
    if S1[0]==S2[0]:
        result = LCS_with_values(S1[1:], S2[1:])
        return (1 + result[0], S1[0] + result[1])
    useS1 = LCS_with_values(S1, S2[1:])
    useS2 = LCS_with_values(S1[1:], S2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

def distance(first, second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0]==second[0]:
        return distance(first[1:], second[1:])
    substitution = 1 + distance(first[1:], second[1:])
    deletion = 1 + distance(first[1:], second)
    insertion = distance(first, second[1:])



    
    

    
    
     
       


    







''' mystery is an example of tail recursion. occurs when there are no pending operations. the result of the function call at the base
case is the final answer. '''







''' every time a function is called, a stack frame is placed on the call stack. a stack frame contains the information needed by the function,
such as all the local variables. the action of placing the stack frame on the stack is called the push operation.

The base case is when the output for a given input is known, without the need for recursion. a recursive call is when a function calls itself
the argument should gradually be approaching the base case. '''

''' a function is said to have linear recursion if there is one recursive call made in a single execution of the function and the result of the
recursive call is applied to a pending operation '''


