def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    return merge(L, R)

def merge(L, R):
    merged = []
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(R[j])
            j += 1
    if i < len(L):
        merged.extend(L[i:])
    if j < len(R):
        merged.extend(R[j:])
    return merged
    