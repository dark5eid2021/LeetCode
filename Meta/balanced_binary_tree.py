"""
Given a binary tree, determine if it is height-balanced

"""
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Soltion:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.Height(root) >= 0)
    
    def Height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        
        leftHeight, rightHeight = self.Height(root.left), self.Height(root.right)
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
            return -1
        
        return max(leftHeight, rightHeight) + 1