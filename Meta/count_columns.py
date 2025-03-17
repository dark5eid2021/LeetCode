'''
Count columns in the tree - get the leftmost column index and rightmost column index of the tree
The left child is one column left of its parent
The right child is one column right of its parent

                4    
                
            2        8
                
        1     3    6    9
              
                  5 7
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(8)
root.right.left = Node(6)
root.right.left.left = Node(5)
root.right.left.right = Node(7)
root.right.right = Node(9)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
leftmost, rightmost = 0, 0

def count_columns(root: TreeNode, column_num: int):
    if not root:
        return
    
    global leftmost
    global rightmost

    leftmost = min(leftmost, column_num - 1)
    rightmost = max(rightmost, column_num + 1)

    # Total columns = rightmost - leftmost + 1

count_columns(root, 0)
print(rightmost - leftmost + 1, leftmost, rightmost)