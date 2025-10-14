class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        i = 0 
        r= 1
        while r < len(nums) and r - i != 2 * k:
            if r - i == k:
                r += 1
                continue
            if nums[r - 1] < nums[r]:
                r += 1
            else:
                if r - i > k:
                    i = i + 1
                    r= i + 1
                else:
                    i = r
                    r += 1
        if r - i == 2 * k:
            return True
        


        return False

