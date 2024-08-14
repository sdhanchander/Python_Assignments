def count_frequency(lst):
    from collections import Counter
    return dict(Counter(lst))

# Example usage
print("Frequency count:", count_frequency([1, 2, 3, 2, 4, 1, 2, 4, 5]))
