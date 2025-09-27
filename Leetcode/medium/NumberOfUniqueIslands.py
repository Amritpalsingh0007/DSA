# https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1
# There is shape normalization for island that is the main point that help in identifying similar shapes

from collections import deque
import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        marked = [[0 for _ in range(n)] for _ in range(m)]
        uniqueIslands = set()
        
        def helperBFS(x, y):
            initial_x, initial_y = x,y
            queue = deque()
            queue.append((x, y))
            directions = [(1, 0), (-1, 0),(0,1),(0,-1)]
            island = [(0,0)]
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    x += dx
                    y += dy
                    
                    if 0<=x<m and 0<=y<n and grid[x][y]==1 and marked[x][y] == 0:
                        marked[x][y]=1
                        queue.append((x, y))
                        island.append((x-initial_x, y-initial_y))
                    x-= dx
                    y -= dy
            return tuple(island)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and marked[i][j]==0:
                    marked[i][j] = 1
                    uniqueIslands.add(helperBFS(i, j))
                
        return len(uniqueIslands)