def sum_of_digits(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

# Example usage
print("Sum of digits:", sum_of_digits(987))
