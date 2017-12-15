# A binary/decimal convertor
# you can convert a binary number to decimal or a decimal number to binary
# note that reduce is a good function, it can transfer a list of digits to one number they correspond to
# we know that we can't simply convert a digit to a string (1 -> '1' is difficult


from functools import reduce

def binTodec(bin):
    if not isinstance(bin, int):
        try:
            bin = int(bin)
        except:
            raise TypeError
    dec = 0
    i = 0
    while bin > 0:
        dec += (bin % 10) * (2 ** i)
        bin //= 10
        i += 1
    return dec


def bin_test(bin):
    while bin > 0:
        if (bin % 10) != 0 and (bin % 10) != 1:
            print('Not a BINARY number')
            return False
            break
        else:
            bin //= 10
    return True


def decTobin(dec):
    i = 0
    bin = list()
    while (dec / 2) != 0:
        temp = dec % 2
        dec //= 2
        bin.append(temp)
    bin = bin[::-1]
    return reduce(lambda x,y: x*10 + y, bin)


if __name__ == '__main__':
    while True:
        user_bin = int(input('Please input a binary number: '))
        test = bin_test(user_bin)
        if test:
            get_dec = binTodec(user_bin)
            print(get_dec)
        else:
            user_bin = int(input('Please input a binary number: '))
        user_dec = int(input('Please input a decimal number: '))
        get_bin = decTobin(user_dec)
        print(get_bin)
