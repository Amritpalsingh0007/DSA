class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length  = len(energy)
        result = float("-inf")
        for i in range(k):
            j = length - i - 1
            sumEnergy = 0
            while j >= 0:
                sumEnergy += energy[j]
                result = max(sumEnergy, result)
                j -= k
            
        
        return result