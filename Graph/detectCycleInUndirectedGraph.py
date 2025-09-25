#DFS Solution recursive
graph =[[], [2,8], [1,3,4], [2], [2,5], [4,6], [5,7], [6,8], [1,7,9], [8]]
tree = [[], [2, 5], [3, 4], [], [], [6, 7], [], []]

visited=[0]* (len(graph) + 1)
def containCycle(graph, curr, prev=None):    
    visited[curr] = 1
    for i in graph[curr]:
        print(curr, i, prev, sep=" : ")
        if visited[i] == 1:
            if prev != i:
                return True
            continue
        if (containCycle(graph, i, curr)):
            return True
    return False
    
print(containCycle(tree, 1))


#BFS Solution
from collections import deque
visited=[0]* (len(graph) + 1)
def containCycleBFS(graph, start):
    queue = deque()
    queue.append((start, None))
    while queue:
        vertex, prev = queue.popleft()
        visited[vertex] = 1

        for adj_vertex in graph[vertex]:
            print(f'{vertex} : {adj_vertex} : {prev}')
            if visited[adj_vertex] == 1 :
                if adj_vertex != prev:
                    return True
                continue
            queue.append((adj_vertex, vertex))
    return False
print("BFS : ")
# graph with mulitple components
graph = [[], [2, 4], [1, 3], [2], [1, 5, 6], [4], [4], [8, 9], [7, 9], [7, 8]]
# For graph with mulitple components
for i in range(1, len(graph)):
    if visited[i] == 1:
        continue
    if containCycleBFS(graph, i):
        print(True)
        exit()
print(False)

# print(f'BFS : {containCycleBFS(tree)}')