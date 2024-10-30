"""
    Problem 5 - Write a function 
    https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

    An extra day is added to the calendar almost every four years as February 29, 
    and the day is called a leap day. It corrects the calendar for the fact that our 
    planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

    In the Gregorian calendar, three conditions are used to identify leap years:

    1. The year can be evenly divided by 4, is a leap year, unless: 
        1.1 The year can be evenly divided by 100, it is NOT a leap year, unless: 
            1.1.1 The year is also evenly divisible by 400. Then it is a leap year. 
    
    Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
    otherwise return False. 
"""
def is_leap(year): 
    leap = False
    if year % 4 == 0 and year % 100 != 0: leap = True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: leap = True         
    return print(leap)

if __name__ == '__main__': 
    try: 
        year = int(input().strip())
        is_leap(year)
    except ValueError: 
        print('Input a valid number for the year')