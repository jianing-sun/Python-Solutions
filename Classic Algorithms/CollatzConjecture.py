'''
    Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''


def collatz(num, count=0):
    if num <= 1:
        return count
    if num % 2 == 0:
        return collatz(num / 2, count+1)
    else:
        return collatz(3 * num + 1, count+1)


if __name__ == '__main__':
    user_num = int(input('please input an integer larger than 1: '))
    result = collatz(user_num)
    print('Number of steps of collatz conjecture for input {} is {}'.format(user_num, result))
