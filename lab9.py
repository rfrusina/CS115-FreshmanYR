'''
Created on Mar 30, 2017

@author: Robert Frusina
'''


def mult(c,n):
    ''' Mult uses a loop and addition to multiply c by the integer n'''
    result = 0
    for x in range(n):
        result = result + c
    return result

def update(c,n):
    ''' update starts with z=0 and runs z=z**2 + c for a total of n times. returns the final z.'''
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    ''' takes in c for the update step of z = z**2 + c n the max number of times to run that step. returns false as soon as abs(z) gets larger than 2
    true if abs(z) never gets larger than 2'''
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel(col,row):
    '''returns true if we want the pixel at col, row and false otherwise'''
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False

def test():
    '''function to demonstrate how to create and save a png image'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col,row)== True:
                image.plotPoint(col, row)
    image.saveFile()

def scale(pix, pixelMax, floatMin, floatMax):
    '''scale takes in pix, the current pixel column(or row) pixMax, the total # of pixel columns, floatMin, the min floating point value
    floatMax, the max floating point value, scale returns the floating point value that corresponds to pix'''
    return((floatMin) + (pix/pixelMax) * (floatMax - floatMin))

def mset():
    ''' creates a 300x200 image of the Mandelbrot set'''
    width = 300
    height = 200
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(width):
            x = scale(col, width, -2.0, 1)
            y = scale(row, height, -1.0, 1)
            if inMSet(x + y *1j, 25):
                image.plotPoint(col,row)
    image.saveFile()


print(mset())
