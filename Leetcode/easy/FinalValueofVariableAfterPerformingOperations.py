class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for i in operations:
            if i[1] == "+":
                x += 1
            else:
                x -= 1
        
        return x

   
# Just a One liner for fun :)
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if i[1] == "+" else -1 for i in operations )