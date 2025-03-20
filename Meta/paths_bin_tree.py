"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

"""

from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, result):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                dfs(node.left, path + '->', result)
                dfs(node.right, path + '->', result)
        result = []
        dfs(root, '', result)
        return result 