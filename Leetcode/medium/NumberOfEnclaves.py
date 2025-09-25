# https://leetcode.com/problems/number-of-enclaves/description/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        marked = [[0 for _ in range(n)] for _ in range(m)]
        def helperDFS(x, y):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y] == 1 and marked[new_x][new_y]==0:
                    marked[new_x][new_y] = 1
                    helperDFS(new_x, new_y)
        
        # Upper boarder
        for j in range(n):
            if grid[0][j] == 1 and marked[0][j]== 0:
                marked[0][j] = 1
                helperDFS(0, j)
        
        # bottom boarder
        for j in range(n):
            if grid[m-1][j] == 1 and marked[m-1][j]== 0:
                marked[m-1][j] = 1
                helperDFS(m-1, j)
        
        # left boarder
        for i in range(m):
            if grid[i][0] == 1 and marked[i][0]== 0:
                marked[i][0] = 1
                helperDFS(i, 0)
        
        # right boarder
        for i in range(m):
            if grid[i][n-1] == 1 and marked[i][n-1]== 0:
                marked[i][n-1] = 1
                helperDFS(i, n-1)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if marked[i][j]==0 and grid[i][j] == 1:
                    count += 1
        
        return count