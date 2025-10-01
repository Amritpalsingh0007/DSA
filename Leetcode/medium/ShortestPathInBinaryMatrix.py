# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# TimeComplexity : O(n^2)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        distances= [([float("inf")] * len(grid[0])) for _ in  range(len(grid))]
        if grid[0][0] == 1:
            return -1
        distances[0][0] = 1
        
        n = len(grid)

        queue = deque([(1, 0, 0)])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while queue:
            distance, i, j = queue.popleft()
            
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    newDistance = distance + 1
                    if distances[x][y] > newDistance:
                        distances[x][y] = newDistance
                        queue.append((newDistance, x, y))
                
        if distances[n-1][n-1] == float("inf"):
            return -1
        return distances[n-1][n-1]
