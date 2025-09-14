# class Solution:
#     def __init__(self, num):
#         self.num = num
    
#     def factors(self):
#         factors_arr = [1, self.num]
        
#         for i in range(2,self.num//2 + 1):
#             if self.num % i == 0:
#                 factors_arr.append(i)
#         return factors_arr

# print(Solution(int(input("Number : "))).factors())

import math
class Solution:
    def __init__(self, num):
        self.num = num
    
    def factors(self):
        factors_arr = [1, self.num]
        
        for i in range(2, int(math.sqrt(self.num)) + 1):
            if self.num % i == 0:
                factors_arr.append(i)
                if self.num // i != i:
                    factors_arr.append(self.num//i)
        return factors_arr

print(Solution(int(input("Number : "))).factors())