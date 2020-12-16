def get_digit(number, digit_position):
    return (number // 10**digit_position) % 10

def counting_sort_for_radix(arr, digit_position):
    L = [None] * 10
    sorted_arr = []
    for i in arr:
        current_digit = get_digit(i, digit_position)
        if L[current_digit]:
            L[current_digit].append(i)
        else:
            L[current_digit] = [i]
    for i in L:
        if i:
            sorted_arr.extend(i)
    return sorted_arr


def radix_sort(arr):
    maxval = max(arr)
    digit_position = 0
    while maxval // 10**digit_position > 0:
        arr = counting_sort_for_radix(arr, digit_position)
        digit_position += 1
    return arr