# Q3.py
def count_pairs(arr, k):
    pairs = set()
    seen = set()
    for num in arr:
        if k - num in seen:
            pairs.add((num, k - num))
        seen.add(num)
    return len(pairs)

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 6
    print("Pair count:", count_pairs(arr, k))
