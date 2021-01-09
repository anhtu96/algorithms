import math

def max_heapify(arr, heap_size, i):
    l = 2*i + 1
    r = 2*i + 2
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, heap_size, largest)

def build_max_heap(arr):
    for i in reversed(range(len(arr)//2)):
        max_heapify(arr, len(arr), i)

def heap_sort(arr):
    heap_size = len(arr)
    build_max_heap(arr)
    for i in reversed(range(1, len(arr))):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, heap_size, 0)
    return arr

# priority queue
def heap_maximum(arr):
    return arr[0]

def heap_extract_max(arr):
    if len(arr) < 1:
        return "heap underflow"
    max_val = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heap_size = len(arr)
    max_heapify(arr, heap_size, 0)
    return max_val


def heap_insert(arr, key):
    arr.append(key)
    i = len(arr) - 1
    parent = (i-1) // 2
    while i > 0 and arr[parent] < arr[i]:
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent
        parent = (i-1) // 2