"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

"""

from collections import deque
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque()
        q.append(root)
        dummy=Node(-999) # initialize with a not null prev
        while q:
            length = len(q) # find level length
            prev = dummy
            for _ in range(length): # iterate through all nodes in the same level
                popped= q.popleft()

                if popped.left:
                    q.append(popped.left)
                    prev.next = popped.left
                    prev= prev.next

                if popped.right:
                    q.append(popped.right)
                    prev.next = popped.right
                    prev = prev.next

        return root
