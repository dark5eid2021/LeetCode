"""
Problem: Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target

Constraints:
- Each input would have exactly one solution
- You may not use the same element twice
- You can return the annswer in any order

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    """
    Hash map approach - single pass

    Strategy:
    1. Iterate through array once
    2. For each number, check if complement(target - num) exists in hash map
    3. If found, return both indices
    4. If not found, store currennt number and index in hash map

    Why this works:
    - hash map lookup is O(1) average case
    - build the map on the go, so complement will be found when the seconnd num is reached
    """


    seen = {} # value -> index mapping
    for i, num in enumerate(nums):
        complement = target - num 

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i 

    return [] # no solution found (shouldn't happen per constraints)


# test cases
def test_two_sum():
    # Test case 1: Basic example
    assert two_sum([2, 3, 11, 15], 9) == [0, 1]
    
    # Test case 2: Numbers not in order
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Test case 3: Duplicate numbers
    assert two_sum([3, 3], 6) == [0, 1]

    # Test case 4: Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


# Alternative solution - Brute Force (for comparison)
def two_sum_brute_force(nums, target):
    """
    Brute Force approach - check all pairs
    Time: O(n²) 
    Space: O(1)


    Less efficient but easier to understand
    """

    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

if __name__=="__main__":
    test_two_sum

# Interview talking points:
"""
Key points to mention during interview:

1. CLARIFY REQUIREMENTS:
   - "Can I assume there's always exactly one solution?"
   - "Can I use the same element twice?"
   - "Does the order of returned indices matter?"

2. APPROACH EXPLANATION:
   - "I'll use a hash map to store numbers I've seen with their indices"
   - "For each number, I check if its complement exists in the map"
   - "This gives us O(n) time instead of O(n²) brute force"

3. EDGE CASES:
   - Empty array (but constraints say solution exists)
   - Duplicate numbers that sum to target
   - Negative numbers

4. OPTIMIZATION:
   - Hash map provides O(1) average lookup time
   - Single pass through array
   - Early return when solution found

5. FOLLOW-UP QUESTIONS:
   - "What if there were multiple solutions?" (return all pairs)
   - "What if no solution exists?" (return empty array)
   - "What about memory constraints?" (discuss brute force trade-off)
"""