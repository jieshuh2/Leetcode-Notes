
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {} #map an old node in this case the neighbor of the input node to a new deep copied node.
        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy #To avoid repeat copy we first add that to oldToNew before parising its neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        return clone(node) if node else None