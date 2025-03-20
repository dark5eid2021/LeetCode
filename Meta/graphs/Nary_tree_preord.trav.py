"""

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value

"""

from typing import List
from typing import Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # to store the output result
        output = []
        self.traverse(root, output)

        return output
    
    def traverse(self, root, output):
        # base case
        if root is None:
            return 

        # append the value of the root node to the output
        output.append(root.val)

        # recursively traverse each node in the children array
        for child in root.children:
            self.traverse(child, output)