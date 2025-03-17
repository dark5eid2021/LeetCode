"""
Invert the binary tree.
So we use Post Order Treversal in which first we go in Left subtree and then in Right subtree then we return back to Parent node.
When we come back to the parent node we swap it's Left subtree and Right subtree.




"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # base case
            return root
        self.invertTree(root.left) # call the left subtree
        self.invertTree(root.right) # call the right subtree
        # swap the nodes
        root.left, root.right = root.right, root.left
        return root
        