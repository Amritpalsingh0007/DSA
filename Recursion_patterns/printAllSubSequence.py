arr = [1,2,3]
power_set = set()
def recursivePrinter(arr):
    if len(arr) == 0:
        print("[]")
    elif len(arr) == 1:
        power_set.add(tuple(arr))
        return

    for i in range(0, len(arr)):
        recursivePrinter(arr[:i] + arr[i+1:])
    
    power_set.add(tuple(arr))
power_set.add(())
recursivePrinter(arr= arr)
for i in power_set:
    print(f"[{','.join(map(str,i))}]")
print("Total No. of subsets : ", len(power_set))

power_set = list()
#Optimal solution
def recursiveSolution(ind, subset):
    if ind >= len(arr):
        power_set.append(subset.copy())
        return
    #Picking the element
    subset.append(arr[ind])
    recursiveSolution(ind + 1, subset)
    #Not Picking the element
    subset.pop()
    recursiveSolution(ind + 1, subset)

recursiveSolution(0, [])

for i in power_set:
    print(f"[{','.join(map(str,i))}]")
print("Total No. of subsets : ", len(power_set))