def reverse_number(num):
    revnum = 0
    while num > 0:
        revnum = revnum * 10 + num % 10
        num //= 10
    return revnum

# Example usage
print("Reversed number:", reverse_number(12345))
