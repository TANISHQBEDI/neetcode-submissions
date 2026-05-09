# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:

        maxD = 0
        def findMaxD(root, currD):
            nonlocal maxD
            if not root:
                return
            if not root.left and not root.right:
                maxD = max(maxD, currD)
            findMaxD(root.left, currD + 1)
            findMaxD(root.right, currD + 1)
        findMaxD(node, 1)
        return maxD