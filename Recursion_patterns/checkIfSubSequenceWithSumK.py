arr = [1,2,3,4,5,6,7,8]
target = 8
def recursiveSolution(index:int, total:int)->bool:
    if total == target:
        return True
    if total > target:
        return False
    if index >= len(arr):
        return False
    if recursiveSolution(index+1, total+arr[index]):
        return True
    return recursiveSolution(index+1, total)

print(recursiveSolution(0,0))