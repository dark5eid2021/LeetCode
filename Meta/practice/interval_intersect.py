list1 = [[3, 8], [100, 150]]
list2 = [[2, 5], [7, 10], [120, 160]]


def interval_intersect(list1, list2):
    result = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        start1, end1 = list1[i]
        start2, end2 = list2[j]

        low = max(start1, start2)
        high = min(end1, end2)

        if low <= high:
            result.append([low, high])

        if end1 < end2:
            i += 1

        else:
            j += 1
    
    return result 



print(interval_intersect(list1, list2))