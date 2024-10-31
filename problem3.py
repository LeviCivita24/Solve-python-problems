"""
    Problem 3 - Arithmetic operators. 
    https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

    The provided code stub reads two integers from STDIN, a and b. Add code to print three lines
    where: 
    1. The first line contains the sum of the two numbers. 
    2. The second line contains the difference of the two numbers (first- second). 
    3. The third line contains the product of the two numbers. 
"""

if __name__ == '__main__': 
    try: 
        a = int(input().strip())
        b = int(input().strip())

        # Condiction 1
        print(a + b)
        # Condiction 2 
        print(a - b)
        # Condiction 3
        print(a * b)
    
    except ValueError: 
        print("Input two integer values")
