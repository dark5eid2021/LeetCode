"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""



from typing import List  # Import List type hinting

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive sequence in an unsorted list of integers.
        Uses a set for O(1) lookups and iterates through the set to find sequences efficiently.
        """
        longest = 0  # Variable to store the maximum length of consecutive sequence
        num_set = set(nums)  # Convert list to a set for O(1) lookups

        # Iterate through the set to find the starting points of consecutive sequences
        for n in num_set:
            # Check if 'n' is the start of a sequence (i.e., 'n-1' is not in the set)
            if (n - 1) not in num_set:
                length = 1  # Start counting the sequence length
                
                # Expand the sequence by checking if 'n + length' exists in the set
                while (n + length) in num_set:
                    length += 1
                
                # Update the longest sequence found so far
                longest = max(longest, length)
        
        return longest  # Return the maximum length found
