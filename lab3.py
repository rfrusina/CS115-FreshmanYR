# Robert Frusina
# I pledge my honor that I have abided by the Stevens Honor system


def change(amt, coins):
    ''' returns the least number of coins needed to make a certain amount '''
    def min_coins(i, amt):
        ''' returns the smaller of its two inputs '''
        if amt == 0:
            return 0
        elif i == -1 or amt < 0:
            return float('inf')
        else:
            return min(min_coins(i-1, amt), 1 + min_coins(i, amt-coins[i]))
    return min_coins(len(coins)-1, amt)



print(change(48, [1,5,10,25,50]))