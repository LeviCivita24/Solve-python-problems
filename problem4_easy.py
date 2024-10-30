"""
    Problem 4 - Python: Division
    https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true

    The provided code stub reads two integers, a and b, from STDIN. Add logic to print two lines. 
    The first line should contain the result of integer division, a // b. The second line should
    contain the result of float division, a / b. 
    No rounding or formatting is neccesary. 
"""

if __name__ == '__main__': 
    try: 
        a = int(input().strip())
        b = int(input().strip())
        
        # Condiction 1 
        print(a // b) 
        # Condiction 2
        print(a / b)

    except ValueError: 
        print("Input a valid integer numbers")