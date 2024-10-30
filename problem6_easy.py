"""
    Problem 6 - Print Function 
    https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

    The included code stub will read an integer, n, from STDIN. 
    Whithout using any string methods, try to print the following: 
    123 ... n 
    note that "..." represents the consecutive values in between. 
"""

if __name__ == '__main__': 
    n = int(input().strip())
    i = 1 # counter is initialized
    while i <= n: 
        print(i, end='')
        i += 1
    