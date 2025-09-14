arr:list = [3,45,3245,345,756,83,46,2,346,348,9579345,6,346,8,5,9586,7345,654]

def bubble_sort(arr:list):
    if len(arr) <= 1:
        return arr
    
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    
    return arr

sorted_arr = bubble_sort(arr=arr)
print("list is mutable and in place changes are done to same object when passed in the function: \n", arr)
print("sorted arr: ", sorted_arr)
print("Is sorted : ", sorted_arr == sorted(arr))