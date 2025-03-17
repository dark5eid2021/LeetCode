"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize pointers
        prev = None # previous node starts as none
        curr = head # current node starts at the head

        # traverse the list
        while curr is not None:
            next_node = curr.next # save the next node

            curr.next = prev # reverse the link

            # move pointers forward
            prev = curr # move the prev to the current node
            curr = next_node # move curr to the next node
        
        # prev is now the new head of the reversed list
        return prev
        