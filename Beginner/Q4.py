def sum_of_odd_numbers(start, stop):
    return sum(x for x in range(start, stop + 1) if x % 2 != 0)

# Example usage
print("Sum of odd numbers:", sum_of_odd_numbers(1, 10))
