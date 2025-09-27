# https://leetcode.com/problems/number-of-islands/description/
# Can use bfs or dfs both are fine but bfs saves stack space
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        marked = [[0 for _ in range(n)] for _ in range(m)]
        count = 0

        def helperDFS(x, y):
            
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in directions:
                x += dx
                y += dy
                if 0<= x < m and 0<= y < n and grid[x][y]=="1" and marked[x][y] == 0:
                    marked[x][y] = 1
                    helperDFS(x, y)
                x -= dx
                y -= dy

        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == "1" and marked[i][j] == 0:
                    count += 1
                    marked[i][j] = 1
                    helperDFS(i, j)
        return count
