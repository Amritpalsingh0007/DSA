# Use for finding shortest path for all reachable node for a given node.
# NOTE: Dijkstra's algorithm don't work in graph with negative edges
# Can be implemented using : Queue, Priority Queue (Min Heap) and Set
# Using set in not efficient and take more time complexity

# Using priorityQueue: for element (x, y) it will pop smallest element 
# based on x if x is same then consider one with smallest y
# Time Complexity : O(E * log(V))

import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        
        adjList = [[] for _ in range(V)]
        
        for u, v, weight in edges:
            adjList[u].append((v, weight))
            adjList[v].append((u, weight))
        
        distances = [float("inf")] * V
        
        priorityQueue = [(0, src)]
        distances[src] = 0
        
        while(len(priorityQueue) != 0):
            distance, node = heapq.heappop(priorityQueue)
            for adjNode, weight in adjList[node]:
                newDistance = distance + weight
                
                if newDistance < distances[adjNode]:
                    distances[adjNode] = newDistance
                    priorityQueue.append((newDistance, adjNode))
        
        return distances
    
