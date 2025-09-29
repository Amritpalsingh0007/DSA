# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/

#step 1: topological sort
#step 2: initialize and relax each node

from typing import List
from collections import deque

class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(V)]
        indegree = [0] * V
        
        for start, end, weight in edges:
            adjList[start].append((end, weight))
            indegree[end] += 1
        
        queue = deque()
        
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        distances = [-1] * V
        distances[0] = 0
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for i, _ in adjList[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        for i in range(V):
            dist = distances[result[i]]
            if dist == -1:
                continue
            for j, weight in adjList[result[i]]:
                new_dist = weight + dist
                if distances[j] == -1 or new_dist < distances[j]:
                    distances[j] = new_dist
               
        return distances