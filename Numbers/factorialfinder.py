# Factorial finder
# The factorial of a positive integer n is defined as the product of the sequence
# n-1, n-2,...1 and the factorial of 0 is defined as being 1
# solve this using both loops and recursion

# mode = 0 for recursion, mode = 1 for loop

import pdb

mode = {'recursion': 0, 'loop': 1}


def recursion(num):
    result = 1
    if num > 1:
        result = num * recursion(num - 1)
    return result


def loop(num):
    result = num
    while num > 1:
        result = result * (num - 1)
        num -= 1
    if num == 0:
        result = 1
    return result


if __name__ == '__main__':
    method = 'loop'
    user_input = int(input('Input a number to compute its factorial: '))
    if mode[method] == 0:
        print('recursion')
        print(recursion(user_input))
    elif mode[method] == 1:
        print('loop')
        print(loop(user_input))
