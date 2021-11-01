# Shortest path Dijstras algorithms.
# on-negative weight
# allow circle
# use the priority queue to store the distance from each node to the start vertex.
# The non-negative weight gurantee that the node pop from the heap is always the shortest distance for given node.
# If the node is already pop, then we don't want to visit it again so we use visit set to check visit.
import heapq
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        visited = set()
        time = 0
        for v, e, w in times:
            if e not in graph:
                graph[e] = Node(e)
            if v not in graph:
                node = Node(v)
                graph[v] = node
            else:
                node = graph[v]
            node.neighbors.append([e, w])
        queue = [(0, k)]

        while (len(queue) != 0):
            distance, e = heapq.heappop(queue)
            node = graph[e]
            if e in visited:
                continue
            visited.add(e)
            time = max(time, distance)
            print(node.neighbors)
            for e,w in node.neighbors:
                heapq.heappush(queue, (distance + w, e))
            
        return time if len(visited) >= n else -1
                