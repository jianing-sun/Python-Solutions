# simple calculator
# the point here is str and int can't be added or sth, we can transfer int to str and then do calculation

def calculator(a, b, symbol):
    if symbol == '+':
        return str(a) + symbol + str(b) + '=' + str((a + b))
    elif symbol == '-':
        return str(a) + symbol + str(b) + '=' + str((a - b))
    elif symbol == '*':
        return str(a) + symbol + str(b) + '=' + str((a * b))
    elif symbol == '/':
        return str(a) + symbol + str(b) + '=' + str((a / b))


if __name__ == '__main__':
    user_a = float(input('Please input the first number: '))
    user_b = float(input('Please input the second number: '))
    user_symbol = str(input('Please input the symbol: +, -, *, /: '))
    result = calculator(user_a, user_b, user_symbol)
    print(result)
