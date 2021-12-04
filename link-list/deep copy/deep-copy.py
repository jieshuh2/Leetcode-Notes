"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Two step: 
# Step 1: Copy Node. Trick: Use hashmap to map old node to new node
# Step 2: Fix pointer
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return
        curr = head
        dic = {}
        while curr != None:
            newNode = Node(curr.val)
            dic[curr] = newNode
            curr = curr.next
        curr = head
        while curr != None:
            node = dic[curr]
            node.next = dic[curr.next] if curr.next in dic else None
            node.random = dic[curr.random] if curr.random in dic else None
            curr = curr.next
        newhead = dic[head]
        return newhead
        