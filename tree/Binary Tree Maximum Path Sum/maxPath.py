# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Sub problem for each node: 
#   Compute the maxlength of the path through it as a root node. Go both left and right.
# Notice when return, it means there is a path from its parent. So we can only go either left or right if it is not a root
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = [-math.inf]
        def maxSum(node):
            if not node:
                return 0
            maxLeft = maxSum(node.left)
            maxRight = maxSum(node.right)
            maxPath[0] = max(maxPath[0], max(maxLeft, 0) + max(0, maxRight) + node.val) # We have negative number. If smaller, drop the children.
            return max(maxLeft, maxRight, 0) + node.val
        maxSum(root)
        return maxPath[0]
            