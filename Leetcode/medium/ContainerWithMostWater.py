#Basic two pointer solution

class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0 #i points at starting 
        j = len(height) - 1 #j points at last element
        res = 0

        while i < j:
            #store max area
            res = max(res, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                #if height at i is less then height at j then we increase i
                i += 1
            else:
                #else we decrease j
                j -= 1

        #return the max area
        return res
