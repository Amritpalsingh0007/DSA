from collections import deque
# Breath First Search (BFS)
n = 5 #No. of nodes
m = 6 #No. of edges

edges = [[1,2], [2,4], [3, 4], [1, 3], [3, 5], [5, 4]]

#using List to make a graph
graph = [[] for _ in range(n+1)]
def createGraph(edges):
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

def bfs(n, graph):
    ans = []
    visited = [0 for _ in range(n+1)]
    r = 0
    queue = [graph[1][0]]
    while r < len(queue):
        if visited[queue[r]] == 0:
            visited[queue[r]] = 1
            ans.append(queue[r])
            for j in graph[queue[r]]:
                queue.append(j)
            
        r += 1
    return ans
createGraph(edges)
print(bfs(n, graph))


graph =[[], [2,8], [1,3,4], [2], [2,5], [4,6], [5,7], [6,8], [1,7,9], [8]]
print(bfs(n=9, graph=graph))


##Optimal Solution (optimize space complexity)
graph =[[], [2,8], [1,3,4], [2], [2,5], [4,6], [5,7], [6,8], [1,7,9], [8]]
def bfs_optimal(n, graph):
    ans = []
    queue = deque()
    visited = [0] * (n + 1)
    queue.append(1)
    visited[1] = 1
    while queue:
        vertex = queue.popleft()
        ans.append(vertex)
        for i in graph[vertex]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return ans

print(bfs_optimal(n=9, graph=graph))
#Time complexity -> O(n + 2e) where n is no. of nodes and e is no. of edges
#Note 2e is total degree
# Space Complexity -> O(3n)