def counting_sort_1(arr):
    maxval = max(arr)
    sorted_arr = []
    L = [None] * (maxval + 1)
    for i in arr:
        if L[i]:
            L[i].append(i)
        else:
            L[i] = [i]

    for i in L:
        sorted_arr.extend(i)
    return sorted_arr

def counting_sort_2(arr):
    maxval = max(arr)
    sorted_arr = [None] * len(arr)
    C = [0] * (maxval + 1)
    for i in arr:
        C[i] += 1
    for i in range(len(C)):
        if i > 0:
            C[i] += C[i-1]
    for i in reversed(arr):
        sorted_arr[C[i] - 1] =  i
        C[i] -= 1
    return sorted_arr