def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j] > key and j > -1:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr