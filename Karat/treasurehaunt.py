import math
def treasurehaunt(board, start, end):
    visited = set()
    paths = []
    path = []
    def dfs(x, y, remainTreasure):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == -1 or (x,y) in visited:
            return False
        visited.add((x,y))
        path.append((x,y))
        if board[x][y] == 1:
            remainTreasure -= 1
        if x == end[0] and y == end[1]:
            if remainTreasure == 0:
                paths.append(path[:])
            visited.remove((x,y))
            path.pop()
            return
        dfs(x + 1, y, remainTreasure)
        dfs(x - 1, y, remainTreasure)
        dfs(x, y - 1, remainTreasure)
        dfs(x, y + 1, remainTreasure)
        path.pop()
        visited.remove((x,y))
    m, n = len(board), len(board[0])
    numTreasure = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                numTreasure += 1
    dfs(start[0], start[1], numTreasure) 
    minlen = math.inf
    res = None
    for path in paths:
        if len(path) < minlen:
            minlen = len(path)
            res = path
    return res

board3 = [
[  1,  0,  0, 0, 0 ],
[  0, -1, -1, 0, 0 ],
[  0, -1,  0, 1, 0 ],
[ -1,  0,  0, 0, 0 ],
[  0,  1, -1, 0, 0 ],
[  0,  0,  0, 0, 0 ],
]
res = treasurehaunt(board3, (5, 2), (2, 0))
print(res)
def findzeros(board, start):
    visited = set()
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or (x, y) in visited or board[x][y] != 0:
            return
        visited.add((x,y))
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
                if board[i][j] == 0:
                    count += 1
    x, y = start
    dfs(x, y)
    if count == visited:
        return True
    return False


# def validmatrix(board):
#     for i in range(len(board)):
#         for j in range(len(board[0])):
            
