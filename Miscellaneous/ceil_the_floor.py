arr = [3,3,3,4,4,5,6,7,7,8,8,8,8,9,10,11]
# ceil is the largest no. in arr that is <= target
#floor is the smallest no. in arr that is >= target
def binarySearch(target:int):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return [target, target]
        if arr[mid] < target:
            left = mid + 1
        if arr[mid] > target:
            right = mid - 1
    if arr[left] < target:
        if left != len(arr) - 1:
            return [arr[left], arr[left + 1]]
        else:
            return [arr[left], -1]
    else:
        if left != 0:
            return [arr[left - 1], arr[left]]
        else:
            return [-1, arr[left]]

print(binarySearch(2))
print(binarySearch(5))
print(binarySearch(12))
