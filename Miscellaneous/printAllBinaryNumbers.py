n = 3
binary_strings = []
def recursiveSolution(binary_string:str):
    if len(binary_string) == n:
        binary_strings.append(binary_string)
        return
    
    if len(binary_string) > n:
        return
    
    recursiveSolution(binary_string + "0")
    recursiveSolution(binary_string + "1")
recursiveSolution("")
print(f"Total binary numbers : {len(binary_strings)}")
print("\n".join(binary_strings))

binary_strings.clear()
#Follow up question make print all binary number in which there are no adjacent 1's
def recursiveSolutionPrunning(binary_string:str, flag: bool):
    if len(binary_string) == n:
        binary_strings.append(binary_string)
        return
    if len(binary_string) > n:
        return
    
    recursiveSolutionPrunning(binary_string + "0", True)
    if flag:
        recursiveSolutionPrunning(binary_string + "1", False)

recursiveSolutionPrunning("", True)
print(f"Total binary numbers : {len(binary_strings)}")
print("\n".join(binary_strings))