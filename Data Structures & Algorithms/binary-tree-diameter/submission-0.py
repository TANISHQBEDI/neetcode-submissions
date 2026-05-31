# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            # Get height of left and right subtrees
            left = height(node.left)
            right = height(node.right)
            
            # Diameter through this node = left_height + right_height
            self.diameter = max(self.diameter, left + right)
            
            # Return height of this node
            return max(left, right) + 1
        
        height(root)
        return self.diameter