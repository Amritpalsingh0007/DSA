class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]

        for index in range(1, len(words)):
            current = words[index]
            prev = words[index - 1]

            if sorted(current) != sorted(prev):
                res.append(current)
        
        return res
