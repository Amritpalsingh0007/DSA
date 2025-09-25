# https://leetcode.com/problems/word-ladder/

# tip: if the strings are lowercase consider using abcdefghijklmnopqrstuvxyz string or vise versa for upper case
# tip: if you have a unique list then consider converting it to set for faster retrieval
# tip: if you can remove in constant time then you dont need visited list for BFS.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        wordLength = len(beginWord)
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, length = queue.popleft()

            for i in range(wordLength):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        if newWord == endWord:
                            return length + 1
                        wordSet.remove(newWord)
                        queue.append((newWord, length + 1))
        return 0
                    