"""
How to place N queens on a n*n chessboard such that it doesn't attack others.
The Brute force approach struggles to generate answers for larger chess boards like 13*13.
perm is the position of queen on the chessboard
example (1, 3, 0, 2) is the position of 4 queens on a 4*4 board. [(0, 1), (1,3), (2,0), (3,2)]

This approach recursively searches the entire solution space.
"""


def can_be_extended_to_sol(perm):
    i = len(perm)-1
    for j in range(i):
        if i-j == abs(perm[i] -perm[j]):
            return False
    return True


def extend(perm, n):
    if len(perm) == n:
        global counter
        counter += 1
        print(perm)

    for k in range(n):
        if k not in perm:
            perm.append(k)
            if can_be_extended_to_sol(perm):
                extend(perm, n)
            perm.pop()


counter = 0
extend([], 15)
print(counter)