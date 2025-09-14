arr:list = [3,45,3245,345,756,83,46,2,346,348,9579345,6,346,8,5,9586,7345,654]

def selection_sort(arr:list):
    if len(arr) <= 1:
        return arr
    
    for i in range(len(arr) - 1):
        min_num_index = i+1
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_num_index]:
                min_num_index = j
        
        if arr[i] > arr[min_num_index]:
            arr[i] = arr[min_num_index] + arr[i]
            arr[min_num_index] = arr[i] - arr[min_num_index]
            arr[i] = arr[i] - arr[min_num_index]
    
    return arr

sorted_arr = selection_sort(arr=arr)
print("sorted arr: ", sorted_arr)
print("Is sorted : ", sorted_arr == sorted(arr))