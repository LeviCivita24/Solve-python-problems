"""
    Problem 1: Python If-Else
    https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
    Given an integer, n, perform the following condictional actions: 
        1. if n is odd, print "weird". 
        2. if n is even and in the inclusive range of 2 to 5, print "not weird". 
        3. if n is even and in the inclusive range of 6 to 20, print "weird".
        4. if n is even and greater than 20, print "not weird" 

    method: strip() --> this method removes any leading, and trailing whitespaces.     
"""
print("Hola")
if __name__== '__main__': 
    try: 
        print("Input a integer number")
        n = int(input().strip()) 
        # Condiction number 1 
        if n%2 == 1: print("Weird") 
        else: 
            # Condiction number 2
            if 2 <= n <= 5: print("Not Weird")
            # Condiction number 3 
            elif 6 <= n <= 20: print("Weird")
            # Condiction number 4
            elif n > 20: print("Not Weird")

    except ValueError: 
        print("Input a valid number")
    