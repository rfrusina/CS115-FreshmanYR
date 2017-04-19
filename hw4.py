''' Robert Frusina
I pledge my honor that I have abided by the Stevens Honor System '''

def pascal_helper(a):
    if a==0:
        return 1
    return 2*pascal_helper(a-1)

print(pascal_helper(1))
print(pascal_helper(5))


def add_row(L):
    '''returns the sum of the value of the first and second element in the list with a one added to the end'''
    if L[1:] == []:
        return [1] 
    return [L[0] + L[1]] + add_row(L[1:])

def pascal_row(n):
    '''Returns the row n of the pascal triangle. If you want to see the first row, input 0, the second row, input 1, and so forth. '''
    if n == 0:
        return [1]
    L = pascal_row(n - 1)
    return [1] + add_row(L) 
print(pascal_row(1))
print(pascal_row(5))
print(pascal_row(4))
print(pascal_row(9))
print(pascal_row(11))



def pascal_triangle(x):
    '''This returns the full pascal triangle of the given n. If you enter in 0, it will return [1]. if you enter in 5, it will return the rows of the triangle in increasing order within a list. '''
    if x==0:
        return [pascal_row(0)]
    return pascal_triangle(x-1)+[pascal_row(x)]
print(pascal_triangle(3))
print(pascal_triangle(5))
print(pascal_triangle(7))
print(pascal_triangle(9))
print(pascal_triangle(11))