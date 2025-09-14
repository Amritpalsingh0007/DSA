arr:list = [3,45,3245,345,756,83,46,2,346,348,95,7934,5,6,346,8,5,9586,7345,654]

def quick_sort(left:int, right:int):
    if left >= right:
        return
    pivot = right
    
    i = left - 1
    j = left

    while j < right:
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]

    quick_sort(left, i)
    quick_sort(i+2, right)
quick_sort(0, len(arr)-1)
print(arr)
print(sorted(arr) == arr)
            
        