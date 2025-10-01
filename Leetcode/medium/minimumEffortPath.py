# Link: https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        effort = [[float("inf")] * m for _ in range(n)]
        effort[0][0] = 0
        priority_queue = [(0, 0, 0)]

        while priority_queue:
            maxEffort, i, j = heapq.heappop(priority_queue)
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy

                if 0 <= x < n and 0 <= y < m :
                    newEffort = max(abs(heights[i][j] - heights[x][y]), effort[i][j])
                    if newEffort < effort[x][y]:
                        effort[x][y] = newEffort
                        heapq.heappush(priority_queue, (newEffort, x, y))
        
        return effort[n - 1][m - 1]