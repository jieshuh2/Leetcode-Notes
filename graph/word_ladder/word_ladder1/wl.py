# Step 1: 
#   Build a graph to map each word to its adjancent word. 
#       Trick: Since the word length is shorter, we use the pattern to bridge between word
# Step 2:
#   Find the shortest path. The first time we pop a word is the shortest path to reach it.
#   BFS (Unweighted graph. BFS. Like dijkstras)
from collections import deque 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + "*" + word[idx + 1:]
                if pattern not in graph:
                    graph[pattern] = set()
                graph[pattern].add(word)
        visited = set([beginWord])
        queue = deque([(beginWord, 1)])
        while (len(queue) != 0):
            word, number = queue.popleft()
            if word == endWord:
                return number
            for idx in range(len(word)):
                pattern = word[:idx] + "*" + word[idx + 1:]
                for newWord in graph[pattern]:
                    if newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, number + 1))
        return 0
# A layer by layer bfs which would be more clear.
from collections import deque 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        for word in wordList:
            for idx in range(len(word)):
                pattern = word[:idx] + "*" + word[idx + 1:]
                if pattern not in graph:
                    graph[pattern] = set()
                graph[pattern].add(word)
        visited = set([beginWord])
        queue = deque([beginWord])
        hierachy = 1
        while (len(queue) != 0):
            length = len(queue)
            for i in range(length):
                word = queue.popleft()
                if word == endWord:
                    return hierachy
                for idx in range(len(word)):
                    pattern = word[:idx] + "*" + word[idx + 1:]
                    for newWord in graph[pattern]:
                        if newWord not in visited:
                            visited.add(newWord)
                            queue.append(newWord)
            hierachy += 1
        return 0