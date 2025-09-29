class Solution:
    def findOrder(words):
        adjDict = { c:set() for w in words for c in  w}
        indegree = {c: 0 for c in adjDict}
        
        for i in range(len(words) - 1):
            min_len = min(len(words[i]), len(words[i+1]))
            if len(words[i])> len(words[i+1]) and words[i][:min_len] == words[i+1][:min_len]:
                return ""
            for j in range(min_len):
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in adjDict[words[i][j]]:
                        adjDict[words[i][j]].add(words[i+1][j])
                        indegree[words[i+1][j]] += 1
                    break
        

        queue = deque()
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
        
            
        result = ""
        while queue:
            vertex = queue.popleft()
            result += vertex
            for i in adjDict[vertex]:
                indegree[i] -= 1
                
                if indegree[i] == 0:
                    queue.append(i)
                    
        if len(result) != len(indegree):
            return ""
        return result
