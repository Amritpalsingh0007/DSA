arr = [1,2,3]

def recursiveApproach(index, total, subset):
    if index >= len(arr):
        print(f"[{','.join(map(str, subset))}] -> {total}")
        return
    subset.append(arr[index])
    recursiveApproach(index + 1, total + arr[index], subset)
    subset.pop()
    recursiveApproach(index+1, total, subset)

recursiveApproach(0, 0, [])

# Time Complexity : O(2^n)
# Space Complexity : O(n)