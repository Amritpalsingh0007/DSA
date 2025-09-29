#Using DFS

class Solution:
    def dfs(self, vertex, adjList, visited):
        visited[vertex]=2
        for i in adjList[vertex]:
            if visited[i] == 2:
                return True
            if visited[i] == 0:
                if self.dfs(i, adjList, visited):
                    return True
        visited[vertex] = 1
        return False
    def isCycle(self, V, edges):
        visited = [0] * V
        adjList = [[] for _ in range(V)]
        for u, v in edges:
            adjList[u].append(v)
        for i in range(V):
            if visited[i] == 0:
                if self.dfs(i, adjList, visited):
                    return True
        return False