# prime factorization for any integer
# for example: 30 = 2*3*5
# TODO: there would be an error with input ZERO


factors = lambda n: [x for x in range(1, n + 1) if not n % x]
is_prime = lambda n: len(factors(n)) == 2
prime_factors = lambda n: list(filter(is_prime, factors(n)))


def prime_factorize(num):
    num = int(num)
    f = prime_factors(num)
    if is_prime(num):
        return str(num)
    else:
        return str(f[0]) + "*" + str(prime_factorize(num / f[0]))


if __name__ == '__main__':
    num = input('input the integer you want to be prime factorized: ')
    print(prime_factorize(num))
