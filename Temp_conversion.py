def fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


c=float(input("Enter degrees in celsius:"))
f=fahrenheit(c)

print(c, 'C', f, 'F')
print('%.2f C = %.2f F' % (c,f))    

f=float(input("Enter degrees in fahrenheit:"))
c=celsius(f)
print(f,'F =', c, 'C')

print()
f = float(input("Enter degrees in fahrenheit"))
assert fahrenheit(celsius(f))==f

'''
use assert to check that the return value is equal to the expected Value, no output should be produced unless the assertion fails which means
you have an error.
'''

