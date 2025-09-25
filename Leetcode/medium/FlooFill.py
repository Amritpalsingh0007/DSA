#URL: https://leetcode.com/problems/rotting-oranges/description/
#Space Complexity: O(m*n)
#Time Complexity: O(m*n)
#code:
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        if startingColor == color:
            return image
        rows, cols = len(image), len(image[0])
        queue = deque() #from collections import deque #If you are running locally
        image[sr][sc] = color
        queue.append((sr, sc))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        #BFS
        while queue:
            x, y = queue.popleft()
            
            #Checking all directions
            for dx, dy in directions:
                i, j = x + dx, y + dy
                #validating index and matching color of that index if valid
                if 0<=i<rows and 0<=j<cols and image[i][j] == startingColor:
                    #Changing color and appending index into queue
                    image[i][j] = color
                    queue.append((i, j))
        return image