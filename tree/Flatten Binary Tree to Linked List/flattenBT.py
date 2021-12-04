#This solution is like the idea of merge-sort or induction. We assume the recursion function will do the right thing for us at each step
# What we do is to combine the result.
# At each node, we assume the recursion will correctly turn its left and right child to link-list. 
# We want to merge the leftlist to the rightlist.

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if node == None:
                return None
            leftTail = dfs(node.left) #end of the leftlinkedlist
            rightTail = dfs(node.right) #end of the rightlinkedlist
            if leftTail: #merge left to right
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            return rightTail or leftTail or node #If the rightlist is empty, the tail will be the end of the left array.
                                                 #If they both are empty, then it is a leaf node, simply return it.
        dfs(root)