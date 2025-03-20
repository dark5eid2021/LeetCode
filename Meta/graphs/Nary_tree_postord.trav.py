"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value


"""

from typing import Optional
from typing import List

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []

        def dfs(root):
            # recursively call dfs for each child of the current node
            for x in root.children:
                dfs(x)

            # append the value of the current node to the result list
            res.append(root.val)

        dfs(root)

        # return the result list containing node values in post order
        return res