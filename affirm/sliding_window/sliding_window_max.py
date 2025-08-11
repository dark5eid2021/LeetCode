
"""
LeetCode 239: Sliding Window Maximum (Hard)
===========================================

Staff Engineer Solution: Monotonic Deque
Time Complexity: O(n) - each element added/removed at most once
Space Complexity: O(k) - deque stores at most k elements

Key insight: Use deque to maintain potential maximums in decreasing order
"""

from collections import deque
from typing import List



def max_sliding_window(nums: List[int], k:int) -> List[int]:
    """
    Optimal solution using monotonic deque*.

    Strategy:
    1. Deque stores indices in decreasing order of their values
    2. Front of deque is always the maximum for current window
    3. Remove expired indices annd indices of smaller values

    Deque invariants**:
    - Indices are in increasing order (temporal)
    - Values at those indices are in decreasing order
    - Front element is current window maximum
    """

    if not nums or k == 0:
        return []
    
    deq = deque() # store indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside current window [i - k+1, i]
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove indices of smaller elements - they can't be the max
        # while current element is in window

        while deq and nums[deq[-1]] <= nums[i]:
            deq.pop()

        deq.append(i)

        # Window is complete, add maximum to result
        if i >= k - 1:
            result.append(nums[deq[0]])
    
    return result 