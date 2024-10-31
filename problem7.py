"""
    Problem 7 - List Comprehensions
    https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

    You are given three integers x, y and z representing the dimensions of a cuboid along with
    an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where
    where the sum of i + j + k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. 
    Please use list comprehensions rather tan multiple loops, as learning exercise. 
"""


# First way 
if __name__ == '__main__': 
    x = int(input().strip()); y = int(input().strip()); z = int(input().strip()); n = int(input().strip()); 
    # List comprehension for each coordinate
    coord_x = [i for i in range(0, x + 1)]; coord_y = [j for j in range(0, y + 1)]; coord_z = [k for k in range(0, z + 1)]
    # Now, implement all possible permutations n! / (n! - r!) where n is the total items in the set and r is the items taken for the permutation
    permutations = [[i,j,k] for i in coord_x for j in coord_y for k in coord_z if i + j + k != n]
    print(permutations)

# Second way - more efficient
if __name__ == '__main__': 
    x = int(input().strip()); y = int(input().strip()); z = int(input().strip()); n = int(input().strip()); 
    # List comprehension for each coordinate
    coord_x = range(0, z + 1); coord_y = range(0, y + 1); coord_z = range(0, z + 1)
    # Now, implement all possible permutations n! / (n! - r!) where n is the total items in the set and r is the items taken for the permutation
    permutations = [[i,j,k] for i in coord_x for j in coord_y for k in coord_z if i + j + k != n]
    print(permutations)
    
# Exist anothe way more efficient than the previous methods but this tools use itertools that is a library to implement permutations and combinations.     

