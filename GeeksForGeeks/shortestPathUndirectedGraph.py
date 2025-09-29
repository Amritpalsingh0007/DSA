# Link : https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance
from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        n = len(adj)
        queue = deque()
        distances = [-1] * n
        queue.append(src)
        distances[src] = 0
        while queue:
            node = queue.popleft()
            
            for i in adj[node]:
                if distances[i] == -1:
                    distances[i] = distances[node] + 1
                    queue.append(i)
                
        return distances