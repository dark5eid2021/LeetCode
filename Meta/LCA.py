class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.right = right
        self.left = left


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            # base case - null node
            if not node:
                return None
            
            # if the current node is neither p or q, return it
            if node == p or node == q:
                return node
            
            # recursion for left and right children
            left = dfs(node.left)
            right = dfs(node.right)

            # otherwise, return the non nnull child (or null if both are null)
            return left if left else right
        
        # start the DFS from the root
        return dfs(root)