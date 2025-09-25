#URL: https://leetcode.com/problems/rotting-oranges/description/
#Space Complexity: O(m*n)
#Time Complexity: O(m*n)
#code:
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        grid_copy = deepcopy(grid) #Created a deepcopy so that orignal data is not changed
        fresh_count = 0
        queue = deque() #If you running locally add this import "from collections import deque"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if fresh_count == 0:
            return 0
        if not len(queue):
            return -1
        
        mintues = -1
        directions = [(1, 0), (0, 1), (-1, 0), (0,-1)]
        #simulate the rottening of oranges
        while(queue):
            length = len(queue)
            # simulate the rottening for every known rotten orange for 1 minute
            while length > 0:
                x, y = queue.popleft()
                length -= 1

                for dx, dy in directions:
                    i, j = x + dx, y + dy

                    if i == rows or i < 0 or j < 0 or j == cols:
                        continue
                    if grid_copy[i][j] == 1:
                        # decrease fresh_count and append new rotten orange to the queue
                        grid_copy[i][j] = 2
                        fresh_count -= 1
                        queue.append((i, j))
            # Increase minutes after every 1 minute simulation
            mintues += 1

        if fresh_count ==0:
            return mintues
        return -1     
