


def merge_arrays(arrayA, arrayB):
    # Merge arraA and arrayB
    # Remove dupes
    # Sort list in ascending order
    return sorted(set(arrayA + arrayB)) # sets in python remove dupes automatically due to the way that they are stored in memory





a = [1, 2, 3, 3, 4, 5, 6]
b = [4, 4, 5, 6, 7, 8, 9]
c = merge_arrays(a, b)

print(c)