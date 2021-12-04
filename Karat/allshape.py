def findallshape(board):
    res = []
    visited = set()
    def dfs(x, y, shape):
        if x < 0 or y < 0 or x > len(board) or y > len(board[0]) or (x,y) in visited:
            return
        if board[x][y] == 1:
            return
        visited.add((x,y))
        shape.push((x,y))
        board[x][y] = 1
        dfs(x + 1, y, shape);
        dfs(x - 1, y, shape);
        dfs(x, y - 1, shape);
        dfs(x, y + 1, shape);
    for i in range(len(board)):
        for j in range(len(board[1])):
            shape = []
            dfs(i, j, shape)
            res.append(shape)
    return res
def findRectangle(board):
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                start = (i, j)
                height = 0
                width = 0
                while (i + height < len(board) and board[height + i] == 0):
                    height += 1
                    board[height + i] = 1
                while (j + width < len(board) and board[width + 1] == 0):
                    width += 1
                    board[width + j] = 1
                for h in range(i, height):
                    board[h][width + j] = 1
                for w in range(i, width):
                    board[height + i][w] = 1
                end = i + height - 1, j + width - 1
            res.append((start, end))
            
