'''
Robert Frusina
I pledge my honor that I have abided by the Stevens Honor System

HW 11
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns object with the same month, day, year
         as the calling object (self)'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same date, and
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day
        
    def tomorrow(self):
        '''Changes the calling object so that it represents one calendar day 
        after the original date'''
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year % 4 == 0:
            days_in_month[2] = 29
        self.day = self.day + 1
        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month = self.month + 1
            if self.month > 12:
                self.month = 1
                self.year = self.year + 1
                
    def yesterday(self):
        '''Changes the calling object so that it represents one calendar day 
        before the original date'''
        if self.month == 1 and self.day == 1: 
            self.day = DAYS_IN_MONTH[12] 
            self.month = 12
            self.year -= 1
        elif self.isLeapYear() == True and self.day == 1 and self.month == 3:
            self.day = 29
            self.month = 2
        elif self.day == 1:
            self.day = DAYS_IN_MONTH[self.month-1]
            self.month -= 1
        else: 
            self.day -= 1
    
    def addNDays(self, N):
        '''Changes the calling object so that it represents N calendar days
        after the original date'''
        for i in range(0, N):
            print(self)
            self.tomorrow()
        print(self)
        
    def subNDays(self, N):
        '''Changes the calling object so that it represents N calendar days
        before the original date'''
        for i in range(N): 
            print(self)
            self.yesterday()
        print(self)
        
    def isBefore(self, d2):
        '''Returns True if calling object is a calendar date before d2, and
        if self is d2 or after d2, returns False'''
        if self.year < d2.year:
            return True
        elif self.year == d2.year:
            if self.month < d2.month:
                return True
            elif self.month == d2.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def isAfter(self, d2):
        '''Returns True if calling object is a calendar date after d2, and
        if self is d2 or before d2, returns False'''
        if self.year > d2.year:
            return True
        elif self.year == d2.year:
            if self.month > d2.month:
                return True
            elif self.month == d2.month:
                if self.day > d2.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def diff(self, d2):
        '''Returns an integer representing the number of days between self and 
        d2'''
        count = 0  
        if self.day == d2.day and self.month == d2.month and self.year == d2.year: 
            return 0  
        if self.isBefore(d2):
            d = d2.copy()
            while not self.equals(d): 
                count -= 1
                d.yesterday()
            return count
        if self.isAfter(d2):
            d = d2.copy()
            while not self.equals(d):
                count += 1
                d.tomorrow()
            return count
    
    def dow(self):
        '''Returns a string that indicates the day of the week of the object
        that calls it'''
        d = self.diff(Date(4, 12, 2017))
        if d % 7 == 0:
            return 'Wednesday'
        elif d % 7 == 1:
            return 'Thursday'
        elif d % 7 == 2:
            return 'Friday'
        elif d % 7 == 3:
            return 'Saturday'
        elif d % 7 == 4:
            return 'Sunday'
        elif d % 7 == 5:
            return 'Monday'
        else:
            return 'Tuesday'

d = Date(11,9,2011)    
print(d.diff(Date(1,1,1899)))
