"""
Test cases for merge k sorted lists
"""

from merge_k_lists import merge_k_lists
from test_helpers import create_linked_list, linked_list_to_list

def test_basic_case():
    """Test the main example case"""
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]

    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]
    print("✅ Basic test case passed!")

def test_edge_cases():
    """Test edge cases"""
    # Empty lists
    assert merge_k_lists([]) is None 

    # Lists with None values
    lists = [None, create_linked_list([1, 2]), None, create_linked_list([3, 4])]
    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == [1, 2, 3, 4]

    # Single list
    lists = [create_linked_list([1, 2, 3])]
    result = merge_k_lists(lists)
    assert linked_list_to_list(result) == [1, 2, 3]

    # All empty lists
    lists = [None, None, None]
    result = merge_k_lists(lists)
    assert result is None

    print("✅ Edge cases passed!")

if __name__ == "__main__":
    test_basic_case()
    test_edge_cases()