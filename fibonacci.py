# Fibonacci Sequence Generator
# Have the user enter a number and
# generate a fibonacci sequence
# which size is equivalent to that number
# 12/08/2017
# Jianing Sun

def user_input():
    user_num = input('Please enter an integer: ')
    while user_num.isdigit() == False:
        user_num = input('Please enter an INTEGER: ')  # Todo: try another warning approach by try-else-finally
    user_num = (int)(user_num)
    return user_num


def gen_fibonacci(num):
    fibonacci = [1]
    fibonacci.append(1)
    for i in range(1, num):
        if i >= 2:
            sequence = fibonacci[i - 1] + fibonacci[i - 2]
            fibonacci.append(sequence)
    for j in range(len(fibonacci)):
        fibonacci[j] = str(fibonacci[j])
    # print('The generated fibonacci sequence is: %s' % fibonacci)
    print(','.join(fibonacci))


if __name__ == '__main__':
    game_state = True
    while game_state:
        user_num = user_input()
        gen_fibonacci(user_num)
        try_again = input('Do you want to try again? y/n ')
        if try_again == 'y':
            game_state = True
        else:
            game_state = False
            print('Thank you. Have a nice day.')
