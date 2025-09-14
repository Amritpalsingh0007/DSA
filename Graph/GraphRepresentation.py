n = 5 #No. of nodes
m = 6 #No. of edges

edges = [[1,2], [2,4], [3, 4], [1, 3], [3, 5], [5, 4]]

# Using Matrix
graph = [[0 for _ in range(n + 1)] for _ in range(n+1)]

def createGraphUsingMatrix(edges):
    for edge in edges:
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
createGraphUsingMatrix(edges)
print(graph)
# Space Complexity -> O(n^2)

#Using List
graph = [[] for _ in range(n+1)]

def createGraphUsingList(edges):
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

createGraphUsingList(edges)
print(graph)
# Space Complexity -> O(2E) -> O(m) here E is no. of edges


#Using dict
graph = dict()
def createGraphUsingDict(edges):
    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]

createGraphUsingDict(edges)
print(graph)