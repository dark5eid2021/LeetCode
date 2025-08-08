"""
Helper functions for testing merge k sorted lists
"""

from typing import List, Optional 
from merge_k_lists import ListNode

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Create linked list from list of values"""
    if not values:
        return None 

    head = ListNode(values[0])
    current = head 
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head 

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to Python list for testing"""
    result = []
    current = head 
    while current:
        result.append(current.val)
        current = current.next 
    return result