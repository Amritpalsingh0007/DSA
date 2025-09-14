class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        n = len(maze)
        solutions = []
        def helper(position, solution):
            if position == (n-1, n-1):
                solutions.append("".join(solution))
                return
            if position[0] > n-1 or position[1] > n - 1 or position[0] < 0 or position[1] < 0:
                return
            
            if position[0] + 1 <= n - 1 and maze[position[0] + 1][position[1]] == 1:
                solution.append("D")
                maze[position[0] + 1][position[1]] = 0
                helper((position[0] + 1, position[1]), solution)
                solution.pop()
                maze[position[0] + 1][position[1]] = 1
        
            if  position[1] - 1 >= 0 and maze[position[0]][position[1] - 1] == 1:
                solution.append("L")
                maze[position[0]][position[1] - 1] = 0
                helper((position[0], position[1]-1), solution)
                solution.pop()
                maze[position[0]][position[1] - 1] = 1
                
            if position[1] + 1 <= n - 1 and maze[position[0]][position[1]+1] == 1:
                maze
                solution.append("R")
                maze[position[0]][position[1]+1] = 0
                helper((position[0], position[1]+1), solution)
                solution.pop()
                maze[position[0]][position[1]+1] = 1
            
            if position[0] - 1 >= 0 and maze[position[0] - 1][position[1]] == 1:
                solution.append("U")
                maze[position[0] - 1][position[1]] = 0
                helper((position[0] - 1, position[1]), solution)
                solution.pop()
                maze[position[0] - 1][position[1]] = 1
        helper((0,0), [])
        return solutions

maze = [
    [1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]
]
solutions = Solution().ratInMaze(maze=maze)

print(solutions)