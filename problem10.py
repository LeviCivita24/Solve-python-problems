"""
    Problem 10 - Lists
    https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

    You are given a string and your task is to swap cases. In other words, convert all 
    lowercase letters to uppercase letters and viceversa. 

    FUNCTION DESCRIPTION: complete the swap_case function in the editor below. swap_case
    has the following parameters: 
        
    INPUT: 
        1. A single line containing a string s.  
    RETURNS: 
        1. string: the modified string. 
"""

def swap_case(s):
    str_ = list(s)
    new_str = []
    for i in str_: 
        if i == i.upper(): new_str.append(i.lower())
        else: new_str.append(i.upper())

    return ''.join(new_str)

if __name__ == '__main__':
    str_ = str(input())
    print(swap_case(str_))