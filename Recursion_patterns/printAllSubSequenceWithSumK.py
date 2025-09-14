arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

subsets = []
target_k = 10
count = 0
def recursiveSolution(index, subset):
    global count
    if index >= len(arr):
        if len(subset) > 0 and sum(subset) == target_k:
            subsets.append(subset.copy())
            count += 1
        return
    
    subset.append(arr[index])
    recursiveSolution(index + 1, subset)
    subset.pop()
    recursiveSolution(index+1, subset)

recursiveSolution(0, [])

for subset in subsets:
    print(f"[{','.join(map(str, subset))}]")

#Optimal Solution 
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
subsets = []
target_k = 10
def recursiveSolution(index, total, subset):
    if total == target_k:
        subsets.append(subset.copy())
        return
    if total > target_k:
        return
    if index >= len(arr):
        return
    
    subset.append(arr[index])
    recursiveSolution(index + 1, total + arr[index], subset)
    subset.pop()
    recursiveSolution(index+1, total, subset)

recursiveSolution(0, 0, [])

for subset in subsets:
    print(f"[{','.join(map(str, subset))}]")
print(f"Total subsets = {len(subsets)}")