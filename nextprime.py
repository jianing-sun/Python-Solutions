# Have the program find prime numbers until the user chooses
# to stop asking for the next one

def is_prime(num):
    if num > 1:
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        if num >= 3:
            for i in range(3, int(num ** 0.5 + 1), 2):
                if num % i == 0:
                    return False
    else:
        return False
    return True


def generator(num):
    num = 1 + num
    while is_prime(num) == False:
        num += 1
    return num


if __name__ == '__main__':
    prime = 1
    while True:
        # current += 1
        user_input = input('Do you want to generate a prime? y/n ')
        if user_input.lower().startswith('y'):
            prime = generator(prime)
            print(prime)
        else:
            current = 0
