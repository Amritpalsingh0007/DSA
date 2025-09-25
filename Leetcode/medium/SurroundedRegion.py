# https://leetcode.com/problems/surrounded-regions/description/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        marked = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        def helperDFS(i:int, j:int)-> None:
            for x, y in [(1,0), (0, 1), (-1, 0),(0, -1)]:
                new_x, new_y = x + i, y + j

                if 0<=new_x<len(board) and 0<=new_y<len(board[0]):
                    if marked[new_x][new_y] == 0 and board[new_x][new_y] == 'O':
                        marked[new_x][new_y] = 1
                        helperDFS(new_x, new_y)
        #left boarder
        for i in range(len(board)):
            if board[i][0] == 'O' and marked[i][0]==0:
                marked[i][0] = 1
                helperDFS(i, 0)
        #Upper boarder
        for j in range(len(board[0])):
            if board[0][j] == 'O' and marked[0][j]==0:
                marked[0][j] = 1
                helperDFS(0, j)
        
        #right boarder
        for i in range(len(board)):
            if board[i][len(board[0])-1] == 'O' and marked[i][len(board[0])-1]==0:
                marked[i][len(board[0])-1] = 1
                helperDFS(i, len(board[0])-1)

        #down boarder
        for j in range(len(board[0])):
            if board[len(board)-1][j] == 'O' and marked[len(board)-1][j]==0:
                marked[len(board)-1][j] = 1
                helperDFS(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if marked[i][j] == 0:
                    board[i][j] = 'X'
        
