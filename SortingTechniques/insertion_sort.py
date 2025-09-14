arr = [1,981,6,9,61,66,315664,1348961,4984,65,41651,84,65,19,65,1,1618,61,1,96,16,51,65,6]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr == sorted(arr))
# OR
arr = [1,981,6,9,61,66,315664,1348961,4984,65,41651,84,65,19,65,1,1618,61,1,96,16,51,65,6]
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1]= key

print(arr == sorted(arr))