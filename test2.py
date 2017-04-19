'''
Created on Mar 30, 2017

@author: frusi_000
'''

def tribonacci(n):
    ''' returns the nth tribonacci number. 0th number is 0, 1st number is 0, 2nd number is 1, and any number after that is the sum of the previous numbers'''
    if n<=1:
        return 0
    if n == 2 or n ==3:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) +tribonacci(n-3)


print(tribonacci(0))
print(tribonacci(2))
print(tribonacci(4))


def trib_memo(n):
    ''' returns the nth tribonacci number. 0th number is 0, 1st number is 0, 2nd number is 1, and any number after that is the sum of the previous numbers.
    Uses memoization to improve performance'''
    def trib_helper(n, memo):
        if n in memo:
            return memo[n]
        elif n<=1:
            result = 0
        elif n == 2 or n == 3:
            result = 1
        else:
            result = trib_helper(n-1, memo) + trib_helper(n-2, memo) + trib_helper(n-3, memo)
            memo[n] = result
            return result
    return trib_helper(n, {})

def test(test_num, function, arg, expected_output):
    received = function(arg)
    try:
        assert(received == expected_output)
        print('Test %d passed.' % test_num)
    except:
        if isinstance(arg, str):
            print('Test %d failed: %s(\'%s\') should be %s.' %
                  (test_num, function.__name__, arg, expected_output))
            print('   -- Received %s.' % received)
        else:
            print('Test %d failed: %s(%s) should be %s.' %
                  (test_num, function.__name__, arg, expected_output))
            print('   -- Received %s.' % received)

test(1, tribonacci, 0, 0)
test(2, tribonacci, 1, 0)
test(3, tribonacci, 2, 1)
test(4, tribonacci, 3, 1)
test(5, tribonacci, 4, 2)
test(6, tribonacci, 7, 13)
test(7, tribonacci, 9, 44)
test(8, tribonacci, 10, 81)
test(9, tribonacci, 11, 149)
test(10, tribonacci, 12, 274)

test(11, trib_memo, 0, 0)
test(12, trib_memo, 1, 0)
test(13, trib_memo, 2, 1)
test(14, trib_memo, 3, 1)
test(15, trib_memo, 4, 2)
test(16, trib_memo, 7, 13)
# If you memoize correctly, these function calls will return nearly
# instantaneously.
test(17, trib_memo, 30, 15902591)
test(18, trib_memo, 49, 1697490356184)
test(19, trib_memo, 50, 3122171529233)
test(20, trib_memo, 60, 1383410902447554)