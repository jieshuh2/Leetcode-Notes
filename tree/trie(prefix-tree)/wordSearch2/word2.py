# My function: backtracking without trie: Time Exceed Limits :(
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        collection = set()
        visited = set()
        def dfs(idx, words, i, j):
            if (i,j) in visited:
                return
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            visited.add((i,j))
            words = words.copy()
            n = 0
            while n < len(words):
                if words[n][idx] != board[i][j]:
                    words.pop(n)
                    continue
                if len(words[n]) - 1 == idx:
                    collection.add(words[n])
                    words.pop(n)
                    continue
                n += 1
            dfs(idx + 1,words, i - 1, j)
            dfs(idx + 1, words, i + 1, j)
            dfs(idx + 1, words, i, j - 1)
            dfs(idx + 1, words, i, j + 1)
            visited.remove((i,j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(0, words, i, j)
        res = list(collection)
        return res
#correct result : Use Prefix Trie
#Trie:
#Each node contains a dic store all the char at this idx. Mark the node which is the end of a word
#This successfully combine words with the same prefix and highly increase the efficiency when searching.
#Use the board to guide the Trie search.
#no need to loop through all word to find the match within dfs
class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addWord(w)
        res, visited = set(), set()
        
        def dfs(word, node, i, j):
            if (i,j) in visited:
                return
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
                return
            visited.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.isWord:
                res.add(word)
            dfs(word, node, i - 1, j)
            dfs(word, node, i + 1, j)
            dfs(word, node, i, j - 1)
            dfs(word, node, i, j + 1)
            visited.remove((i,j))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs("", root, i, j)
        res = list(res)
        return res