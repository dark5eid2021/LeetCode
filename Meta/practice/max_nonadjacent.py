arr = [10, 20, 50, 30]

def max_non_adjacent_sum(arr):
    n = len(arr)
    max_sum = float('-inf')

    for i in range(n):
        for j in range(n):
            if abs( i - j) > 1:
                max_sum = max(max_sum, arr[i] + arr[j])

    return max_sum

print(max_non_adjacent_sum(arr))

