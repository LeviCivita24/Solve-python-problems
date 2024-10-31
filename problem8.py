"""
    Problem 8 - Nested Lists
    https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

    Given the names and grades for each student in a class of N students, store them 
    in a nested list and print the name(s) of any strudent(s) having the second lowest
    grades. Note: if there are multiple students with the second lowest grade, order their names
    alphabetically and print each name on a new line. 
"""

if __name__ == '__main__': 
    records = [[input(), float(input())] for _ in range(0, int(input().strip()))]
    # The idea will be obtain grades sorted and after find the name for the runner-up
    num_values = sorted([i[1] for i in records])
    min_ = min(num_values)  
    numero_mas_cercano = min((i for i in num_values if i > min_), default=None)
    name = sorted([i[0] for i in records if i[1]==numero_mas_cercano])
    for i in name: 
        print(i)
    

    
     
    
    
    
    
    
    

    
    
    
        
        