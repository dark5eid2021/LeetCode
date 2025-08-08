"""
Problem: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Time Complexity: O(N log k) where N is total number of nodes, k is number of lists
Space Complexity: O(log k) for recursion stack in divide & conquer approach
"""

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

    def __repr__(self):
        result = []
        current = self 
        while current:
            result.append(str(current.val))
            current = current.next 
        return " -> ".join(result)
    

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Divide and Conquer Approach
    
    Strategy:
    1. Pair up lists and merge them one by one
    2. After first iteration: k/2 list remains
    3. Continue until only one list remains
    4. Uses the two-list merge as a building block

    Time: O(N log k) - each node processed log k times
    Space: O(log k) - recursion depth
    """

    if not lists:
        return None
    
    def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Helper: merge two sorted linked lists"""
        dummy = ListNode(0)
        current = dummy 

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1 
                l1 = l1.next 
            else:
                current.next = l2 
                l2 = l2.next 
            current = current.next 

        # Attach remaining nodes
        current.next = l1 or l2 
        return dummy.next 
    
    # Divide and conqure
    while len(lists) > 1:
        merged_lists = []

        # Pair up lists and merge
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_lists.append(merge_two_lists(l1, l2))

        lists = merged_lists
    
    return lists[0] if lists else None 
    