# For DijkstraAlgo refer Graph/DijkstraAlgorithm.py
import heapq
class Solution:

    def ShortestPath(self, src, destination, edges, V):
        adjList = [[] for _ in range(V)]
        for u, v, weight in edges:
            adjList[u].append((v, weight))
            adjList[v].append((u, weight))
        
        priority_queue = [(0, src)]
        parent = [-1] * V
        distances = [float("inf")] * V
        while len(priority_queue) != 0:
            distance, node = heapq.heappop(priority_queue)
            for adjNode, weight in adjList[node]:
                newDistance = distance + weight
                if newDistance < distances[adjNode]:
                    distances[adjNode] = newDistance
                    parent[adjNode] = node
                    heapq.heappush(priority_queue, (newDistance, adjNode))
        shortest_path = [destination]
        curr_node = destination

        while curr_node != src:
            curr_node = parent[curr_node]

            if(curr_node == -1):
                print("Unable to find the path")
                return []
            shortest_path = [curr_node] + shortest_path
        return shortest_path

solve = Solution()
edges = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [1, 3, 1], [3, 4, 1]]

print(" -> ".join(map(str,solve.ShortestPath(0, 4, edges, 5))))