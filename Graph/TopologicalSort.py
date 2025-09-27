# Using DFS

class Solution:
    def dfs(self, vertex, visited, stack, adjList):
        visited[vertex]=1
        for adjNode in adjList[vertex]:
            if visited[adjNode]==0:
                self.dfs(adjNode, visited, stack, adjList)
            
        stack.append(vertex)
    
    def topoSort(self, V, edges):
        adjList = [[] for _ in range(V)]
        
        for x,y in edges:
            adjList[x].append(y)
            
        
        visited = [0] * V
        stack = []
        
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, visited, stack, adjList)
        
        return stack[::-1]