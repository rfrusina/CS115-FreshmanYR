'''
Robert Frusina
I pledge my honor that I have abided by the Stevens Honor System

'''

def knapsack(capacity, items):
    '''returns the total amount of value that a knapsack can hold without exceeding the total amount of weight it can hold. takes in an integer and a list of lists with two integers in each sublist.'''
    if capacity==0:
        return [0,[]]
    if items==[]:
        return [0,[]]
    elif capacity < items[0][0]:
        return knapsack(capacity,items[1:])
    use_it = knapsack(capacity - items[0][0], items[1:])
    lose_it = knapsack(capacity, items[1:])
    use_it[0] = items[0][1] + use_it[0]
    use_it[1] = [items[0]] + use_it[1]
    if use_it[0] > lose_it[0]:
        return use_it
    return lose_it

