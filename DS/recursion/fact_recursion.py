'''
Factorial using recursion.
'''

def generate_factorial(num):
    if num == 0:
        return 1
    else:
        return num * generate_factorial(num -1)

print(generate_factorial(6))