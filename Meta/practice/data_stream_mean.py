from collections import deque

stream = [4, 2, 3, 5, 1, 1]
k = 4

def moving_avg(stream, k):
    window = deque(maxlen=k)
    window_sum = 0
    results = []

    for num in stream:
        window.append(num)
        window_sum += num

        if len(window) > k:
            window_sum -= window.popleft()

        current_avg = window_sum/ len(window)
        results.append(current_avg)

    return results

print(moving_avg(stream, k))