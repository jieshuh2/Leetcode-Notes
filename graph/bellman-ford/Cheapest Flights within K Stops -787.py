#Bellman Fords Algorithms
# k is the longest path length. 
# shortestLength(v, k) = min(shortestLength(v, k - 1), min(shortestLength(w, k-1) + Edgelength(w, v) for all Edge w->v)
# time Complexity V E
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        length = [float("inf")]*n
        length[src] = 0
        for i in range(k + 1):
            temp = length.copy()
            for w, v, weight in flights:
                temp[v] = min(temp[v], length[w] + weight)
            length = temp
        return length[dst] if length[dst] != float("inf") else -1