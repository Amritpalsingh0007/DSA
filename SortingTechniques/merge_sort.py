"""
Although it is also the implementation of the mergeSort 
but this one is not inplace we can have a inplace version of the same that scales better
"""
arr = [1,981,6,9,61,66,315664,1348961,4984,65,41651,84,65,19,65,1,1618,61,1,96,16,51,65,6]

def mergeSort(arr: list)->list:
    if len(arr) == 1:
        return arr
    res:list = []
    mid:int = len(arr)//2
    left:list = mergeSort(arr[:mid])
    right:list = mergeSort(arr[mid:])
    i:int = 0
    j:int = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    while i < len(left):
        res.append(left[i])
        i += 1
    
    while j < len(right):
        res.append(right[j])
        j += 1
    
    return res

print(sorted(arr) == mergeSort(arr))

"""
Better version of the merge sort.
"""
arr = [1,981,6,9,61,66,315664,1348961,4984,65,41651,84,65,19,65,1,1618,61,1,96,16,51,65,6]
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(n1):
        left_arr[i] = arr[left + i]
    for j in range(n2):
        right_arr[j] = arr[mid + j + 1]
    
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = left_arr[i]
        k += 1
        i += 1 
    
    while j < n2:
        arr[k] = right_arr[j]
        k += 1
        j += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = len(arr)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

print(sorted(arr) == mergeSort(arr))