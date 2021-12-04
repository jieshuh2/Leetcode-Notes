#Notice the two diagnal is r + c and r - c
#Explore all the path: backtracking
class Solution:
    def totalNQueens(self, n: int) -> int:
        colum = set()
        positivediagnol = set()
        negativediagnol = set()
        count = [0]
        def dfs(n, r):
            if (r >= n):
                count[0] += 1
                return
            for c in range(n):
                if c not in colum and (r - c) not in positivediagnol and (r + c) not in negativediagnol:
                    colum.add(c)
                    positivediagnol.add(r - c)
                    negativediagnol.add(c + r)
                    dfs(n, r + 1)
                    colum.remove(c)
                    positivediagnol.remove(r - c)
                    negativediagnol.remove(c + r)
        dfs(n, 0)
        return count[0]