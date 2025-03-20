"""
Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

"""
from typing import List
from typing import Optional

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root: 
            return None

        node = Node(root.val) # create new node for the root

        for child in root.children:
            node.children.append(self.cloneTree(child))
            # call the method recursively passing each child and 
            # append to the children of the new node

        return node
    
    