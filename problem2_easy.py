"""
    Problem 2 - Loops 
    https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
    The provided code stub reads and integer, n, from STDIN. For all negative integers
    i < n, print i**2
"""

if __name__ == '__main__': 
    try: 
        n = int(input().strip())
        i = 0 # A counter is initialized
        while i < n: 
            print(i ** 2)
            i += 1
    except ValueError:
        print("Input another number")