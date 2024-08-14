# Q7.py
def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

# Example usage
if __name__ == "__main__":
    number_list = [7, 2, 5, 1, 9, 3]
    print(f"Median: {find_median(number_list)}")
