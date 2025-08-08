# LeetCode 23: Merge k Sorted Lists - Staff Engineer Solution

## Overview
This repository contains an optimal solution for LeetCode problem 23: Merge k Sorted Lists, designed specifically for staff-level engineering interviews.

## Problem Statement
Given an array of k linked-lists, each sorted in ascending order, merge all linked-lists into one sorted linked-list.

**Example:**
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

## Files Structure
- `merge_k_lists.py` - Main solution with ListNode class and divide & conquer algorithm
- `test_helpers.py` - Utility functions for testing
- `test_cases.py` - Comprehensive test suite
- `README.md` - This file

## Running the Solution
```bash
python test_cases.py
```

## Key Interview Talking Points

### 1. Clarifying Questions
- "Are the input lists guaranteed to be sorted?" (Yes)
- "Can lists be empty or None?" (Handle gracefully)
- "Should I modify existing nodes or create new ones?" (Reuse existing)
- "What's the expected range of k and list lengths?"

### 2. Why Divide & Conquer is Optimal
- **Time Complexity**: O(N log k) where N = total nodes, k = number of lists
- **Space Complexity**: O(log k) for recursion stack
- Each node is processed exactly log k times
- Naturally parallelizable for distributed systems
- Builds on the simpler two-list merge problem

### 3. Algorithm Walkthrough
1. **Pair up lists**: Take lists two at a time
2. **Merge pairs**: Use standard two-list merge
3. **Reduce by half**: After each round, we have k/2 lists
4. **Repeat**: Continue until only one list remains

### 4. Alternative Approaches (Why Not Chosen)
- **Sequential merge**: O(N*k) - much worse time complexity
- **Heap approach**: O(N log k) time but O(k) space - good for streaming
- **Brute force**: O(N log N) - collect all values, sort, rebuild

### 5. Edge Cases Handled
- Empty input array
- All lists are None/empty
- Single list
- Lists of different lengths
- Duplicate values across lists

### 6. Production Considerations for Staff Level
- **Scalability**: How would you handle k=10,000 lists?
- **Memory**: What if lists don't fit in memory?
- **Distributed**: How to parallelize across multiple machines?
- **Monitoring**: What metrics would you track?
- **Error handling**: Invalid input, corrupted lists

### 7. Follow-up Questions
- "What if lists aren't sorted?" → Sort first, then merge
- "What about memory constraints?" → Streaming/external sort
- "How to make this real-time?" → Priority queue with lazy loading
- "How to handle very large k?" → MapReduce pattern

### 8. Time Complexity Deep Dive
```
Round 1: k lists → k/2 lists (each node processed once)
Round 2: k/2 lists → k/4 lists (each node processed once)
...
Total rounds: log k
Total work: N * log k
```

### 9. Code Quality Points
- Clean helper function separation
- Proper null handling
- Clear variable naming
- Comprehensive test coverage
- Type hints for better documentation

This problem demonstrates advanced algorithmic thinking, optimization skills, and system design considerations - perfect for staff-level interviews.