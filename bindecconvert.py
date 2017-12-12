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
    pass



if __name__ == '__main__':
    while True:
        user_bin = int(input('Please input a binary number: '))
        test = bin_test(user_bin)
        if test:
            get_dec = binTodec(user_bin)
            print(get_dec)
        else:
            user_bin = int(input('Please input a binary number: '))

