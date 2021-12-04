# We have only one direction, the trie isn't efficient in this case. 
# A list is enough here.
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False
#     def addWord(self,word):
#         curr = self
#         for c in word:
#             if c not in curr.children:
#                 curr.children[c] = TrieNode()
#             curr = curr.children[c]
#         curr.isWord = True
#     def contains(self, word):
#         curr = self
#         for c in word:
#             if c not in curr.children:
#                 return False
#             curr = curr.children[c]
#         return curr.isWord

#DP: 
# Defination: We declare splitable(i) to be whether s[i:] is splitable
# Induction: splitable(i) = isWord(i, j), splitable(j) (i < j)
# For simplicity, we declare the memo to be of length + 1 and set the last position to be True. 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # root = TrieNode()
        # for word in wordDict:
        #     root.addWord(word)
        wordDict = set(wordDict)
        breakable = [False]*(len(s) + 1)
        breakable[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict and breakable[j]:
                    breakable[i] = True
                    break
        return breakable[0]
            