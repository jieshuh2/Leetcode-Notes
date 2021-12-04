import random
class Game:
    def __init__(self, size, board = None, used = 0):
        self.used = used
        self.size = size
        if board:
            self.board = board
        else:
            self.board = []
            for i in range(size):
                self.board.append([0] * size)
            self.add_new_2()
        
    def add_new_2(self):
        if self.used >= self.size*self.size:
            print("Lose")
            return 
        r = random.randint(0, self.size - 1)
        c = random.randint(0, self.size - 1)
    
        while(self.board[r][c] != 0):
            r = random.randint(0, self.size - 1)
            c = random.randint(0, self.size - 1)
        self.board[r][c] = 2
        self.used += 1
    def transpose(self):
        newMatrix = [[0]*len(self.board) for _ in range(len(self.board[0]))]
        for i in range(len(self.board)):
            for j in range(self.board):
                newMatrix[i][j] = self.board[j][i]
        self.board = newMatrix
    def reverse(self):
        new_mat =[]
        for i in range(self.board):
            new_mat.append([])
            for j in range(self.board):
                new_mat[i].append(self.board[i][self.board - j])
        self.board = new_mat
    def stack(self):
        newMatrix = [[0]*len(self.board) for _ in range(len(self.board[0]))]
        for i in range(len(self.board)):
            position = 0
            for j in range(len(self.board[0])):
                if (self.board[i][j] != 0):
                    newMatrix[i][position] = self.board[i][j]
                    position += 1
        self.board = newMatrix
    def combine(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])- 1):
                if self.board[i][j] != 0 and self.board[i][j + 1] == self.board[i][j]:
                    self.board[i][j] *= 2
                    self.board[i][j + 1] = 0
                    self.used -= 1
    def left(self):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_2()
    def up(self):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.add_new_2()
        self.transpose()
    def right(self):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.add_new_2()
        self.reverse()
    def down(self):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_2()
    def printBoard(self):
        print(self.board)
board = [[2, 4, 2, 0], [0, 2, 2, 2], [0, 2, 0, 2]]
game = Game(3, board, 8)
game.printBoard()
game.left()
game.printBoard()