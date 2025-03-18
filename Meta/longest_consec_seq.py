"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n -1) not in num_set:
                length += 1
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
        return longest