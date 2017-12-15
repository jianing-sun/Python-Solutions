'''
    Implement two types of sorting algorithms:
    Merge sort and bubble sort
'''


# str_in = input('Please input the numbers you want to be order, separated with a space: ')
# num = [int(n) for n in str_in.split()]



def merge(left, right):
    i, j = 0, 0
    output = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output += left[i:]
    output += right[j:]
    return output


def merge_func(num):  # recursion
    if len(num) == 1:
        return num
    middle = int(len(num) / 2)
    left_num = merge_func(num[:middle])
    right_num = merge_func(num[middle:])
    return merge(left_num, right_num)


def bubble_sort(num):
    # output = []
    i, j = 0, 0
    while i < len(num):
        i += 1
        j = 0
        while j < (len(num) - i):
            if num[j] > num[j + 1]:
                temp = num[j]
                num[j] = num[j + 1]
                num[j + 1] = temp
            j += 1
    return num


if __name__ == '__main__':
    test = [10, 5, 2, 3, 7, 4, 8, 9]
    str_in = input('Please input the numbers you want to be order, separated with a space: ')
    num = [int(n) for n in str_in.split()]
    print(bubble_sort(num))
    print(merge_func(num))
