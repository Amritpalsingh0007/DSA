from collections import deque

graph =[[], [2,8], [1,3,4], [2], [2,5], [4,6], [5,7], [6,8], [1,7,9], [8]]

def dfs(graph):
    visited = [0] * (len(graph) + 1)
    queue = deque()
    # queue.append(graph[1][0])
    # visited[graph[1][0]] = 1
    queue.append(1)
    visited[1] = 1
    while queue:
        vertex = queue.popleft()
        for i in graph[vertex]:
            if visited[i] == 0:
                visited[i] = 1
                queue.appendleft(i)
        print(vertex)

dfs(graph)

# SC -> O(N)
# TimeComplexity -> O(N + 2e)