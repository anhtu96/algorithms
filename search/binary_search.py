def binary_search(arr, key, left, right):
    middle = (left + right + 1) // 2
    if right < left:
        return None
    else:
        if key < arr[middle]:
            return binary_search(arr, key, left, middle-1)
        elif key > arr[middle]:
            return binary_search(arr, key, middle+1, right)
        else:
            return middle

def search(arr, key):
    return binary_search(arr, key, 0, len(arr)-1)