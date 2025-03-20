"""


"""
from typing import Optional
from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.right = right
        self.left = left

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)

            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()
        
        return levels
