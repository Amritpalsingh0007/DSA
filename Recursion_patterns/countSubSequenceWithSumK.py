arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target = 10
def recursiveSolution(index:int, total:int)-> int:
    if total ==target:
        return 1
    
    if total > target:
        return 0
    
    if index >= len(arr):
        return 0
    
    return recursiveSolution(index+1, total+arr[index]) + recursiveSolution(index+1, total)

print(recursiveSolution(0,0))