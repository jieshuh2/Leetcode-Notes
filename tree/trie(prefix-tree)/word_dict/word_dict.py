class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def searchx(curr, idx):
            if idx == len(word):
                return curr.isWord
            if word[idx] != '.':
                c = word[idx]
                if c not in curr.children:
                    return False
                else:
                    return searchx(curr.children[c], idx + 1)
            else:
                for c in curr.children:
                    if searchx(curr.children[c], idx + 1):
                        return True
                return False
        return searchx(self.root, 0)