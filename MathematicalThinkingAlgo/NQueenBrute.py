"""
How to place N queens on a n*n chessboard such that it doesn't attack others.
The Brute force approach struggles to generate answers for larger chess boards like 13*13.
perm is the position of queen on the chessboard
example (1, 3, 0, 2) is the position of 4 queens on a 4*4 board. [(0, 1), (1,3), (2,0), (3,2)]
"""

import itertools as it


def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True


for perm in it.permutations(range(8)):
    if is_solution(perm):
        print(perm)