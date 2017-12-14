'''
    A happy number is defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not inclu-
de 1. Those numbers for which this process ends in 1 are happy numbers, while those that do
not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy
numbers.
'''


def squares_sum(num):
    digits = []
    while num > 0:
        digit = num % 10
        num //= 10
        digits.append(digit)
    digits = digits[::-1]
    # print(digits)
    return sum(list(map(lambda x: x ** 2, digits)))
    # return (sum(list(map(square, digits))))


def is_happy(num):
    history = []
    sum = squares_sum(num)
    while True:
        if sum == 1:
            return True
        elif sum in history[1:]:
            return False
        else:
            history.append(sum)
            sum = squares_sum(sum)


def gen_happy(numbers, start):
    happy_numbers = []
    while numbers > 0:
        if is_happy(start):
            happy_numbers.append(start)
            numbers -= 1
        start += 1
    return happy_numbers


if __name__ == '__main__':
    user_numbers = int(input('How many happy numbers you want to generate? '))
    user_start = int(input('Which number you want to start from? '))
    happy_numbers = gen_happy(user_numbers, user_start)
    print('The first {} happy numbers starts from number {} are: {}'.format(user_numbers, user_start, happy_numbers))
