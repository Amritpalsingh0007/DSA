arr = [1,2,3,4,5,6,7,8,9,0]

print("arr before: ", arr)

def reverse_arr(arr:list):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = reverse_arr(arr[:mid])
    right = reverse_arr(arr[mid:])
    return right + left

arr = reverse_arr(arr)
print("arr after : ", arr)