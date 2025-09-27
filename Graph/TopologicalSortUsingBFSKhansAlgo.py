#Link :
#Khan's Algo aka Toplogical sort using BFS
#basically use indegree array instead of visited

from collections import deque
class Solution:
    
    def topoSort(self, V, edges):
        adjList = [[] for _ in range(V)]
        indegree = [0] * V
        
        for x,y in edges:
            adjList[x].append(y)
            # Caculate the indegree for each node
            indegree[y] += 1
        
        result = []
        
        queue = deque()
        
        #append vertex with indegree 0 to queue
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        # run a while loop until queue is empty
        while(queue):
            # pop the element from queue
            vertex = queue.popleft()

            # check all adj node using a for loop
            for i in adjList[vertex]:
                # first decrease indegree of the node
                indegree[i] -= 1
                # if the indegree is 0 then push it into queue
                if indegree[i] == 0:
                    queue.append(i)
            #append the vertex into the result
            result.append(vertex)
        return result
            