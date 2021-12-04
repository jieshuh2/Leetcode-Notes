# 1) Step1: Figure out Start point and End point: [i, j] -> [j, n - i - 1]
# 2) Step2: Group process, Make sure no overlap.
#       1. Group by layer: Layer to rotate: n//2
#       2. Four number in a rotation process.
#       3. Number of rotation Group: n - i - 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        length = n
        for layer in range(n // 2):
            for place in range(n - 2*layer - 1):
                store = None
                r = layer 
                c = layer + place
                for rotate in range(5):
                    if store != None:
                        tmp = matrix[r][c]
                        matrix[r][c] = store
                        store = tmp
                    else:
                        store = matrix[r][c]
                    newr = c
                    newc = n - r - 1
                    r = newr
                    c = newc