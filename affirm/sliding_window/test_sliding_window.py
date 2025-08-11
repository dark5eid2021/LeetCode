"""
Test cases for sliding window maximum
"""

from sliding_window_max import max_sliding_window

def test_sliding_window_maximum():
    """Core test cases covering main scenarios"""

    # Basic example
    nums = [1, 2, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [3, 3, 5, 5, 6, 7] 
    assert max_sliding_window(nums, k) == expected

    # Single element window
    nums = [1, 2, 3, 4, 5]
    k = 1
    expected = [1, 2, 3, 4, 5]
    assert max_sliding_window(nums, k) == expected

    # Window equals array length
    nums = [1, 3, 2, 5, 4]
    k = 5 
    expected =[5]
    assert max_sliding_window(nums, k) == expected

    # Decreasing sequence
    nums = [7, 6, 5, 4, 3, 2, 1]
    k = 3
    expected = [7, 6, 5, 4, 3]
    assert max_sliding_window(nums, k) == expected

    print("✅ All test cases passed!")

def test_edge_cases():
    """Edge cases that could break the algorithm"""

    assert max_sliding_window([], 1) == []
    assert max_sliding_window([1, 2, 3], 0) == []
    assert max_sliding_window([42], 1) == [42]

    # Negative numbers
    nums = [-1, -3, -2, -5, -4]
    k = 2
    expected = [-1, -2, -2, -4]
    assert max_sliding_window(nums, k) == expected

    print("✅ Edge cases passed!")


if __name__ == "__main__":
    test_sliding_window_maximum()
    test_edge_cases()