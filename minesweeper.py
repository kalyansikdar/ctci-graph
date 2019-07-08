class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        stack = []
        row, col = click
        stack.append([row, col])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        visited = []
        
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                temp.append(False)
            visited.append(temp)
        
        while stack:
            row, col = stack.pop()
            
            visited[row][col] == True
            if board[row][col] == 'M':
                board[row][col] = 'X'
                
            else:
                count = 0
                for dir in directions:
                    r, c = row + dir[0], col + dir[1]
                    if dir[0] == 0 and dir[1] == 0:
                        continue
                    elif r > (len(board)-1) or r < 0 or c < 0 or c > (len(board[0])-1) or visited[r][c]:
                        continue
                    else:                            
                        if board[r][c] == 'M' or board[r][c] == 'X':
                            count += 1

                if count:
                    board[row][col] = str(count)
                else:
                    board[row][col] = 'B'
                    for dir in directions:
                        r, c = row + dir[0], col + dir[1]
                        if dir[0] == 0 and dir[1] == 0:
                            continue
                        elif r < 0 or c < 0 or r > (len(board)-1) or c > (len(board[0])-1) or visited[r][c]:
                            continue
                        elif board[r][c] == 'E':
                            board[r][c] = 'B'
                            stack.append([r,c])
                    
        return board
            
