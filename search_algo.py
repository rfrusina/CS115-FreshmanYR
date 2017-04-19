'''
Created on Apr 10, 2017

@author: frusi_000
'''
from wheel.util import binary

def sequential_search(lst,key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

lst = [5,9,-2,-12,7]
print(sequential_search(lst, 99))
    
def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -low - 1

print(binary_search(lst, 9))