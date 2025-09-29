# Link : https://leetcode.com/problems/find-eventual-safe-states/description/
# Problem Number : 802

# Using BFS/ Topological sort:
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        queue = deque()
        indegree = [0] * len(graph)
        adjList = [[] for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                adjList[j].append(i)
                indegree[i] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for i in adjList[vertex]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        result.sort()
        return result


# using DFS Topological sort
